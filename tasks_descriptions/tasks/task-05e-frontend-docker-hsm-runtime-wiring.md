# Задача T05E: Frontend Docker и HSM Runtime Wiring

## Контекст
- Источник: декомпозиция [`tasks_descriptions/tasks/task-05-ui-skeleton-routing.md`](tasks_descriptions/tasks/task-05-ui-skeleton-routing.md).
- Frontend service уже зарегистрирован в [`hsm-registry/services/code-rag-frontend.yaml`](hsm-registry/services/code-rag-frontend.yaml).
- Требуется подготовить стабильный dev/prod runtime path для UI.

## Architecture Context References
- [ ] HSM модель services: [`docs/architecture.md`](docs/architecture.md:47)
- [ ] Текущий HSM манифест: [`hsm.yaml`](hsm.yaml:8)

## Specification References
- [ ] Stage 3 requirement для Docker UI service: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md:110)
- [ ] T05 архитектурный план: [`plans/task-05-ui-skeleton-routing-architecture-plan.md`](plans/task-05-ui-skeleton-routing-architecture-plan.md)

## Test Design References
- [ ] L4 Environment checks: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:297)
- [ ] Frontend integration baseline: [`tasks_descriptions/tasks/task-09-testing-l4-ui-e2e-visual.md`](tasks_descriptions/tasks/task-09-testing-l4-ui-e2e-visual.md)

## Цель
- Обеспечить воспроизводимый frontend runtime в dev и prod профилях через Docker и HSM.

## Шаги реализации
- [ ] Добавить Dockerfile для dev и Dockerfile для prod/static serve.
- [ ] Добавить `nginx.conf` для prod static hosting.
- [ ] Актуализировать service fields в [`hsm-registry/services/code-rag-frontend.yaml`](hsm-registry/services/code-rag-frontend.yaml:1): ports, volumes, env.
- [ ] Определить env contract (`VITE_API_BASE_URL`, optional branding variables).

## Definition of Done
- [ ] Frontend запускается в dev container с hot reload.
- [ ] Frontend запускается в prod container и отдает static build.
- [ ] HSM registry configuration соответствует фактической структуре frontend repo.
- [ ] Environment variables документированы в frontend README.

## Execution Status
- Current State: planned.
- Next Step: подготовить Docker assets и синхронизировать service registry.
- Blockers: none.
- Contract Changes: none.
- Verification: воспроизводимый запуск frontend в dev/prod через docker и проверка доступности UI.

