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

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md`](tasks_descriptions/tasks/task-02-web-ui-api-contract-openapi.md), [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md)

## Execution Status
- Current State: planned
- Next Step: формализовать UI schema полей и валидационные ограничения
- Blockers: none
- Contract Changes: none
- Verification: создан planning artifact (`tasks_descriptions/tasks/task-07-ui-settings-forms.md`)
