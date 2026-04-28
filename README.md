# CV Project

Небольшой проект резюме на Flask с мультиязычной версией и статической сборкой для GitHub Pages.

## Что делает проект

- `app.py` запускает локальный просмотр резюме через Flask.
- `build_static.py` собирает готовую статическую версию в папку `docs/`.
- `compile_translations.py` пересобирает переводы из `.po` в `.mo`.
- `templates/` содержит HTML-шаблон резюме.
- `static/` содержит стили и фотографию.
- `translations/` содержит тексты для разных языков.

## Основные команды

Локальный запуск:

```powershell
cd C:\Users\HP\PycharmProjects\CV
.\.venv\Scripts\python.exe app.py
```

Сборка статической версии для GitHub Pages:

```powershell
cd C:\Users\HP\PycharmProjects\CV
.\.venv\Scripts\python.exe build_static.py
```

Перекомпиляция переводов после правки `.po` файлов:

```powershell
cd C:\Users\HP\PycharmProjects\CV
.\.venv\Scripts\python.exe compile_translations.py
```

## Как обновлять резюме

1. Измени шаблон, стили или переводы.
2. Если менялись `.po` файлы, запусти `compile_translations.py`.
3. Запусти `build_static.py`.
4. Загрузи изменения в GitHub, если сайт опубликован через GitHub Pages.
