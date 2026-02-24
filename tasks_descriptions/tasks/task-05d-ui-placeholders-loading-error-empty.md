# Задача T05D: UI Placeholders (Loading, Error, Empty)

## Контекст
- Источник: декомпозиция [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md).
- Требуется как foundation для T06/T07: [`tasks_descriptions/tasks/task-06-ui-progress-status.md`](tasks_descriptions/tasks/task-06-ui-progress-status.md), [`tasks_descriptions/tasks/task-07-ui-settings-forms.md`](tasks_descriptions/tasks/task-07-ui-settings-forms.md).

## Architecture Context References
- [ ] UI responsibilities и states в Web UI: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:351)
- [ ] Общие UI границы: [`docs/architecture.md`](docs/architecture.md:155)

## Specification References
- [ ] T05 route screen scope: [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md:16)
- [ ] Stage 3 planning input по UI: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:111)

## Test Design References
- [ ] L4 UI flow требования: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:297)
- [ ] Error-path дизайн: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:321)

## Цель
- Ввести унифицированные reusable placeholders для состояний загрузки, ошибки и пустых данных.

## Шаги реализации
- [ ] Создать generic компоненты `LoadingStub`, `ErrorStub`, `EmptyStub`.
- [ ] Подключить placeholders на pages `/projects`, `/projects/:projectId`, `/settings`.
- [ ] Добавить единый интерфейс пропсов для текстов, retry action и вариаций.
- [ ] Убедиться, что визуальный стиль placeholders согласован с AppShell.

## Definition of Done
- [ ] На каждой ключевой странице есть все три состояния.
- [ ] Placeholders переиспользуются без копипаста.
- [ ] Error state поддерживает retry callback.
- [ ] Структура компонентов готова для data integration в T06/T07.

## Execution Status
- Current State: planned.
- Next Step: добавить reusable stubs и интегрировать их в page templates.
- Blockers: none.
- Contract Changes: none.
- Verification: ручной прогон всех placeholder states на route pages.

