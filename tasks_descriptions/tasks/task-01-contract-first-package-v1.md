# Задача T01: Contract-First пакет схем v1

## Контекст
- На Stage 3 нужно формализовать contract artifacts в [`services/code-rag-backend/docs/contracts/v1/`](services/code-rag-backend/docs/contracts/v1/) для Contract-First разработки.
- Входной источник: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секции 2, 5.1, 5.4.
- Набор схем уже существует, требуется проверить coverage и согласованность со Stage 2 specification.

## Шаги реализации
1. Проверить, что полный набор схем в [`services/code-rag-backend/docs/contracts/v1/`](services/code-rag-backend/docs/contracts/v1/) покрывает push, reconcile, query, error envelope, provider capabilities.
2. Сверить metadata и versioning semantics с `contract_version = 1.0` из Stage 2 спецификации.
3. Убедиться, что примеры из Stage 2 валидируются текущими схемами.
4. Уточнить [`services/code-rag-backend/docs/contracts/README.md`](services/code-rag-backend/docs/contracts/README.md): границы v1 package и policy совместимости.
5. На основе исследования [`tasks_descriptions/research/reasearch_results.md`](tasks_descriptions/research/reasearch_results.md) добавить/уточнить provider capabilities для Ollama-моделей:
   - `supports_dimensions` (true/false)
   - `supports_instruction` (true/false)
   - `max_context_tokens` (model-specific)
   - `recommended_query_instruction` (optional)

## Критерии готовности (Definition of Done)
- [ ] Схемы в [`services/code-rag-backend/docs/contracts/v1/`](services/code-rag-backend/docs/contracts/v1/) покрывают домены: push, reconcile, query, errors, provider capabilities.
- [ ] Задокументированы правила версионирования: breaking -> `v2/`, non-breaking -> расширение `v1/`.
- [ ] README контрактов отражает фактическую структуру и usage.
- [ ] Описан и воспроизводим путь валидации sample payloads.
- [ ] Provider capabilities отражают различия `qwen3-embedding` vs `bge-m3`.

## Architecture Context References
- Базовая архитектура и границы компонентов: [`docs/architecture.md`](docs/architecture.md)
- Контрактные принципы и границы Stage 2: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:64)

## Specification References
- Входная спецификация Stage 3: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:35)
- Политика contract package и версионирования: [`services/code-rag-backend/docs/contracts/README.md`](services/code-rag-backend/docs/contracts/README.md)

## Test Design References
- Канонический дизайн тестов L1–L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259).
- Релевантный уровень для задачи: L2 Contract (schema-first): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:274).
- Обязательные проверки по задаче:
  - Push-first contract и негативные кейсы: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:276).
  - Acceptance response shape: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:279).
  - Error envelope: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:281).
  - Query contract: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:283).
  - Практическая матрица L2 payload validation: [`services/code-rag-backend/docs/contracts/contract-tests.md`](services/code-rag-backend/docs/contracts/contract-tests.md:1).

## Зависимости
- Нет (entry task).

## Execution Status
- Current State: implemented (v1 schemas reviewed, provider capabilities updated, L2 contract tests added)
- Next Step: поддерживать тест-матрицу при изменении схем `v1/`
- Blockers: none
- Contract Changes: present
- Verification: `cd services/code-rag-backend && uv run pytest tests/contracts/test_v1_schemas.py`
