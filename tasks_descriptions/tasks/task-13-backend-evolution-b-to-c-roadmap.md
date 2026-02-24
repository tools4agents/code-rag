# Задача T13: Backend evolution roadmap B -> C

## Контекст
- Источник: принятое архитектурное решение в [`plans/backend-package-architecture-variant-b-with-c-evolution.md`](plans/backend-package-architecture-variant-b-with-c-evolution.md).
- Цель: запланировать контролируемый переход от Variant B к Variant C.

## Architecture Context References
- [ ] Component boundaries и multi-repo стратегия: [`docs/architecture.md`](docs/architecture.md:70)
- [ ] Принципы расширяемости и plugin-first подход: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)

## Specification References
- [ ] Variant B/C package plan: [`plans/backend-package-architecture-variant-b-with-c-evolution.md`](plans/backend-package-architecture-variant-b-with-c-evolution.md)
- [ ] Backend API contract baseline: [`services/code-rag-backend/docs/contracts/web-ui.openapi.yaml`](services/code-rag-backend/docs/contracts/web-ui.openapi.yaml)

## Test Design References
- [ ] L2 contract baseline: [`services/code-rag-backend/docs/testing/suites/contracts-v1.md`](services/code-rag-backend/docs/testing/suites/contracts-v1.md)
- [ ] L4 follow-up dependencies: [`tasks_descriptions/tasks/task-09-testing-l4-ui-e2e-visual.md`](tasks_descriptions/tasks/task-09-testing-l4-ui-e2e-visual.md)

## Цель
- Подготовить non-breaking migration plan для выделения `rag4code-project-registry` и `rag4code-provider-catalog` после стабилизации Variant B.

## Шаги реализации
- [ ] Определить trigger criteria для старта перехода в Variant C.
- [ ] Описать extraction sequence: `project-registry` -> `provider-catalog`.
- [ ] Зафиксировать compatibility rules для OpenAPI и schema contracts.
- [ ] Добавить проверочный checklist для migration completion.

## Definition of Done
- [ ] Есть документированный migration plan с фазами и gates.
- [ ] Контрактная совместимость для B -> C описана явно.
- [ ] Риски migration и mitigation actions перечислены.
- [ ] Handoff для Code mode готов к исполнению.

## Execution Status
- Current State: planned.
- Next Step: определить критерии перехода и order extraction шагов.
- Blockers: none.
- Contract Changes: none.
- Verification: наличие утвержденного migration checklist и gate критериев.

