# Задача T12C: Backend API package и OpenAPI binding

## Контекст
- Источник: [`plans/backend-package-architecture-variant-b-with-c-evolution.md`](plans/backend-package-architecture-variant-b-with-c-evolution.md).
- Зависит от: [`tasks_descriptions/tasks/task-12a-backend-domain-core-package-extraction.md`](tasks_descriptions/tasks/task-12a-backend-domain-core-package-extraction.md), [`tasks_descriptions/tasks/task-12b-backend-indexing-pipeline-package-extraction.md`](tasks_descriptions/tasks/task-12b-backend-indexing-pipeline-package-extraction.md).

## Architecture Context References
- [ ] API boundary и Web UI integration role: [`docs/architecture.md`](docs/architecture.md:68)
- [ ] Thin transport over backend core: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)

## Specification References
- [ ] Web UI OpenAPI contract: [`services/code-rag-backend/docs/contracts/web-ui.openapi.yaml`](services/code-rag-backend/docs/contracts/web-ui.openapi.yaml)
- [ ] Variant B package plan: [`plans/backend-package-architecture-variant-b-with-c-evolution.md`](plans/backend-package-architecture-variant-b-with-c-evolution.md)

## Test Design References
- [ ] L2 contract tests по OpenAPI: [`services/code-rag-backend/tests/contracts/test_openapi_contract.py`](services/code-rag-backend/tests/contracts/test_openapi_contract.py)
- [ ] Test-map backend: [`services/code-rag-backend/docs/testing/test-map.md`](services/code-rag-backend/docs/testing/test-map.md)

## Цель
- Выделить `rag4code-backend-api` как reusable transport package с contract-first binding к OpenAPI.

## Шаги реализации
- [ ] Создать package skeleton `packages/rag4code-backend-api`.
- [ ] Реализовать request/response mapping и validation boundary.
- [ ] Реализовать error envelope mapping на основе доменных ошибок.
- [ ] Подключить API package к backend runtime entrypoint.

## Definition of Done
- [ ] API endpoints соответствуют OpenAPI contract.
- [ ] Error responses соответствуют error envelope schema.
- [ ] Контрактные тесты проходят.
- [ ] Документация API package добавлена.

## Execution Status
- Current State: planned.
- Next Step: создать API package scaffold и подключить первый endpoint.
- Blockers: none.
- Contract Changes: none.
- Verification: прогон L2 OpenAPI contract tests.

