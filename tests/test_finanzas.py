
from fastapi.testclient import TestClient
from app.main import app
from app.services.calculadora import analizar_finanzas

client = TestClient(app)


def test_analisis_financiero():
    resultado = analizar_finanzas(2000000, 1200000)

    assert resultado["balance"] == 800000
    assert resultado["porcentaje_gastos"] == 60
    assert resultado["estado"] == "Estable"


def test_pagina_principal():
    respuesta = client.get("/")

    assert respuesta.status_code == 200
    assert "FinanSmart" in respuesta.text


def test_resultado_del_analisis():
    respuesta = client.post(
        "/analizar",
        data={
            "ingresos": 2000000,
            "gastos": 1200000
        }
    )

    assert respuesta.status_code == 200
    assert "Resumen financiero" in respuesta.text
    assert "Estable" in respuesta.text


def test_rechazar_ingresos_negativos():
    respuesta = client.post(
        "/analizar",
        data={
            "ingresos": -100000,
            "gastos": 50000
        }
    )

    assert respuesta.status_code == 400
    assert "Los ingresos no pueden ser negativos." in respuesta.text


def test_rechazar_gastos_negativos():
    respuesta = client.post(
        "/analizar",
        data={
            "ingresos": 1000000,
            "gastos": -50000
        }
    )

    assert respuesta.status_code == 400
    assert "Los gastos no pueden ser negativos." in respuesta.text
