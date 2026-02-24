# Задача T05A: Frontend Bootstrap (Vite + React + TypeScript + Tailwind)

## Контекст
- Источник: декомпозиция [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md).
- Архитектурный план: [`plans/task-05-ui-skeleton-routing-architecture-plan.md`](plans/task-05-ui-skeleton-routing-architecture-plan.md).
- Компонентный репозиторий: [`services/code-rag-frontend/`](services/code-rag-frontend/).

## Architecture Context References
- [ ] Repository boundaries и роль frontend repo: [`docs/architecture.md`](docs/architecture.md:70)
- [ ] Thin MCP + component repo модель: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)

## Specification References
- [ ] Stage 3 UI scope: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:110)
- [ ] T05 requirements: [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md)

## Test Design References
- [ ] Канонический L1-L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259)
- [ ] UI flow focus для skeleton: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:304)

## Цель
- Поднять минимально рабочий frontend foundation для последующей реализации routing, layout и интеграции с backend API.

## Шаги реализации
- [ ] Инициализировать Vite React TypeScript проект в [`services/code-rag-frontend/`](services/code-rag-frontend/).
- [ ] Подключить Tailwind CSS и базовые design tokens для dark IDE-like темы.
- [ ] Настроить entrypoint и базовую структуру каталогов `app/layout/pages/components/styles`.
- [ ] Обновить [`services/code-rag-frontend/README.md`](services/code-rag-frontend/README.md) с командами запуска.

## Definition of Done
- [ ] Приложение стартует локально и отдает базовую страницу.
- [ ] Tailwind классы применяются корректно.
- [ ] Базовая структура каталогов готова для T05B-T05F.
- [ ] README синхронизирован с фактическими командами.

## Execution Status
- Current State: planned.
- Next Step: создать скелет проекта и проверить запуск dev server.
- Blockers: none.
- Contract Changes: none.
- Verification: подготовить воспроизводимую команду запуска frontend в dev режиме.

