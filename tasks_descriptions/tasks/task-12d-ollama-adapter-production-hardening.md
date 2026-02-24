# Задача T12D: Ollama adapter production hardening

## Контекст
- Источник: необходимость перейти от dummy adapter к production behavior в рамках Variant B.
- Текущая реализация-заглушка: [`services/code-rag-backend/packages/rag4code-ollama/src/rag4code_ollama/adapter.py`](services/code-rag-backend/packages/rag4code-ollama/src/rag4code_ollama/adapter.py).

## Architecture Context References
- [ ] Provider error classification pattern: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)
- [ ] Plugin mechanism и entry points: [`services/code-rag-backend/docs/theory/entry_points_mechanism.md`](services/code-rag-backend/docs/theory/entry_points_mechanism.md)

## Specification References
- [ ] Provider capabilities schema: [`services/code-rag-backend/docs/contracts/v1/provider_capabilities.schema.json`](services/code-rag-backend/docs/contracts/v1/provider_capabilities.schema.json)
- [ ] OpenAPI settings/indexing boundaries: [`services/code-rag-backend/docs/contracts/web-ui.openapi.yaml`](services/code-rag-backend/docs/contracts/web-ui.openapi.yaml)

## Test Design References
- [ ] L2 contract tests baseline: [`services/code-rag-backend/tests/contracts/test_v1_schemas.py`](services/code-rag-backend/tests/contracts/test_v1_schemas.py)
- [ ] Error path expectations: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:321)

## Цель
- Сделать `rag4code-ollama` production-ready adapter с реальными HTTP вызовами, timeout/retry и нормализацией provider errors.

## Шаги реализации
- [ ] Реализовать HTTP client взаимодействие с Ollama embeddings endpoint.
- [ ] Добавить timeout, retry policy и connection error handling.
- [ ] Нормализовать provider errors в доменные error codes.
- [ ] Добавить unit/integration tests для happy path и failure path.

## Definition of Done
- [ ] Adapter возвращает реальные embeddings вместо dummy vector.
- [ ] Ошибки `model_not_found/context_length_exceeded/timeout/connection_error` корректно классифицируются.
- [ ] Тесты покрывают основные failure scenarios.
- [ ] README адаптера документирует runtime requirements.

## Execution Status
- Current State: planned.
- Next Step: заменить dummy реализацию на HTTP client слой.
- Blockers: none.
- Contract Changes: none.
- Verification: воспроизводимый тест вызова embeddings endpoint и обработка ошибок.

