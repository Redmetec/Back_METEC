from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.calcular_flujo import calcular_flujo_fotovoltaico
from pydantic import BaseModel


app = FastAPI(
    title="API Modelo Financiero FV",
    description="API para calcular flujo de caja de proyectos fotovoltaicos",
    version="1.0.0",
)

# Permitir llamadas desde el frontend (React en Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ en producción mejor poner tu dominio de Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataInput(BaseModel):
    generacion_anual_kwh: float
    porcentaje_autoconsumo: float
    consumo_anual_usuario: float
    precio_compra_kwh: float
    crecimiento_energia: float
    precio_bolsa: float
    crecimiento_bolsa: float
    componente_comercializacion: float
    capex: float
    opex_anual: float
    horizonte_anios: int
    tasa_descuento: float
    anios_deduccion_renta: int
    usar_leasing: bool = False
    tasa_leasing: float = 0.0
    plazo_leasing: int = 0

@app.get("/")
async def root():
    return {"status": "API funcionando 🚀"}

@app.post("/calcular")
async def calcular(request: Request):
    data = await request.json()
    resultado = calcular_flujo_fotovoltaico(data)
    return resultado
