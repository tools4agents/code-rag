# Задача T09: L4 UI Tests (Playwright E2E + Visual Regression)

## Контекст
- Stage 3 требует L4 тесты для UI flows и визуальной стабильности.
- Источник: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секции 4 и 5.4.
- Минимальные браузеры: Chromium и Firefox.

## Шаги реализации
1. Настроить Playwright test harness для E2E сценариев UI.
2. Реализовать happy-path сценарий: project selection -> settings -> start indexing -> progress/status check.
3. Подключить visual regression snapshots для ключевых экранов.
4. Обеспечить запуск тестов минимум в Chromium и Firefox.
5. Интегрировать запуск в CI pipeline и зафиксировать правила обновления snapshot-ов.

## Критерии готовности (Definition of Done)
- [ ] E2E happy-path стабильно проходит.
- [ ] Visual regression snapshots созданы и проверяются автоматически.
- [ ] Тесты запускаются в Chromium и Firefox.
- [ ] Описаны правила обслуживания snapshots и triage визуальных диффов.

## Architecture Context References
- Web UI архитектурные требования Stage 2: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:334)
- Общая архитектура и взаимодействие UI с backend: [`docs/architecture.md`](docs/architecture.md)

## Specification References
- Входная спецификация Stage 3 Testing: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:120)
- OpenAPI контракт для E2E-потоков UI: [`services/code-rag-backend/docs/contracts/web-ui.openapi.yaml`](services/code-rag-backend/docs/contracts/web-ui.openapi.yaml)

## Test Design References
- Канонический дизайн тестов L1–L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259).
- Релевантный уровень для задачи: L4 Environment (E2E / High-Fidelity): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:297).
- Frontend & Visual Assurance (методология): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:309).
- Обязательные проверки по задаче:
  - Cross-browser coverage Chromium + Firefox: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:312).
  - Visual regression golden master и правила стабилизации данных: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:315).
  - E2E happy path и error path: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:319).
  - Stage 3 требование по L4 UI tests: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:90).

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md), [`tasks_descriptions/tasks/task-06-ui-progress-status.md`](tasks_descriptions/tasks/task-06-ui-progress-status.md), [`tasks_descriptions/tasks/task-07-ui-settings-forms.md`](tasks_descriptions/tasks/task-07-ui-settings-forms.md)

## Execution Status
- Current State: planned
- Next Step: подготовить playwright конфигурацию и определить baseline snapshots
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-09-testing-l4-ui-e2e-visual.md`)
