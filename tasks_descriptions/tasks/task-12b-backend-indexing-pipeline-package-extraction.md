# Задача T12B: Backend Indexing Pipeline package extraction

## Контекст
- Источник: [`plans/backend-package-architecture-variant-b-with-c-evolution.md`](plans/backend-package-architecture-variant-b-with-c-evolution.md).
- Зависит от: [`tasks_descriptions/tasks/task-12a-backend-domain-core-package-extraction.md`](tasks_descriptions/tasks/task-12a-backend-domain-core-package-extraction.md).

## Architecture Context References
- [ ] Modular orchestration pattern: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)
- [ ] Plugin-driven architecture: [`docs/adr/002-plugin-system-entrypoints.md`](docs/adr/002-plugin-system-entrypoints.md)

## Specification References
- [ ] Variant B package plan: [`plans/backend-package-architecture-variant-b-with-c-evolution.md`](plans/backend-package-architecture-variant-b-with-c-evolution.md)
- [ ] Текущая engine orchestration: [`services/code-rag-backend/src/code_rag_backend/core/engine.py`](services/code-rag-backend/src/code_rag_backend/core/engine.py:7)

## Test Design References
- [ ] Канонический test design: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259)
- [ ] Backend unit baseline: [`services/code-rag-backend/docs/testing/test-map.md`](services/code-rag-backend/docs/testing/test-map.md)

## Цель
- Выделить reusable package `rag4code-indexing-pipeline` для orchestration сценариев `chunk -> embed -> upsert`.

## Шаги реализации
- [ ] Создать package skeleton `packages/rag4code-indexing-pipeline`.
- [ ] Перенести orchestration use-cases из текущего core слоя.
- [ ] Подключить dependency на domain-core и adapter interfaces.
- [ ] Добавить extension points для retry/cancel/progress hooks.

## Definition of Done
- [ ] Pipeline use-cases работают через package API.
- [ ] Backend service использует package вместо локальной реализации orchestration.
- [ ] Тесты на indexing flow проходят после extraction.
- [ ] Документация по pipeline API добавлена.

## Execution Status
- Current State: planned.
- Next Step: создать package и вынести базовый indexing use-case.
- Blockers: none.
- Contract Changes: none.
- Verification: запуск unit/contract tests на indexing сценариях.

