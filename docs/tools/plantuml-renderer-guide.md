# Инструкция по использованию PlantUML Docker Renderer

[PlantUML Docker Renderer](https://github.com/VLMHyperBenchTeam/plantuml-docker-renderer) — это инструмент для автоматического пакетного рендеринга диаграмм PlantUML в форматы SVG и PNG.

## Основные возможности
*   **Автоматический поиск**: Сканирует указанную директорию на наличие файлов `.puml`.
*   **Двойной экспорт**: Генерирует сразу и `.svg`, и `.png` для каждого исходника.
*   **Рекурсивная обработка**: Поддерживает вложенные папки.
*   **Изоляция**: Работает внутри Docker-контейнера, не требуя установки Java или Graphviz на хост-машину.

## Как запустить рендеринг

### 1. Подготовка
Убедитесь, что у вас установлен Docker и вы авторизованы в GitHub Container Registry (GHCR).

```bash
# Авторизация через GitHub CLI
gh auth login
gh auth setup-git
```

### 2. Запуск (Linux/macOS)
Запустите контейнер, смонтировав папку с документацией:

```bash
docker run --rm \
  -v "$(pwd)/docs:/docs" \
  ghcr.io/vlmhyperbenchteam/plantuml-renderer
```

### 3. Запуск (Windows PowerShell)
```powershell
docker run --rm `
  -v "${PWD}/docs:/docs" `
  ghcr.io/vlmhyperbenchteam/plantuml-renderer
```

## Работа в нашем проекте
Согласно [ADR-001](../adr/001-diagrams-storage-and-rendering.md), мы используем следующую схему:
1.  Вы вносите изменения в `.puml` файл (например, в `docs/diagrams/architecture/component-diagram.puml`).
2.  Запускаете команду рендеринга (см. выше).
3.  Рендерер создаст/обновит файл `component-diagram.png` в той же папке.
4.  Вы проверяете результат и коммитите оба файла.

## Устранение проблем
*   **Файлы не обновляются**: Проверьте права доступа к папке `docs`.
*   **Ошибка рендеринга**: Убедитесь, что файл начинается с `@startuml` и заканчивается `@enduml`.