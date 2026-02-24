# Задача T11: Post-Refactor Validation (Component Repos + Thin MCP Root)

## Контекст
- После рефакторинга проект разделен на component repos: backend и frontend вынесены из root.
- Root-репозиторий должен оставаться только thin MCP-слоем + orchestration/task-артефактами.
- Нужна отдельная проверка на архитектурную консистентность и отсутствие регрессий после миграции.

## Шаги реализации
1. Проверить boundary-правила по репозиториям:
   - root содержит только MCP слой (`src/code_rag/mcp/**`) + общие docs/tasks/hsm;
   - backend хранит свой код/контракты/тесты/docs в `services/code-rag-backend/**`;
   - frontend хранит свой код/docs в `services/code-rag-frontend/**`.
2. Проверить HSM-консистентность:
   - `hsm.yaml` содержит нужные services;
   - `hsm-registry/services/*` согласованы с фактическими путями;
   - `hsm check` и (при необходимости) `hsm sync --verify` проходят.
3. Проверить package/runtime слой компонентов:
   - backend собирается и запускает тесты из собственного репо;
   - import paths и package naming стабильны;
   - frontend имеет корректный базовый каркас для дальнейшей реализации.
4. Проверить документацию и задачи:
   - ссылки из task-файлов и docs ведут в актуальные component paths;
   - test-map/suite ссылки согласованы с фактическим размещением тестов;
   - architecture docs отражают repository boundaries.
5. Проверить Git ownership и изоляцию nested repos:
   - изменения не смешиваются между root и component repos;
   - карта репозиториев (`gitContext`) соответствует фактической структуре.
6. Сформировать verification report с найденными несоответствиями и remediation plan (если есть).

## Критерии готовности (Definition of Done)
- [x] Подтверждено соблюдение repository boundaries для root/backend/frontend.
- [x] HSM манифесты и реестр проходят проверки без ошибок.
- [x] Backend validation (минимум `uv run pytest`) воспроизводима из component repo.
- [x] Документация и task-ссылки не содержат устаревших root-путей для backend-артефактов.
- [x] Git context и ownership для nested repos актуализированы.
- [x] Подготовлен краткий отчет по результатам проверки и дальнейшим действиям.

## Architecture Context References
- Границы root/backend/frontend: [`docs/architecture.md`](docs/architecture.md)
- Принципы Thin MCP Layer и Repository-per-Component: [`.kilocode/rules/memory-bank/systemPatterns.md`](.kilocode/rules/memory-bank/systemPatterns.md)

## Specification References
- Stage 3 planning input: [`plans/stage-3-planning-input.md`](plans/stage-3-planning-input.md)
- HSM CLI reference: [`/home/anton-admin/Загрузки/develop/education/hyper-graph/hsm/website/docs/05-reference/cli.md`](/home/anton-admin/Загрузки/develop/education/hyper-graph/hsm/website/docs/05-reference/cli.md)

## Test Design References
- Канонический тест-дизайн L1–L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259)
- Backend test map (component repo): [`services/code-rag-backend/docs/testing/test-map.md`](services/code-rag-backend/docs/testing/test-map.md)

## Зависимости
- Зависит от: [`tasks_descriptions/tasks/task-10-python-code-style-tooling.md`](tasks_descriptions/tasks/task-10-python-code-style-tooling.md) (частично, по части унификации quality checks)

## Execution Status
- Current State: remediation for GAP-1..GAP-5 completed; backend runtime validation executed successfully (`49 passed`).
- Next Step: none.
- Blockers: none
- Contract Changes: none
- Verification: выполнена команда `cd services/code-rag-backend && uv run pytest`, результат: `49 passed in 0.35s`; документация и структура синхронизированы с post-refactor boundaries.

### Verification Report (2026-02-24)
- **Boundary Root Thin MCP**: [x] OK. [`src/code_rag/mcp/gateway.py`](../../src/code_rag/mcp/gateway.py) подтвержден.
- **HSM Manifests & Registry**: [x] OK. [`hsm.yaml`](../../hsm.yaml) и [`hsm-registry/services/`](../../hsm-registry/services/) согласованы.
- **GAP-1 (Stale Paths)**: [-] Найдено: [`plans/stage-3-planning-input.md`](../../plans/stage-3-planning-input.md), [`plans/t01-t03-code-implementation-plan.md`](../../plans/t01-t03-code-implementation-plan.md) используют старые пути `docs/contracts/`.
- **GAP-2 (Backend README)**: [-] Найдено: [`services/code-rag-backend/README.md`](../../services/code-rag-backend/README.md) ссылается на `src/code_rag/core` вместо `src/code_rag_backend/core`.
- **GAP-3 (Backend Test Docs)**: [-] Найдено: [`services/code-rag-backend/docs/testing/test-map.md`](../../services/code-rag-backend/docs/testing/test-map.md) ссылается на `docs/architecture/stage-2-specification.md` через некорректный относительный путь.
- **GAP-4 (Git Context)**: [-] Найдено: [`.kilocode/rules/memory-bank/gitContext.md`](../../.kilocode/rules/memory-bank/gitContext.md) содержит несуществующий `./hsm/.kilocode/`.
- **GAP-5 (Frontend Skeleton)**: [-] Найдено: [`services/code-rag-frontend/README.md`](../../services/code-rag-frontend/README.md) декларирует `src/` и `docs/`, которых нет в ФС.

### Remediation Plan
1. Обновить пути в `plans/*.md` и `docs/architecture.md` на актуальные (с учетом `services/code-rag-backend/`).
2. Исправить пути к исходникам в `services/code-rag-backend/README.md`.
3. Скорректировать кросс-репозиторные ссылки в `services/code-rag-backend/docs/testing/**`.
4. Актуализировать `gitContext.md`.
5. Создать базовые директории `src/` и `docs/` в `services/code-rag-frontend/`.
