# Задача T03: Backend Project Registry (CRUD)

## Контекст
- UI-слою нужен стабильный источник данных по проектам (`path + display_name`).
- Требование зафиксировано в [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секции 3 и 5.2.
- Реализация должна соответствовать DDD-паттерну проекта: thin interface layer над core.

## Шаги реализации
1. Спроектировать модель `ProjectRegistry` в backend core (entity + repository contract).
2. Реализовать CRUD-операции: list/create/update/get details.
3. Добавить валидацию входных данных (валидный path, уникальность project id/display name policy).
4. Экспортировать use-cases в API-слой, совместимый с Web UI contract.
5. Добавить unit tests для registry logic и error paths.

## Критерии готовности (Definition of Done)
- [ ] Backend хранит и возвращает список проектов в стабильном формате.
- [ ] Поддерживаются операции list/create/update/details.
- [ ] Ошибки возвращаются консистентно с error envelope policy.
- [ ] Unit tests покрывают happy path и ключевые негативные сценарии.

## Architecture Context References
- Принцип отделения Core и интерфейсов: [`docs/architecture.md`](docs/architecture.md)
- Сервисные границы Stage 2: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:35)

## Specification References
- Входная спецификация Stage 3 Backend Registry: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:103)
- API-контракт для совместимости с UI: [`docs/contracts/web-ui.openapi.yaml`](docs/contracts/web-ui.openapi.yaml)

## Test Design References
- Канонический дизайн тестов L1–L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259).
- Релевантные уровни для задачи:
  - L1 Unit (logic/intent): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:263).
  - L2 Contract (границы и error envelope): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:274).
- Обязательные проверки по задаче:
  - Детерминированная бизнес-логика registry и валидация edge cases (L1): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:263).
  - Консистентный error envelope (L2): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:281).
  - Проверка required params/shape ответов на API-границе (L2): [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:283).

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-01-contract-first-package-v1.md`](tasks_descriptions/tasks/task-01-contract-first-package-v1.md), [`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`](tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md)

## Execution Status
- Current State: planned
- Next Step: определить backend модель и storage strategy для project registry
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-03-backend-project-registry-crud.md`)
