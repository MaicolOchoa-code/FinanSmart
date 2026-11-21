
def analizar_finanzas(ingresos, gastos):
    if ingresos < 0:
        raise ValueError("Los ingresos no pueden ser negativos.")

    if gastos < 0:
        raise ValueError("Los gastos no pueden ser negativos.")

    if ingresos == 0 and gastos == 0:
        raise ValueError("Debes ingresar al menos un valor mayor que cero.")

    balance = ingresos - gastos

    if ingresos > 0:
        porcentaje_gastos = (gastos / ingresos) * 100
    else:
        porcentaje_gastos = 0

    if balance < 0:
        estado = "Déficit"
        recomendacion = "Tus gastos superan tus ingresos. Reduce los gastos."
    elif porcentaje_gastos >= 80:
        estado = "Alerta"
        recomendacion = "Estás gastando gran parte de tus ingresos. Intenta ahorrar."
    elif porcentaje_gastos >= 50:
        estado = "Estable"
        recomendacion = "Tus finanzas están controladas, pero puedes mejorar tu ahorro."
    else:
        estado = "Saludable"
        recomendacion = "¡Muy bien! Tienes una buena capacidad de ahorro."

    return {
        "ingresos": ingresos,
        "gastos": gastos,
        "balance": balance,
        "porcentaje_gastos": round(porcentaje_gastos, 2),
        "estado": estado,
        "recomendacion": recomendacion
    }
