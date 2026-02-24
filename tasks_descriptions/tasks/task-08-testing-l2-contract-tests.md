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

## Architecture Context References
- Контрактные границы и error model Stage 2: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:64)
- Общая архитектура сервиса: [`docs/architecture.md`](docs/architecture.md)

## Specification References
- Входная спецификация Stage 3 Testing: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:120)
- Контрактные схемы для L2: [`docs/contracts/v1/`](docs/contracts/v1/)

## Test Design References
- Канонический дизайн тестов L1–L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259).
- Релевантный уровень для задачи: L2 Contract (Component/Mocked): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:274).
- Обязательные проверки по задаче:
  - Push-first contract и негативные кейсы: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:276).
  - Acceptance response: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:279).
  - Error model / envelope: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:281).
  - Query contract: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:283).
  - Детализированная матрица L2 кейсов по схемам: [`docs/contracts/contract-tests.md`](docs/contracts/contract-tests.md:1).
  - Модель-специфичные L2 кейсы (`qwen3-embedding`, `bge-m3`): [`tasks_descriptions/research/reasearch_results.md`](tasks_descriptions/research/reasearch_results.md:450).

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-01-contract-first-package-v1.md`](tasks_descriptions/tasks/task-01-contract-first-package-v1.md), [`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`](tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md)

## Execution Status
- Current State: planned
- Next Step: выбрать инструментарий schema validation и зафиксировать test matrix
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-08-testing-l2-contract-tests.md`)
