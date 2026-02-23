# Задача T02: Web UI API contract (OpenAPI)

## Контекст
- Для Stage 3 нужен формальный Web API contract для UI-слоя.
- Входные требования зафиксированы в [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секции 3 и 5.1.
- Текущий артефакт: [`docs/contracts/web-ui.openapi.yaml`](docs/contracts/web-ui.openapi.yaml).

## Шаги реализации
1. Проверить, что в OpenAPI определены resources: Projects, Indexing, Settings catalogs.
2. Сверить обязательные operations: list/create/update/details для Projects; start/status/stop для Indexing; list catalogs для settings.
3. Проверить единый формат ошибок через [`docs/contracts/v1/error_envelope.schema.json`](docs/contracts/v1/error_envelope.schema.json).
4. Зафиксировать в контракте model-specific поля embedder settings на основе исследования [`tasks_descriptions/research/reasearch_results.md`](tasks_descriptions/research/reasearch_results.md):
   - `instruction` (query-side, особенно для `qwen3-embedding`),
   - `dimensions` (optional, при поддержке моделью),
   - `truncate` и служебные provider options.
5. Актуализировать описания endpoint-ов и примеры ответов для UI integration.

## Критерии готовности (Definition of Done)
- [ ] OpenAPI покрывает минимально необходимый набор resources и operations.
- [ ] Ошибки описаны консистентно через error envelope.
- [ ] Спецификация валидируется линтером/валидатором OpenAPI.
- [ ] В embedder settings отражены различия `qwen3-embedding` и `bge-m3` без нарушения единого API.
- [ ] UI-команда может использовать контракт как single source of truth.

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-01-contract-first-package-v1.md`](tasks_descriptions/tasks/task-01-contract-first-package-v1.md)

## Execution Status
- Current State: planned
- Next Step: выполнить ревью OpenAPI на полноту resources/operations
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`)
