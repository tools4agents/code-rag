# Задача T10: Python code style tooling setup

## Контекст
- В проектных правилах зафиксировано требование к Python docstrings: Google Style with types ([`.kilocode/rules/project.md`](.kilocode/rules/project.md)).
- На текущем этапе в репозитории нет единого enforce-контура code style для Python-кода (format/lint/type-check/docstring checks).
- Нужна отдельная задача на внедрение и интеграцию инструментов, чтобы правило применялось автоматически и воспроизводимо.

## Architecture Context References
- [x] Принципы инженерной дисциплины и единых контрактов качества: [`docs/architecture.md`](docs/architecture.md)
- [x] Сервисная граница и quality context Stage 2: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259)

## Specification References
- [x] Локальные правила проекта (docstrings policy): [`.kilocode/rules/project.md`](.kilocode/rules/project.md:21)
- [x] Текущая конфигурация Python-проекта: [`pyproject.toml`](pyproject.toml)

## Test Design References
- [x] Канонический Test Design L1-L4: [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md:259)
- [x] Релевантный акцент для задачи: L1/L2 quality gates и reproducible checks в CI

## Цель
- Внедрить единый набор инструментов style quality для Python-кода и docstrings, с локальным запуском и CI-совместимым пайплайном.

## Шаги реализации
- [ ] Утвердить целевой toolchain: `ruff` (lint + import order + pydocstyle rules), `black` (format), `mypy` (type checks), `pytest` (quality gate smoke).
- [ ] Добавить конфигурацию инструментов в [`pyproject.toml`](pyproject.toml) с правилами для Google-style docstrings и typed sections.
- [ ] Добавить make/uv команды (или scripts) для единообразного запуска: format, lint, typecheck, test.
- [ ] Настроить pre-commit hooks для локального авто-контроля качества.
- [ ] Добавить CI job для обязательного прогона quality gates на PR.
- [ ] Обновить документацию разработчика с инструкцией запуска и troubleshooting.

## Definition of Done
- [ ] В репозитории есть единая конфигурация style-инструментов для Python.
- [ ] Докстринги Google Style with types проверяются автоматически линтером.
- [ ] Есть воспроизводимые команды локального запуска quality gates.
- [ ] CI блокирует merge при нарушении code style/type/docstring правил.
- [ ] Документация содержит актуальные инструкции для команды.

## Execution Status
- Current State: planned
- Next Step: согласовать целевой toolchain и конкретные правила docstring-lint
- Blockers: none
- Contract Changes: none
- Verification: создан task artifact (`tasks_descriptions/tasks/task-10-python-code-style-tooling.md`)
