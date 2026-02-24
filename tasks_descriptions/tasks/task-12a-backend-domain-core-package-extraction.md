# Задача T12A: Backend Domain Core package extraction

## Контекст
- Источник: [`plans/backend-package-architecture-variant-b-with-c-evolution.md`](plans/backend-package-architecture-variant-b-with-c-evolution.md).
- Решение: реализуем Variant B как текущий target package architecture.

## Architecture Context References
- [ ] Архитектурные границы backend component repo: [`docs/architecture.md`](docs/architecture.md:74)
- [ ] Системные паттерны modular backend: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)

## Specification References
- [ ] Пакетная декомпозиция Variant B: [`plans/backend-package-architecture-variant-b-with-c-evolution.md`](plans/backend-package-architecture-variant-b-with-c-evolution.md)
- [ ] Текущая lifecycle модель: [`services/code-rag-backend/src/code_rag_backend/core/indexing_job.py`](services/code-rag-backend/src/code_rag_backend/core/indexing_job.py:182)

## Test Design References
- [ ] L1-L4 канон: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259)
- [ ] Unit suite indexing lifecycle: [`services/code-rag-backend/docs/testing/suites/unit-indexing-job-lifecycle.md`](services/code-rag-backend/docs/testing/suites/unit-indexing-job-lifecycle.md)

## Цель
- Выделить reusable package `rag4code-domain-core` с доменными моделями, инвариантами и ошибками.

## Шаги реализации
- [ ] Создать package skeleton `packages/rag4code-domain-core`.
- [ ] Перенести/адаптировать доменные сущности indexing lifecycle и error model.
- [ ] Стабилизировать публичный API package для потребления pipeline/api слоями.
- [ ] Обновить import boundaries в backend service.

## Definition of Done
- [ ] `rag4code-domain-core` собирается как отдельный package.
- [ ] Domain модели и ошибки переиспользуются из package, а не из локального core monolith.
- [ ] Unit tests обновлены и проходят.
- [ ] Документация package API добавлена.

## Execution Status
- Current State: planned.
- Next Step: создать package scaffold и вынести lifecycle domain модели.
- Blockers: none.
- Contract Changes: none.
- Verification: запуск unit tests для lifecycle после переноса.

