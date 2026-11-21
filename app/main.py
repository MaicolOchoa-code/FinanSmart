
from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.services.calculadora import analizar_finanzas


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="FinanSmart",
    description="Analizador de ingresos y gastos personales",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/analizar")
async def analizar(
    request: Request,
    ingresos: float = Form(...),
    gastos: float = Form(...)
):
    try:
        resultado = analizar_finanzas(ingresos, gastos)

        return templates.TemplateResponse(
            request=request,
            name="resultado.html",
            context={
                "request": request,
                "resultado": resultado
            }
        )

    except ValueError as error:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "request": request,
                "error": str(error)
            },
            status_code=400
        )
