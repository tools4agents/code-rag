# Задача T01: Contract-First пакет схем v1

## Контекст
- На Stage 3 нужно формализовать contract artifacts в [`docs/contracts/v1/`](docs/contracts/v1/) для Contract-First разработки.
- Входной источник: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секции 2, 5.1, 5.4.
- Набор схем уже существует, требуется проверить coverage и согласованность со Stage 2 specification.

## Шаги реализации
1. Проверить, что полный набор схем в [`docs/contracts/v1/`](docs/contracts/v1/) покрывает push, reconcile, query, error envelope, provider capabilities.
2. Сверить metadata и versioning semantics с `contract_version = 1.0` из Stage 2 спецификации.
3. Убедиться, что примеры из Stage 2 валидируются текущими схемами.
4. Уточнить [`docs/contracts/README.md`](docs/contracts/README.md): границы v1 package и policy совместимости.
5. На основе исследования [`tasks_descriptions/research/reasearch_results.md`](tasks_descriptions/research/reasearch_results.md) добавить/уточнить provider capabilities для Ollama-моделей:
   - `supports_dimensions` (true/false)
   - `supports_instruction` (true/false)
   - `max_context_tokens` (model-specific)
   - `recommended_query_instruction` (optional)

## Критерии готовности (Definition of Done)
- [ ] Схемы в [`docs/contracts/v1/`](docs/contracts/v1/) покрывают домены: push, reconcile, query, errors, provider capabilities.
- [ ] Задокументированы правила версионирования: breaking -> `v2/`, non-breaking -> расширение `v1/`.
- [ ] README контрактов отражает фактическую структуру и usage.
- [ ] Описан и воспроизводим путь валидации sample payloads.
- [ ] Provider capabilities отражают различия `qwen3-embedding` vs `bge-m3`.

## Зависимости
- Нет (entry task).

## Execution Status
- Current State: planned
- Next Step: выполнить review покрытия и согласованности схем со Stage 2
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-01-contract-first-package-v1.md`)
