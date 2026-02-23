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
- [ ] Backend возвращает status и progress в стабильной форме.
- [ ] UI может использовать данные для корректного progress bar.
- [ ] Ошибки и невалидные transitions обрабатываются предсказуемо.
- [ ] В status/details отражены model-specific параметры запуска индексации.
- [ ] Unit tests покрывают основной lifecycle и edge cases.

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`](tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md), [`tasks_descriptions/tasks/task-03-backend-project-registry-crud.md`](tasks_descriptions/tasks/task-03-backend-project-registry-crud.md)

## Execution Status
- Current State: planned
- Next Step: согласовать state model и структуру progress payload
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-04-backend-indexing-job-progress.md`)
