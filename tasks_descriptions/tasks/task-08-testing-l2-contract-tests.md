# Задача T08: L2 Contract Tests по v1 схемам

## Контекст
- Stage 3 требует перевести test design в конкретные L2 contract tests.
- Требования: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секции 4 и 5.4.
- Тесты должны валидировать payloads на контрактных границах по схемам `docs/contracts/v1/`.

## Шаги реализации
1. Настроить test harness для schema-based validation (request/response payloads).
2. Добавить тест-наборы для push/reconcile/query и provider capabilities payloads.
3. Добавить негативные сценарии: missing required fields, type mismatch, invalid enums.
4. Включить проверку error envelope для ошибок валидации и бизнес-ошибок.
5. Добавить модель-специфичные L2 кейсы на основе исследования [`tasks_descriptions/research/reasearch_results.md`](tasks_descriptions/research/reasearch_results.md):
   - `qwen3-embedding` с `dimensions` и `instruction`;
   - `bge-m3` без `instruction` и без override `dimensions`.
6. Документировать способ запуска L2 тестов и expected output.

## Критерии готовности (Definition of Done)
- [ ] L2 тесты валидируют payloads по всем схемам `v1/`.
- [ ] Негативные кейсы стабильно детектируются.
- [ ] Ошибки проверяются на соответствие error envelope.
- [ ] Покрыты отличия поведения/параметров для `qwen3-embedding` и `bge-m3`.
- [ ] Тесты воспроизводимо запускаются локально и в CI.

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-01-contract-first-package-v1.md`](tasks_descriptions/tasks/task-01-contract-first-package-v1.md), [`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`](tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md)

## Execution Status
- Current State: planned
- Next Step: выбрать инструментарий schema validation и зафиксировать test matrix
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-08-testing-l2-contract-tests.md`)
