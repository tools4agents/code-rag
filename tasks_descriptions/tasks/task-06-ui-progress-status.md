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

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-04-backend-indexing-job-progress.md`](tasks_descriptions/tasks/task-04-backend-indexing-job-progress.md), [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md)

## Execution Status
- Current State: planned
- Next Step: согласовать UI state mapping с backend status model
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-06-ui-progress-status.md`)

