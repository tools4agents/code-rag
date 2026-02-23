# Contracts: code-rag

Этот каталог содержит Contract-First артефакты `code-rag`.

Stage 2 описывает контракты текстом и примерами в [`docs/architecture/stage-2-specification.md`](docs/architecture/stage-2-specification.md). Stage 3 должен зафиксировать **формальные схемы** (JSON Schema или эквивалент), чтобы:

- L2 Contract tests могли валидировать payloads;
- backend, UI и интеграции (например `code-atlas`) могли развиваться независимо.

## Версионирование

- Директория версии (`v1/`, `v2/`, ...) соответствует `contract_version` из push-first контракта.
- Breaking change любой схемы -> новая директория версии.
- Non-breaking change -> расширение схемы внутри текущей директории.

## v1 (целевой набор схем)

В версии `v1/` должны появиться схемы:

- `push_batch.schema.json` (см. [`docs/architecture/stage-2-specification.md:92`](docs/architecture/stage-2-specification.md:92))
- `push_item.schema.json` (см. [`docs/architecture/stage-2-specification.md:104`](docs/architecture/stage-2-specification.md:104))
- `push_acceptance.schema.json` (см. [`docs/architecture/stage-2-specification.md:130`](docs/architecture/stage-2-specification.md:130))
- `reconcile_request.schema.json` (см. [`docs/architecture/stage-2-specification.md:180`](docs/architecture/stage-2-specification.md:180))
- `reconcile_response.schema.json` (см. [`docs/architecture/stage-2-specification.md:204`](docs/architecture/stage-2-specification.md:204))
- `query_request.schema.json` (см. [`docs/architecture/stage-2-specification.md:220`](docs/architecture/stage-2-specification.md:220))
- `query_response.schema.json` (см. [`docs/architecture/stage-2-specification.md:229`](docs/architecture/stage-2-specification.md:229))
- `error_envelope.schema.json` (см. [`docs/architecture/stage-2-specification.md:236`](docs/architecture/stage-2-specification.md:236))
- `provider_capabilities.schema.json` (см. требования к провайдерам в [`docs/architecture/stage-2-specification.md:70`](docs/architecture/stage-2-specification.md:70))

## Web API для Web UI

Web UI требования перечислены в [`docs/architecture/stage-2-specification.md:295`](docs/architecture/stage-2-specification.md:295).

Рекомендуемый формат контракта для UI<->backend: OpenAPI (файл будет добавлен на Stage 3, например `openapi.yaml`).

