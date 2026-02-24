# Задача T05C: App Shell Layout и Dark IDE Style

## Контекст
- Источник: декомпозиция [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md).
- Зависит от routing base: [`tasks_descriptions/tasks/task-05b-frontend-routing-navigation-contract.md`](tasks_descriptions/tasks/task-05b-frontend-routing-navigation-contract.md).
- Визуальный ориентир: [`plans/task-05-ui-skeleton-routing-architecture-plan.md`](plans/task-05-ui-skeleton-routing-architecture-plan.md).

## Architecture Context References
- [ ] Общая архитектура UI и component boundaries: [`docs/architecture.md`](docs/architecture.md:74)
- [ ] Repository-per-Component pattern: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)

## Specification References
- [ ] Stage 3 UI skeleton requirements: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:111)
- [ ] Базовая задача T05: [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md)

## Test Design References
- [ ] Канонический дизайн тестов: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259)
- [ ] Frontend visual assurance baseline: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:309)

## Цель
- Реализовать единый `AppShell` layout в стиле professional dark IDE с аккуратными cyberpunk accents.

## Шаги реализации
- [ ] Реализовать компоненты layout: `SidebarNav`, `TopBar`, `StatusBar`, `PageHost`.
- [ ] Ввести базовые color tokens и typography tokens для dark theme.
- [ ] Настроить responsive behavior для desktop-first и корректного mobile fallback.
- [ ] Ограничить decorative effects так, чтобы UI оставался рабочим инструментом.

## Definition of Done
- [ ] Все route pages рендерятся внутри единого `AppShell`.
- [ ] Визуальный стиль консистентен на ключевых экранах.
- [ ] Контрастность и читаемость соблюдены в dark theme.
- [ ] Layout готов к расширению под T06 и T07 без пересборки основы.

## Execution Status
- Current State: planned.
- Next Step: собрать `AppShell` и подключить его к route pages.
- Blockers: none.
- Contract Changes: none.
- Verification: выполнить визуальную проверку shell-компонентов на трех route-path.

