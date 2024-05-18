# Pasos para hacer una app de dash y hacer el deploy en render
**Instalar**
~~~
pip install dash-tools

dashtools gui
~~~
**Estructura de carpetas**
~~~
Carpeta del proyecto/
├── data/
│   └── datos.csv (o lo que sea)
├── src/
│   └── app.py
├── requirements.txt
└── render.yaml
~~~

**Requisitos**
* Que exitan los archivos:
  - src/app.py
  - render.yaml (Se puede generar automáticamente con el Dash Tools, indicando previamente el Render App Name)
  - requirements.txt (Se puede generar automáticamente con el Dash Tools )
* El proyecto debe estar Pushed to GitHub Public repository
* Debe estar la línea: `server = app.server` en el archivo src/app.py (después de `app = Dash(__name__)` )
