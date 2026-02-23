# Задача T05: UI Skeleton и Routing

## Контекст
- Stage 3 требует базовый UI-каркас для дальнейшей интеграции с backend.
- Требования: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секция 5.3.
- UI разворачивается как Docker service в HSM model.

## Шаги реализации
1. Инициализировать структуру frontend-приложения (React) в рамках текущего workspace.
2. Настроить routing для экранов: projects list, project details, settings.
3. Добавить базовые layout-компоненты (navigation, page container, loading/error stubs).
4. Подготовить Docker-конфигурацию для dev/prod запуска UI через HSM.
5. Проверить, что маршруты открываются и не ломают существующую архитектурную схему.

## Критерии готовности (Definition of Done)
- [ ] Доступны 3 ключевых экрана: список проектов, экран проекта, экран настроек.
- [ ] Routing стабильно работает между экранами.
- [ ] UI запускается в Docker-контуре согласно HSM-модели.
- [ ] Базовые states (loading/error placeholder) присутствуют.

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`](tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md)

## Execution Status
- Current State: planned
- Next Step: выбрать структуру frontend каталога и bootstrap strategy
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`)

