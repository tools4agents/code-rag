# Stage 2 Specification for code-rag

> **Status**: Accepted
>
> **Date**: 2026-02-20
>
> **Related**:
> - [Architecture](../architecture.md)
> - [ADR 002 Plugin System](../adr/002-plugin-system-entrypoints.md)
> - [Code Atlas ADR 003](../../../code-atlas/docs/adr/0003-rag-integration-strategy.md)

## 1. Scope

Документ фиксирует Stage 2 для `code-rag`:
- архитектурные границы;
- контракт интеграции `code-atlas -> code-rag`;
- Web UI требования и границу Web UI -> `code-rag` API (без детализации схем);
- правила хранения и аудита;
- reconcile протокол в режимах `dry_run` и `fix`.

## 2. Functional Goals

1. Автономная индексация и поиск по коду.
2. Опциональная интеграция с `code-atlas` в Push-first модели.
3. Изоляция данных через namespace strategy.
4. Трассируемость индексации через Git-aware аудит.
5. Контур восстановления консистентности `reconcile`.

## 3. Non-Goals

- Оркестрация всех слоев HyperGraph в одном сервисе.
- Перенос AST логики из `code-atlas` внутрь `code-rag`.
- Одновременная работа нескольких vector backend в одном процессе.

## 4. Service Boundaries

### 4.1 code-rag owns
- chunking and embedding orchestration;
- vector index write and retrieval;
- namespace lifecycle;
- reconcile reports and fixes.

### 4.2 code-atlas owns
- stable symbol IDs;
- code graph and structural context;
- symbol extraction payload for push events.

## 5. HSM Assembly Model

`services/code-rag/packages` считаются клиентскими пакетами для внешних сервисов.

Рантаймы сервисов:
- docker service;
- isolated python VES runtime.

Связь через `implies`:
- abstract client implies abstract service;
- concrete client implies concrete service.

Пример:
- `vector-db-client` implies `vector-db-service`;
- `qdrant-client` implies `qdrant-service`.

## 6. Plugin Contracts

Entry point groups:
- `rag4code.vector_db`
- `rag4code.embedder`
- `rag4code.chunker`

Provider requirements:
1. deterministic init from config;
2. explicit capability flags in provider metadata;
3. stable error envelope for runtime failures.

## 7. Namespace Strategy

Namespace format:

`project_key/purpose/chunk_strategy`

Where:
- `project_key`: project or tenant identity;
- `purpose`: `code_search` | `atlas_graph` | `docs_search`;
- `chunk_strategy`: strategy identifier.

Namespace examples:
- `root/code_search/simple_file_chunks`
- `root/atlas_graph/code_atlas_provider`

## 8. Push-first Contract

### 8.1 Batch envelope

```json
{
  "contract_version": "1.0",
  "project": "root",
  "source": "code-atlas",
  "batch_id": "atlas-batch-2026-02-20T12:00:00Z",
  "items": []
}
```

### 8.2 Item contract

```json
{
  "node_id": "func:src/auth.py:AuthService.login",
  "node_type": "function",
  "path": "src/auth.py",
  "language": "python",
  "content": "def login ...",
  "range": {
    "start_line": 10,
    "end_line": 42
  },
  "source_audit": {
    "git_commit": "abc123",
    "git_branch": "main",
    "git_dirty": false,
    "captured_at": "2026-02-20T12:00:00Z"
  },
  "symbol_meta": {
    "module": "src.auth",
    "qualname": "AuthService.login"
  }
}
```

### 8.3 Acceptance response

```json
{
  "batch_id": "atlas-batch-2026-02-20T12:00:00Z",
  "accepted": 10,
  "rejected": 1,
  "errors": [
    {
      "node_id": "func:src/auth.py:broken",
      "code": "VALIDATION_ERROR",
      "message": "content is empty"
    }
  ]
}
```

## 9. Index Record Metadata

Каждая запись индекса должна содержать:

1. **Identity**
   - `node_id`
   - `project`
   - `namespace`

2. **Chunk Context**
   - `chunk_id`
   - `chunk_strategy`
   - `path`
   - `start_line`
   - `end_line`

3. **Source Audit**
   - `source_system`
   - `source_batch_id`
   - `git_commit`
   - `git_branch`
   - `git_dirty`
   - `source_captured_at`

4. **Index Audit**
   - `indexed_at`
   - `indexer_version`
   - `embedder_provider`
   - `embedder_model`
   - `vector_backend`

## 10. Reconcile Protocol

### 10.1 Inputs
- `project`
- optional `namespace`
- `mode`: `dry_run` | `fix`
- optional `batch_id`

### 10.2 Detection rules
- **missing**: есть source элемент, нет index записи;
- **stale**: `git_commit` или hash не совпадает;
- **orphan**: есть index запись без source элемента.

### 10.3 Modes

#### dry_run
- Ничего не меняет.
- Возвращает diff отчет по `missing`, `stale`, `orphan`.

#### fix
- Применяет изменения:
  - upsert missing;
  - reindex stale;
  - delete orphan according policy.
- Возвращает applied actions report.

### 10.4 Reconcile response

```json
{
  "project": "root",
  "namespace": "root/atlas_graph/code_atlas_provider",
  "mode": "dry_run",
  "summary": {
    "missing": 2,
    "stale": 5,
    "orphan": 1
  },
  "actions": []
}
```

## 11. Query Contract

Required query params:
- `query`
- `project`
- optional `purpose`
- optional `chunk_strategy`
- optional `top_k`

Query output includes:
- matched chunks;
- score;
- `node_id`;
- path and line range;
- source and index audit metadata.

## 12. Error Model

Standard error envelope:

```json
{
  "error": {
    "code": "NAMESPACE_NOT_FOUND",
    "message": "namespace is not initialized",
    "details": {}
  }
}
```

Recommended codes:
- `VALIDATION_ERROR`
- `UNSUPPORTED_CONTRACT_VERSION`
- `NAMESPACE_NOT_FOUND`
- `PROVIDER_NOT_AVAILABLE`
- `BACKEND_UNAVAILABLE`
- `RECONCILE_FAILED`

## 13. Test Design for Stage 2

Цель раздела: зафиксировать набор проверок по уровням L1–L4, достаточный для Stage 3 (Planning) без додумывания.

### Level 1 Unit (Logic / Intent)
Фокус: чистая логика без IO.
- Namespace key builder
  - входы: `project_key`, `purpose`, `chunk_strategy`
  - ожидаемое: детерминированный формат как в [`docs/architecture/stage-2-specification.md:79`](docs/architecture/stage-2-specification.md:79)
- Metadata mapping
  - вход: push item (или локальный индексируемый объект)
  - ожидаемое: заполнение обязательных полей `Identity`, `Chunk Context`, `Source Audit`, `Index Audit` как в [`docs/architecture/stage-2-specification.md:147`](docs/architecture/stage-2-specification.md:147)
- Reconcile diff classifier
  - случаи: `missing`, `stale`, `orphan` как в [`docs/architecture/stage-2-specification.md:186`](docs/architecture/stage-2-specification.md:186)

### Level 2 Contract (Component / Mocked)
Фокус: проверка форм контрактов на границах (schema-first) и стабильного error envelope.
- Push-first contract
  - валидировать batch envelope и item contract по структуре из [`docs/architecture/stage-2-specification.md:92`](docs/architecture/stage-2-specification.md:92)
  - негативные кейсы: пустой `content`, неизвестный `contract_version`, отсутствующий `node_id`
- Acceptance response
  - формат ответа и ошибки как в [`docs/architecture/stage-2-specification.md:130`](docs/architecture/stage-2-specification.md:130)
- Error model
  - envelope shape и обязательные поля как в [`docs/architecture/stage-2-specification.md:236`](docs/architecture/stage-2-specification.md:236)
- Query contract
  - required params и shape результата как в [`docs/architecture/stage-2-specification.md:220`](docs/architecture/stage-2-specification.md:220)

### Level 3 System (Integration / Real World)
Фокус: реальные зависимости (vector backend, embedder) без UI.
- Local indexing happy path
  - index -> query: запись чанков и поиск по ним на реальном backend
  - проверка: наличие audit metadata в выдаче
- Push-first emulation
  - эмуляция `code-atlas` push -> index write on real vector backend
- Reconcile
  - `dry_run` возвращает diff отчет без изменений
  - `fix` применяет upsert/reindex/delete согласно политике и возвращает applied actions report

### Level 4 Environment (E2E / High-Fidelity)
Фокус: HSM assembled stack и полный пользовательский сценарий.
- Sandbox bootstrapping
  - запуск assembled окружения (HSM) с реальными зависимостями
- End-to-end flows
  - create/select project -> configure chunker/embedder -> start indexing -> observe progress -> search
  - reconcile `dry_run` -> reconcile `fix` -> verify consistency
- Web UI flows (в паре с backend)
  - отображение списка проектов и переключение между ними
  - отображение статуса готовности и прогресса индексации
  - изменение настроек chunker (`chunk_size`, `chunk_overlap`) и embedder model (Stage 2: `qwen3-embedding`)

#### Frontend & Visual Assurance (методология)
Цель: гарантировать не только функциональную корректность UI, но и визуальную целостность.

- Cross-browser coverage
  - основные движки: Chromium (Blink) и Firefox (Gecko)
  - Safari (WebKit) в Stage 2 не является обязательным таргетом
- Visual Regression Testing
  - инструмент: Playwright screenshots (golden master)
  - правила: избегать флакеров (динамический контент, timestamps), стабилизировать данные через тестовый seed
  - стратегия: критические экраны (project list, project details/status, settings) покрываются визуальными снапшотами
- E2E сценарии UI
  - happy path: create/select project -> configure -> start indexing -> observe progress -> search
  - error path: backend unavailable / provider unavailable -> корректный error envelope отображается пользователю

## 14. Risks and Mitigations

1. **ID drift between atlas and rag**
   - mitigate by strict `node_id` contract and reconcile.

2. **Namespace explosion**
   - mitigate by policy and cleanup automation.

3. **Provider mismatch in runtime**
   - mitigate by HSM implies declarations and startup validation.

## 15. Web UI (React) Requirements

Web UI является отдельным frontend сервисом (React) и поставляется как Docker container.

### 15.1 Responsibilities
- Web UI управляет конфигурацией проектов и отображением статуса.
- Web UI работает в Docker-контейнере и не читает файловую систему хоста напрямую.
- Backend `code-rag` на текущем этапе запускается как локальный `uv` VES runtime (host process) и имеет доступ к файловой системе ОС.
  - Выбор источников (папок проектов) осуществляется через backend API.
  - Для безопасности и воспроизводимости рекомендуется фиксировать `project_root` явно (даже если технически backend имеет доступ ко всем путям).

### 15.2 Required capabilities (Stage 2 subset)
UI должен уметь отображать список существующих проектов и переключаться между ними.

Для каждого проекта UI должен уметь:
1. Выбирать проект-источник (папку с текстовыми файлами) для которого поддерживаем vector index и семантический поиск.
   - Базовая стратегия именования: name по папке, но пользователь может изменить display name.
2. Отображать прогресс чанкирования/индексации (progress bar) и текущий статус готовности.
3. Выбирать chunker strategy и настройки.
   - Stage 2: только file chunker.
   - Настройки: `chunk_size`, `chunk_overlap`.
4. Выбирать embedder model и параметры использования.
   - Stage 2: только `qwen3-embedding`.

Примечание: точный backend API контракт для Web UI фиксируется отдельным Contract-First документом/схемой на Stage 3.

## 16. Acceptance Criteria

1. Архитектура и спецификация Stage 2 зафиксированы в документации.
2. Push-first контракт описан и валидируем.
3. Reconcile протокол включает оба режима `dry_run` и `fix`.
4. HSM client service модель и `implies` отражены в документах.
