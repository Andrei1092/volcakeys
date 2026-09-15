# Project: Weather Informer (Desktop App)

A Python desktop weather application built with `pywebview` serving a local HTML/CSS/JS frontend (`wea.html`).

## Structure
- `app.py` - Main Python entrypoint using `pywebview` and `resource_path` handling for PyInstaller bundles.
- `wea.html` - Primary frontend UI asset.
- `style.css`, `script.js` - Styling and client-side logic.
- `app.spec` - PyInstaller spec configuration bundling assets.
- `dist/` - Standalone binary output (`app.exe`).

## Commands
- Run app: `python app.py`
- Build executable: `pyinstaller app.spec` (or `pyinstaller --noconsole --onefile --add-data "wea.html;." app.py`)

## Engineering Principles & Workflow
-  Озвучивай допущения и компромиссы до первой строки кода. Сомневаешься - копай код и задавай вопросы.
-  Хороший код - минимум кода: KISS и YAGNI по умолчанию; DRY и SOLID подключай, когда задача переросла разовый скрипт.
-  Трогай только то, чего требует задача, без попутных правок. Про найденные дыры и техдолг докладывай после, а не чини по ходу.
-  Всегда фиксируй проверяемый критерий готовности и работай до него.
-  Ищи дыры в плане до того, как писать код. Сломалось - чини стратегию, а не реализацию.
