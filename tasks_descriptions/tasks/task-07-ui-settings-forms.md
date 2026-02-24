# Задача T07: UI Settings формы (Chunker/Embedder)

## Контекст
- Stage 3 включает настройку параметров chunker и embedder в UI.
- Требования: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md), секция 5.3.
- Базовые поля: `chunk_size`, `chunk_overlap`, `embedder_model` (Stage 2: `qwen3-embedding`).
- По результатам исследования [`tasks_descriptions/research/reasearch_results.md`](tasks_descriptions/research/reasearch_results.md):
  - для `qwen3-embedding` нужно поддержать optional `instruction` (query-side) и optional `dimensions`;
  - для `bge-m3` `instruction` не обязателен, `dimensions` по умолчанию не настраивается.

## Шаги реализации
1. Создать settings form для chunker параметров (`chunk_size`, `chunk_overlap`) с валидацией.
2. Создать settings form для выбора embedder model с дефолтным значением `qwen3-embedding`.
3. Добавить model-aware поля:
   - `dimensions` (показывать только если модель поддерживает);
   - `instruction` для query embedding (рекомендуемый сценарий для `qwen3-embedding`).
4. Интегрировать загрузку defaults/capabilities из settings catalogs API.
5. Реализовать сохранение/применение настроек к запуску индексации.
6. Добавить UI/component tests для валидации форм и сериализации payload.

## Критерии готовности (Definition of Done)
- [ ] Формы chunker и embedder отображаются и валидируют ввод.
- [ ] Значения defaults подгружаются из catalogs endpoints.
- [ ] Сформированный payload совместим с backend contract.
- [ ] UI корректно учитывает различия `qwen3-embedding` vs `bge-m3` (видимость/валидация model-specific полей).
- [ ] Тесты покрывают happy path и невалидный ввод.

## Architecture Context References
- UI требования к настройкам chunker/embedder: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:352)
- Общая архитектура и границы взаимодействия: [`docs/architecture.md`](docs/architecture.md)

## Specification References
- Входная спецификация Stage 3 по UI settings: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:117)
- API контракты settings/catalogs: [`docs/contracts/web-ui.openapi.yaml`](docs/contracts/web-ui.openapi.yaml)

## Test Design References
- Канонический дизайн тестов L1–L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259).
- Релевантные уровни для задачи:
  - L2 Contract для сериализации settings payload и error envelope: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:274).
  - L4 Environment для UI forms в пользовательском сценарии: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:297).
  - Frontend & Visual Assurance: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:309).
- Обязательные проверки по задаче:
  - Web UI settings chunker/embedder как часть UI flow: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:307).
  - E2E happy path с configure step: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:320).
  - L2/L3 модель-специфичные кейсы qwen3-embedding vs bge-m3: [`tasks_descriptions/research/reasearch_results.md`](tasks_descriptions/research/reasearch_results.md:450).

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`](tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md), [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md)

## Execution Status
- Current State: planned
- Next Step: формализовать UI schema полей и валидационные ограничения
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-07-ui-settings-forms.md`)
