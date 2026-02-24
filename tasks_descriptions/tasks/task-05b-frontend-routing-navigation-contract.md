# Задача T05B: Frontend Routing и Navigation Contract

## Контекст
- Источник: декомпозиция [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md).
- Предыдущий шаг: [`tasks_descriptions/tasks/task-05a-frontend-bootstrap-vite-tailwind.md`](tasks_descriptions/tasks/task-05a-frontend-bootstrap-vite-tailwind.md).
- Архитектурный план: [`plans/task-05-ui-skeleton-routing-architecture-plan.md`](plans/task-05-ui-skeleton-routing-architecture-plan.md).

## Architecture Context References
- [ ] UI и backend repository boundaries: [`docs/architecture.md`](docs/architecture.md:70)
- [ ] Принцип Unified Engine API для adapter-слоя: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)

## Specification References
- [ ] Stage 3 маршрутные требования: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:110)
- [ ] Базовая T05 постановка: [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md)

## Test Design References
- [ ] Канонический L1-L4 test design: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259)
- [ ] Web UI flow checks по навигации: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:304)

## Цель
- Реализовать стабильный route map и navigation поведение для экранов projects list, project details и settings.

## Шаги реализации
- [ ] Ввести route config для `/projects`, `/projects/:projectId`, `/settings`, `/` redirect и `*` fallback.
- [ ] Реализовать router module и интегрировать его в root `App`.
- [ ] Обеспечить active state в `SidebarNav` по текущему route.
- [ ] Добавить NotFound page placeholder для некорректных URL.

## Definition of Done
- [ ] Все route-path доступны через прямой URL.
- [ ] Redirect `/ -> /projects` работает стабильно.
- [ ] Fallback `*` отображает NotFound page.
- [ ] Navigation не ломает общий layout и state приложения.

## Execution Status
- Current State: planned.
- Next Step: реализовать route map и проверить navigation переходы.
- Blockers: none.
- Contract Changes: none.
- Verification: выполнить воспроизводимую ручную проверку переходов между route-path.

