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

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md), [`tasks_descriptions/tasks/task-06-ui-progress-status.md`](tasks_descriptions/tasks/task-06-ui-progress-status.md), [`tasks_descriptions/tasks/task-07-ui-settings-forms.md`](tasks_descriptions/tasks/task-07-ui-settings-forms.md)

## Execution Status
- Current State: planned
- Next Step: подготовить playwright конфигурацию и определить baseline snapshots
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-09-testing-l4-ui-e2e-visual.md`)

