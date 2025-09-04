from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.modelo_financiero import calcular_flujo_fotovoltaico

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

@app.get("/")
async def root():
    return {"status": "API funcionando 🚀"}

@app.post("/calcular")
async def calcular(request: Request):
    data = await request.json()
    resultado = calcular_flujo_fotovoltaico(data)
    return resultado
