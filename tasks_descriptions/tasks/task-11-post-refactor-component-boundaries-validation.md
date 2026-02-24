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
- [ ] Подтверждено соблюдение repository boundaries для root/backend/frontend.
- [ ] HSM манифесты и реестр проходят проверки без ошибок.
- [ ] Backend validation (минимум `uv run pytest`) воспроизводима из component repo.
- [ ] Документация и task-ссылки не содержат устаревших root-путей для backend-артефактов.
- [ ] Git context и ownership для nested repos актуализированы.
- [ ] Подготовлен краткий отчет по результатам проверки и дальнейшим действиям.

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
- Current State: planned
- Next Step: выполнить audit по boundary/HSM/docs/tasks и собрать verification report
- Blockers: none
- Contract Changes: none
- Verification: создать checklist-отчет по пунктам DoD в рамках этой задачи
