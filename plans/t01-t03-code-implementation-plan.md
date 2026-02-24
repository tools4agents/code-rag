# План реализации T01 → T02 → T03 (Code mode)

## Принятые архитектурные решения
- Порядок выполнения: T01 → T02 → T03.
- Операция `DELETE /projects/{project_id}` остается в контракте и включается в scope T03.
- Policy по docstrings: Google Style with types в локальных правилах.

## T01 — Contract-First пакет v1

### Что уже зафиксировано
- Обновлен provider capabilities контракт: `supports_dimensions`, `supports_instruction`, `max_context_tokens`, `recommended_query_instruction`.
- Уточнен `README` контрактов по версии `v1` и policy совместимости.
- Синхронизирована матрица L2-кейсов для provider capabilities.

### Что реализовать в Code mode
1. Добавить L2 schema tests для всех схем `services/code-rag-backend/docs/contracts/v1/`:
   - positive/negative cases для push/reconcile/query/error/provider capabilities;
   - qwen3-embedding vs bge-m3 кейсы.
2. Добавить фикстуры payloads (валидные и невалидные).
3. Добавить воспроизводимый запуск в тестовом контуре.

### Артефакты
- `services/code-rag-backend/tests/contracts/test_v1_schemas.py`
- `services/code-rag-backend/tests/contracts/fixtures/*.json`

---

## T02 — Web UI OpenAPI contract

### Что уже зафиксировано
- В embedder settings добавлены model-specific поля: `instruction`, `dimensions`, `truncate`, `provider_options`.
- Добавлена модель capabilities для embedder catalog.

### Что реализовать в Code mode
1. Валидация OpenAPI спецификации линтером/валидатором.
2. L2 checks консистентности ошибок:
   - shape `ErrorEnvelope` в OpenAPI не противоречит `v1/error_envelope.schema.json`.
3. Контрактные проверки по обязательным operations:
   - Projects: list/create/details/update/delete;
   - Indexing: start/status/stop;
   - Catalogs: chunkers/embedders.

### Артефакты
- `services/code-rag-backend/tests/contracts/test_openapi_contract.py`

---

## T03 — Backend Project Registry (CRUD + delete)

### Что уже зафиксировано
- Есть доменная заготовка `ProjectRegistry` с create/list/get/update и `RegistryError`.
- Scope задачи расширен до полного CRUD, включая delete.

### Что реализовать в Code mode
1. Добавить `delete_project` в core-модель.
2. Проверить стабильность error envelope mapping через `RegistryError.to_error_envelope()`.
3. Добавить unit tests на registry logic:
   - create/list/get/update/delete happy path;
   - duplicate path;
   - duplicate display name;
   - invalid path;
   - not found для get/update/delete.
4. Согласовать формат ответов с OpenAPI `Project`/`ProjectList`.

### Артефакты
- `services/code-rag-backend/tests/unit/test_project_registry.py`
- при необходимости: update `services/code-rag-backend/src/code_rag_backend/core/project_registry.py`

---

## Проверки и критерии приемки
1. Все L2 schema tests и OpenAPI tests проходят.
2. Unit tests для registry проходят.
3. Контрактная консистентность между `services/code-rag-backend/docs/contracts/v1/*.schema.json` и `services/code-rag-backend/docs/contracts/web-ui.openapi.yaml` подтверждена тестами.
4. Изменения не нарушают DDD границы: core отдельно от интерфейсного слоя.

## Команды прогона (Code mode)
- `cd services/code-rag-backend && uv run pytest tests/contracts`
- `cd services/code-rag-backend && uv run pytest tests/unit`
- `cd services/code-rag-backend && uv run pytest`
