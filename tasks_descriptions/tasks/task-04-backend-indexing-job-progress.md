# Задача T04: Backend Indexing Job Model и Progress Reporting

## Контекст
- UI должен отображать статус индексации и progress bar в реальном времени.
- Требования зафиксированы в [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секции 3 и 5.2.
- Формат ответа должен быть стабильным и совместимым с Web API contract.

## Шаги реализации
1. Спроектировать `IndexingJob` domain model (state machine, progress fields, timestamps).
2. Реализовать сервис управления lifecycle: start/status/stop (если поддерживается).
3. Определить стабильный response contract для статуса и прогресса.
4. С учетом исследования [`tasks_descriptions/research/reasearch_results.md`](tasks_descriptions/research/reasearch_results.md) добавить в job metadata параметры embedding-пайплайна: `model`, optional `dimensions`, optional `instruction`, `truncate`.
5. Добавить обработку ошибок и переходов состояний (queued/running/completed/failed/canceled), включая provider-ошибки (`model_not_found`, `context_length_exceeded`, `timeout`, `connection_error`).
6. Покрыть модель и transitions unit tests.

## Критерии готовности (Definition of Done)
- [x] Backend возвращает status и progress в стабильной форме.
- [x] UI может использовать данные для корректного progress bar.
- [x] Ошибки и невалидные transitions обрабатываются предсказуемо.
- [x] В status/details отражены model-specific параметры запуска индексации.
- [x] Unit tests покрывают основной lifecycle и edge cases.

## Architecture Context References
- Требование статусов/прогресса в UI: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:351)
- Общая архитектура сервиса: [`docs/architecture.md`](docs/architecture.md)

## Specification References
- Входная спецификация Stage 3 по Indexing Job: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:107)
- UI API контракт статусов: [`services/code-rag-backend/docs/contracts/web-ui.openapi.yaml`](services/code-rag-backend/docs/contracts/web-ui.openapi.yaml)

## Test Design References
- Канонический дизайн тестов L1–L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259).
- Релевантные уровни для задачи:
  - L1 Unit (state machine и transitions): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:263).
  - L2 Contract (status payload/error envelope): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:274).
  - L3 Integration (реальные зависимости при индексации): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:286).
- Обязательные проверки по задаче:
  - Error envelope и ошибки провайдера: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:281).
  - Проверка audit metadata в реальной выдаче при integration-сценариях: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:288).

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`](tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md), [`tasks_descriptions/tasks/task-03-backend-project-registry-crud.md`](tasks_descriptions/tasks/task-03-backend-project-registry-crud.md)

## Execution Status
- Current State: implemented in backend component core with stable lifecycle/status contract and test coverage
- Next Step: реализовать API-layer адаптеры поверх `IndexingJobService` (endpoints start/status/stop + SSE integration)
- Blockers: none
- Contract Changes: present
- Verification: `cd services/code-rag-backend && uv run pytest` (`49 passed`), suite docs updated in [`services/code-rag-backend/docs/testing/suites/unit-indexing-job-lifecycle.md`](services/code-rag-backend/docs/testing/suites/unit-indexing-job-lifecycle.md) and [`services/code-rag-backend/docs/testing/suites/openapi-web-ui.md`](services/code-rag-backend/docs/testing/suites/openapi-web-ui.md)
