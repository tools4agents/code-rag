# Technical Design: Integrated Knowledge Graph Schema

Этот документ описывает схему единого графа знаний, объединяющего структурный анализ кода (Structural Graph) и архитектурный контекст (Memory Bank).

## 1. Концепция "Мега-Графа"

Граф строится на принципе слоев. Каждый слой добавляет уровень абстракции.

### Слой 1: Физическая структура (Code)
*   **Источники**: Исходный код (.py), манифесты (hpm.yaml).
*   **Генерация**: Автоматическая (AST Parser, HPM Analyzer).
*   **Узлы**: `File`, `Class`, `Function`, `HPM_Package`.

### Слой 2: История изменений (Git)
*   **Источники**: Git log, diffs.
*   **Генерация**: Автоматическая (Git Indexer).
*   **Узлы**: `Commit`, `Author`, `Branch`.

### Слой 3: Архитектурный контекст (Memory Bank)
*   **Источники**: ADR (.md), Plans, Discussions.
*   **Генерация**: Полуавтоматическая (LLM-assisted extraction).
*   **Узлы**: `ADR`, `Requirement`, `Decision`, `Concept`.

## 2. Детальная Схема (Schema Definition)

### 2.1. Узлы (Nodes)

#### Structural Nodes
*   `HPM_Package`: {name, version, type}
*   `Entrypoint`: {name, command}
*   `File`: {path, language, hash}
*   `Class`: {name, qualified_name}
*   `Function`: {name, signature, body_hash}

#### Git Nodes
*   `Commit`: {sha, message, date}
*   `Author`: {name, email}

#### Context Nodes (Memory Bank)
*   `ADR`: {id, title, status, decision_date}
*   `Requirement`: {id, description, priority}
*   `Concept`: {name, description} (e.g., "Async Inference", "HPM Runtime")
*   `Community`: {id, level, title, summary} (Generated high-level summaries)

#### Documentation Nodes
*   `DocPage`: {path, title, url}
*   `DocSection`: {title, content_hash}

### 2.2. Связи (Relationships)

#### Structural Links
*   `(:HPM_Package)-[:DECLARES_DEPENDENCY]->(:HPM_Package)`
*   `(:HPM_Package)-[:HAS_ENTRYPOINT]->(:Entrypoint)`
*   `(:Entrypoint)-[:INVOKES]->(:Function)` (Связь команды запуска с кодом)
*   `(:Function)-[:CALLS]->(:Function)`
*   `(:Class)-[:INHERITS]->(:Class)`

#### Context Links
*   `(:ADR)-[:DECIDED_TO_USE]->(:Concept)`
*   `(:Requirement)-[:IMPLEMENTED_BY]->(:Function|:Class|:HPM_Package)`
*   `(:ADR)-[:AFFECTS]->(:HPM_Package)` (Архитектурное решение влияет на пакет)
*   `(:Commit)-[:LINKED_TO]->(:ADR)` (Коммит реализует решение)

#### Documentation Links
*   `(:DocPage)-[:CONTAINS]->(:DocSection)`
*   `(:DocSection)-[:DESCRIBES]->(:Concept|:HPM_Package|:Class)` (Связь документации с сущностями)

#### Community Links
*   `(:File)-[:BELONGS_TO]->(:Community)`
*   `(:Community)-[:PARENT_OF]->(:Community)` (Иерархия сообществ)

## 3. Стратегия Контекстного Поиска (Context Retrieval)

Как получить нужный контекст из "Мега-Графа" без перегрузки? Используем **Community Detection** и **Traversals**.

### 3.1. Сценарий: "Как работает HPM Runtime?"
1.  **Entry Point**: Поиск узла `Concept {name: "HPM Runtime"}`.
2.  **Expansion (1-hop)**: Находим связанные `ADR` (почему так сделано) и `HPM_Package` (где это лежит).
3.  **Expansion (2-hop)**: От пакета идем к ключевым `Class` и `Function`.
4.  **Result**: Агент получает:
    *   ADR-002 (Динамические зависимости)
    *   Пакет `hyper_package_manager`
    *   Класс `RuntimeManager`
    *   Функцию `bootstrap_env`

### 3.2. Сценарий: "Почему изменился API Wrapper?"
1.  **Entry Point**: Поиск пакета `HPM_Package {name: "api_wrapper"}`.
2.  **Traversal**: Идем по связи `(:HPM_Package)<-[:CHANGED_IN]-(:Commit)`.
3.  **Context**: От `Commit` идем к `ADR` или `Requirement` (`(:Commit)-[:LINKED_TO]->(:ADR)`).
4.  **Result**: "API Wrapper изменился в коммите `abc1234` (feat: async support), который реализует ADR-004".

## 4. Реализация Инструмента (MCP Tool)

Инструмент `query_knowledge_graph` будет поддерживать разные режимы "глубины":

*   `mode="structure"`: Возвращает только код и зависимости (для IDE).
*   `mode="context"`: Возвращает ADR и требования (для планирования).
*   `mode="full"`: Возвращает трассировку от требования до кода (для аудита).

```json
{
  "name": "query_knowledge_graph",
  "arguments": {
    "query": "HPM Runtime",
    "mode": "context",
    "depth": 2
  }
}