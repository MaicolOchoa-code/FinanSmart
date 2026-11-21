
# FinanSmart

## Descripción

FinanSmart es una aplicación web desarrollada con Python que permite analizar las finanzas personales mediante el registro de ingresos y gastos mensuales.

Su propósito es ayudar al usuario a conocer su balance financiero, identificar cuánto dinero está utilizando y recibir recomendaciones para mejorar el manejo de sus recursos.

## Objetivo

Desarrollar una herramienta sencilla que facilite el análisis de las finanzas personales y promueva mejores hábitos de ahorro.

## Tecnologías utilizadas

- Python
- FastAPI
- Jinja2
- HTML5
- CSS3
- Pytest
- Uvicorn

## Funcionalidades

- Registro de ingresos mensuales.
- Registro de gastos mensuales.
- Cálculo del balance disponible.
- Cálculo del porcentaje de gastos.
- Clasificación del estado financiero.
- Recomendaciones según los resultados.
- Validación de valores negativos.
- Interfaz moderna con diseño oscuro.

## Estructura del proyecto

FinanSmart/
│
├── app/
│   ├── main.py
│   ├── services/
│   │   └── calculadora.py
│   ├── templates/
│   │   ├── index.html
│   │   └── resultado.html
│   └── static/
│       └── styles.css
│
├── tests/
│   └── test_finanzas.py
│
├── evidencias/
├── requirements.txt
├── README.md
└── .gitignore

## Instalación

1. Clonar el repositorio.
2. Crear el entorno virtual:

   python -m venv venv

3. Activar el entorno virtual en Windows:

   .\venv\Scripts\Activate.ps1

4. Instalar las dependencias:

   pip install -r requirements.txt

## Ejecución

Ejecutar el siguiente comando:

uvicorn app.main:app --reload

Abrir en el navegador:

http://127.0.0.1:8000

## Pruebas automatizadas

Para ejecutar las pruebas:

python -m pytest -v

El proyecto cuenta con cinco pruebas automatizadas que verifican:

- El análisis financiero.
- La carga de la página principal.
- La generación de resultados.
- El rechazo de ingresos negativos.
- El rechazo de gastos negativos.

## Rutas principales

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | / | Página principal |
| POST | /analizar | Procesamiento del análisis financiero |

## Autor

Proyecto académico desarrollado para la asignatura de Desarrollo de Aplicaciones Web.
