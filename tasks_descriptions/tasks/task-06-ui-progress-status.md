# Задача T06: UI Progress и Status отображение

## Контекст
- Stage 3 требует визуализацию статуса индексации и progress bar на стороне UI.
- Входные требования: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секции 4 и 5.3.
- UI должен опираться на стабильный backend status contract.

## Шаги реализации
1. Реализовать client-side модель статусов и прогресса, совместимую с backend response.
2. Подключить polling/refresh стратегию для актуализации статуса indexing job.
3. Добавить UI-компоненты: progress bar, badges состояний, last update timestamp.
4. Обработать edge cases: failed/canceled/timeout states и отсутствие данных.
5. Добавить component tests для ключевых UI states.

## Критерии готовности (Definition of Done)
- [ ] Progress bar и status отображаются и обновляются без ручной перезагрузки.
- [ ] Состояния queued/running/completed/failed/canceled визуально различимы.
- [ ] Ошибки отображаются предсказуемо и не ломают экран.
- [ ] Component tests покрывают основные status transitions.

## Architecture Context References
- Требование отображения progress/status в UI: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:351)
- Общая архитектура UI-слоя: [`docs/architecture.md`](docs/architecture.md)

## Specification References
- Входная спецификация Stage 3 по UI progress/status: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:114)
- Контракт API статусов: [`services/code-rag-backend/docs/contracts/web-ui.openapi.yaml`](services/code-rag-backend/docs/contracts/web-ui.openapi.yaml)

## Test Design References
- Канонический дизайн тестов L1–L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259).
- Релевантные уровни для задачи:
  - L2 Contract для status/error payloads: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:274).
  - L4 Environment для UI status/progress flows: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:297).
  - Frontend & Visual Assurance: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:309).
- Обязательные проверки по задаче:
  - Отображение статуса готовности и прогресса индексации: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:306).
  - E2E happy path с наблюдением progress/status: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:320).
  - Error path при недоступности backend/provider: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:321).

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-04-backend-indexing-job-progress.md`](tasks_descriptions/tasks/task-04-backend-indexing-job-progress.md), [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md)

## Execution Status
- Current State: planned
- Next Step: согласовать UI state mapping с backend status model
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-06-ui-progress-status.md`)
