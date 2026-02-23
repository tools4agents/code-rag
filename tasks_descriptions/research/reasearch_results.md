# Ollama integration research: `qwen3-embedding` vs `bge-m3`

Below is a **verified, implementation-ready analysis** structured exactly as requested.

---

# Section 1 — Verified Facts (with sources)

## 1.1 Official Ollama embedding API (current, correct endpoint)

### Endpoint

**Canonical endpoint:**

```
POST /api/embed
```

**Request body:**

```json
{
  "model": "model-name",
  "input": "string or array[string]",
  "truncate": true,
  "dimensions": 1024,
  "keep_alive": "5m",
  "options": {}
}
```

**Response format:**

```json
{
  "model": "model-name",
  "embeddings": [[float, float, ...]],
  "total_duration": int,
  "load_duration": int,
  "prompt_eval_count": int
}
```

Source: Ollama API documentation ([docs.ollama.com][1])

**Critical facts:**

* `input` accepts **string OR array[string] (batch supported)** ([docs.ollama.com][2])
* Embeddings are **L2-normalized vectors** (important for cosine similarity) ([docs.ollama.com][2])
* `dimensions` parameter can control output vector size (model dependent) ([docs.ollama.com][1])
* `truncate` defaults to `true`, otherwise exceeding context → error ([docs.ollama.com][1])

---

## 1.2 `/api/embeddings` vs `/api/embed` (compatibility)

Key fact:

* `/api/embed` is the **current official endpoint**
* `/api/embeddings` exists mainly for OpenAI compatibility and is deprecated or inconsistent

Source: Ollama issues and release notes ([GitHub][3])

**Integration decision:**
→ Always use `/api/embed` for native Ollama provider.

---

# 1.3 Batch input support

Supported natively:

```json
{
  "model": "bge-m3",
  "input": ["text1", "text2", "text3"]
}
```

Returns:

```json
{
  "embeddings": [
    [vector1],
    [vector2],
    [vector3]
  ]
}
```

Source: Ollama embedding docs ([docs.ollama.com][2])

Batch support introduced explicitly in embedding API v0.3.4 ([newreleases.io][4])

---

# 1.4 Vector normalization behavior

Vectors returned are:

* unit-length normalized (L2 norm = 1)

Source: Ollama embedding docs ([docs.ollama.com][2])

Implication:

* Cosine similarity safe by default
* No need to normalize in backend

---

# 1.5 Qwen3-Embedding model characteristics

From Ollama model registry:

### Supported context

```
32k–40k tokens
```

### Embedding dimensions

```
Supports user-defined output dimensions from 32 to 4096
```

Source: Ollama Qwen3-Embedding page ([ollama.com][5])

Verified real output example:

```
Vector dimension: 4096
```

Source: real API example ([blog.csdn.net][6])

---

# 1.6 BGE-M3 model characteristics

From Ollama registry:

Context length:

```
8192 tokens
```

Source: Ollama model registry ([registry.ollama.ai][7])

Capabilities:

* multilingual
* dense + sparse retrieval
* multi-vector retrieval

Source: Ollama registry + academic paper ([registry.ollama.ai][7])

---

# 1.7 Vector DB integration behavior (Qdrant example)

Recommended pattern:

```python
response = oclient.embeddings(model="qwen3-embedding", prompt=text)

vector_size = len(response["embedding"])

qdrant.create_collection(
  vectors_config=models.VectorParams(
    size=vector_size,
    distance=models.Distance.COSINE
  )
)
```

Source: Qdrant official Ollama integration example ([Qdrant][8])

Implication:

* Dimension must be dynamically detected.

---

# 1.8 Model-specific parameter support

Supported request parameters:

| parameter  | supported |
| ---------- | --------- |
| model      | required  |
| input      | required  |
| dimensions | optional  |
| truncate   | optional  |
| keep_alive | optional  |
| options    | optional  |

Source: Ollama API docs ([docs.ollama.com][1])

These apply equally to all embedding models.

---

# Section 2 — Comparison Table: qwen3-embedding vs bge-m3

| Feature                    | qwen3-embedding                           | bge-m3                          |
| -------------------------- | ----------------------------------------- | ------------------------------- |
| API endpoint               | `/api/embed`                              | `/api/embed`                    |
| Request format             | identical                                 | identical                       |
| Batch support              | Yes                                       | Yes                             |
| Default dimension          | 4096 typical                              | ~1024 typical (model dependent) |
| Configurable dimensions    | Yes (32–4096)                             | Not documented configurable     |
| Max context                | 32k–40k tokens                            | 8k tokens                       |
| Multilingual               | Yes                                       | Yes                             |
| Sparse retrieval support   | No                                        | Yes                             |
| Embedding normalization    | Yes                                       | Yes                             |
| Embedding pooling          | Last-token pooling (model design)         | Mean pooling / multi-vector     |
| Vector DB implications     | dimension must match configured dimension | dimension fixed                 |
| Instruction tuning support | Yes                                       | No documented support           |
| Stability in Ollama        | newer model                               | mature, stable                  |

Sources: Ollama model pages and docs ([ollama.com][5])

---

# Section 3 — Minimal Working Examples

## Example 1 — qwen3-embedding (single)

```bash
curl http://localhost:11434/api/embed \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-embedding",
    "input": "This is a test"
  }'
```

---

## Example 2 — qwen3-embedding (batch)

```bash
curl http://localhost:11434/api/embed \
  -d '{
    "model": "qwen3-embedding",
    "input": [
      "First text",
      "Second text"
    ]
  }'
```

---

## Example 3 — qwen3-embedding with custom dimensions

```bash
curl http://localhost:11434/api/embed \
  -d '{
    "model": "qwen3-embedding",
    "input": "test",
    "dimensions": 1024
  }'
```

Supported explicitly by model docs ([ollama.com][5])

---

## Example 4 — bge-m3

```bash
curl http://localhost:11434/api/embed \
  -d '{
    "model": "bge-m3",
    "input": "This is a test"
  }'
```

---

# Section 4 — Integration Decisions for code-rag

## Decision 1: Use `/api/embed` only

Reason:

* Official
* Stable
* Supports batch
* Supports dimensions

---

## Decision 2: Unified provider contract

No need for separate backend adapters.

Strategy configuration sufficient.

Only model-specific config:

```
dimensions
max_input_tokens
```

---

## Decision 3: Vector DB schema strategy

Always dynamically detect dimension:

```
dimension = len(response.embeddings[0])
```

Never hardcode.

---

## Decision 4: Safe default configuration

Recommended defaults:

```
truncate = true
dimensions = null (model default)
batch_size = 32
timeout = 60s
```

---

# Section 5 — Contract Proposal (backend normalized contract)

## Request Contract

```ts
interface EmbeddingRequest {
  provider: "ollama"
  model: string
  input: string | string[]
  dimensions?: number
  truncate?: boolean
  timeout_ms?: number
}
```

---

## Response Contract

```ts
interface EmbeddingResponse {
  provider: "ollama"
  model: string
  embeddings: number[][]
  dimension: number
  usage?: {
    prompt_tokens?: number
    total_duration_ns?: number
  }
}
```

---

## Error Contract

```ts
interface EmbeddingError {
  provider: "ollama"
  model?: string
  type:
    | "model_not_found"
    | "model_not_loaded"
    | "context_length_exceeded"
    | "timeout"
    | "invalid_request"
    | "internal_error"
    | "connection_error"
  message: string
  retryable: boolean
}
```

---

# Section 6 — Error mapping recommendations

Common Ollama errors:

| HTTP               | cause              | normalized error |
| ------------------ | ------------------ | ---------------- |
| 404                | model not found    | model_not_found  |
| 500                | model load failure | model_not_loaded |
| 400                | invalid request    | invalid_request  |
| connection refused | server offline     | connection_error |
| timeout            | inference timeout  | timeout          |

---

# Section 7 — Backend adapter architecture recommendation

No separate adapter needed.

Use:

```
OllamaEmbeddingProvider
```

with config strategy:

```ts
interface OllamaEmbeddingStrategy {
  model: string
  dimensions?: number
}
```

Example config:

```
{
 provider: "ollama",
 model: "qwen3-embedding",
 dimensions: 1024
}
```

or

```
{
 provider: "ollama",
 model: "bge-m3"
}
```

---

# Section 8 — Test Plan Additions

## L2 Contract Tests

### Required tests

### 1. Single input embedding

```
input: "hello"
expect embeddings.length == 1
```

---

### 2. Batch embedding

```
input: ["hello", "world"]
expect embeddings.length == 2
```

---

### 3. Dimension consistency

```
dimension == embeddings[0].length
```

---

### 4. Custom dimension test (qwen only)

```
dimensions=1024
expect vector length == 1024
```

---

### 5. Model not found

expect:

```
error.type == model_not_found
```

---

### 6. Context overflow

```
truncate=false
input > context window
expect context_length_exceeded
```

---

## L3 Integration tests

### Required:

Test both models:

```
qwen3-embedding
bge-m3
```

Verify:

```
insert → retrieve → similarity search works
```

---

# Section 9 — Final Integration Recommendation Summary

## Backend adapter logic

Use unified adapter.

Model-specific logic only for:

```
dimensions support (qwen only)
max context length
```

No branching required beyond config.

---

## Recommended production defaults

For qwen3-embedding:

```
dimensions: 1024
truncate: true
batch_size: 32
```

For bge-m3:

```
dimensions: undefined
truncate: true
batch_size: 32
```

---

# Section 10 — Risks / Unknowns

## Risk 1: Dimension mismatch with vector DB

Mitigation:

Always detect dynamically.

---

## Risk 2: Some Ollama versions inconsistent with `/api/embed`

Mitigation:

Require Ollama ≥ 0.3.4

---

## Risk 3: Qwen dimension configurability not universally supported across quantizations

Mitigation:

Test dimension override at startup.

---

## Risk 4: Memory usage high for qwen3-embedding-8b

Mitigation:

Prefer:

```
qwen3-embedding:0.6b
```

---

# FINAL CONCLUSION

There is **NO architectural reason to implement separate adapters**.

Use:

```
Unified OllamaEmbeddingProvider
```

with:

```
Strategy config
```

---

If you want, I can now produce:

• production-ready TypeScript adapter implementation
• Qdrant schema auto-negotiation logic
• full error-mapping middleware

[1]: https://docs.ollama.com/api/embed?utm_source=chatgpt.com "Generate embeddings - Ollama"
[2]: https://docs.ollama.com/capabilities/embeddings?utm_source=chatgpt.com "Embeddings - Ollama"
[3]: https://github.com/ollama/ollama/issues/7242?utm_source=chatgpt.com "`api/embed` endpoint is not working exactly like `api/embeddings` endpoint · Issue #7242 · ollama/ollama · GitHub"
[4]: https://newreleases.io/project/github/ollama/ollama/release/v0.3.4?utm_source=chatgpt.com "ollama/ollama v0.3.4 on GitHub"
[5]: https://ollama.com/library/qwen3-embedding?utm_source=chatgpt.com "qwen3-embedding"
[6]: https://blog.csdn.net/applepie_max/article/details/155304285?utm_source=chatgpt.com "Ollama配置Qwen3-Embedding-8B_ollama qwen3 embedding-CSDN博客"
[7]: https://registry.ollama.ai/library/bge-m3?utm_source=chatgpt.com "bge-m3"
[8]: https://qdrant.tech/documentation/embeddings/ollama/?utm_source=chatgpt.com "Ollama - Qdrant"

## Что такое Instruction tuning support (Instruction-aware embeddings)

**Instruction tuning support** означает, что embedding-модель обучена учитывать не только сам текст, но и *инструкцию, описывающую задачу embedding*.

То есть embedding зависит от **контекста задачи**, а не только от текста.

Модели серии Qwen3-Embedding официально являются **Instruction-aware**, т.е. могут использовать инструкции для улучшения качества retrieval. ([ollama.com][1])

Причём использование инструкции обычно улучшает retrieval-качество примерно на **+1–5%**. ([ollama.com][1])

---

# Почему это важно

Обычная embedding модель:

```text
Input:
"What is the capital of China?"
```

Instruction-aware embedding:

```text
Instruct: Given a web search query, retrieve relevant passages that answer the query
Query: What is the capital of China?
```

Embedding получается **другим**, потому что модель знает:

* это search query
* не просто текст
* а именно запрос для retrieval

---

# Интуитивная аналогия

Без instruction:

```text
"apple"
```

Модель не знает — это:

* фрукт
* компания
* название проекта

С instruction:

```text
Instruct: Represent a company entity
Query: apple
```

embedding будет ближе к:

```text
Microsoft, Google, Amazon
```

а не к:

```text
banana, orange
```

---

# Как это выглядит на практике (официальный пример Qwen3)

Пример из официальной документации:

```python
def get_detailed_instruct(task_description: str, query: str) -> str:
    return f'Instruct: {task_description}\nQuery:{query}'

task = "Given a web search query, retrieve relevant passages that answer the query"

queries = [
    get_detailed_instruct(task, "What is the capital of China?"),
    get_detailed_instruct(task, "Explain gravity")
]
```

([ollama.com][2])

---

# Важно: instruction обычно применяется только к query

Правильная схема:

```text
Query embedding:
"Instruct: Given a web search query, retrieve relevant passages that answer the query
Query: What is vector database?"

Document embedding:
"Vector databases store embeddings efficiently for similarity search."
```

Instruction добавляется только к query.

Это официально рекомендовано Qwen. ([GitHub][3])

---

# Пример с Ollama + qwen3-embedding

Ollama не имеет отдельного поля instruction.
Instruction добавляется прямо в input.

## Query embedding

```bash
curl http://localhost:11434/api/embed \
-d '{
  "model": "qwen3-embedding",
  "input": "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: What is a vector database?"
}'
```

---

## Document embedding

```bash
curl http://localhost:11434/api/embed \
-d '{
  "model": "qwen3-embedding",
  "input": "A vector database stores embeddings and allows similarity search."
}'
```

---

# Batch пример (production-style)

```bash
curl http://localhost:11434/api/embed \
-d '{
  "model": "qwen3-embedding",
  "input": [
    "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: What is a vector database?",
    "A vector database stores embeddings efficiently."
  ]
}'
```

---

# Почему bge-m3 обычно не требует instruction

bge-m3 использует другой training paradigm:

```text
query: "What is vector database?"
document: "Vector databases store embeddings..."
```

без явного instruction prefix.

Иногда используется:

```text
Represent this sentence for searching relevant passages: {query}
```

но это optional.

---

# Когда instruction использовать обязательно

Use instruction для:

* semantic search
* RAG retrieval
* QA retrieval
* code search
* domain-specific retrieval

---

# Когда instruction не нужен

Не использовать instruction если:

* clustering
* semantic deduplication
* anomaly detection
* general similarity

---

# Production recommendation для вашего backend

Добавьте optional поле:

```ts
instruction?: string
```

---

# Recommended contract

```ts
interface EmbeddingRequest {
  model: string
  input: string | string[]
  instruction?: string
}
```

Backend implementation:

```ts
function buildInput(text, instruction) {
  if (!instruction) return text

  return `Instruct: ${instruction}\nQuery: ${text}`
}
```

---

# Production recommendation specifically for code-rag

Use this instruction:

```text
Given a code search query, retrieve relevant code snippets
```

Example:

```text
Instruct: Given a code search query, retrieve relevant code snippets
Query: how to create websocket server in nodejs
```

---

# Summary — practical integration impact

| Feature                       | qwen3-embedding   | bge-m3   |
| ----------------------------- | ----------------- | -------- |
| Instruction support           | YES (recommended) | optional |
| Requires special API param    | NO                |          |
| Requires input formatting     | YES               |          |
| Backend adapter change needed | minor             |          |
| Recommended use               | YES               |          |

---

# Recommended backend implementation (final)

Strategy-based:

```ts
if (model.supportsInstruction && instruction) {
  input = `Instruct: ${instruction}\nQuery: ${text}`
}
```

---

# If you want, I can also provide

* unified adapter implementation supporting instruction automatically
* or retrieval benchmarks showing real improvement % between qwen3 vs bge-m3 with instruction

[1]: https://ollama.com/dengcao/Qwen3-Embedding-8B?utm_source=chatgpt.com "dengcao/Qwen3-Embedding-8B"
[2]: https://ollama.com/ryanshillington/Qwen3-Embedding-8B?utm_source=chatgpt.com "ryanshillington/Qwen3-Embedding-8B"
[3]: https://github.com/QwenLM/Qwen3-Embedding?utm_source=chatgpt.com "GitHub - QwenLM/Qwen3-Embedding"
