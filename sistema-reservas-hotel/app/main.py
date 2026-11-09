from fastapi import FastAPI

from app.routes.quartos import router as quartos_router
from app.routes.hospedes import router as hospedes_router
from app.routes.reservas import router as reservas_router
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Sistema de Reservas de Hotel",
    description="API para gerenciamento de reservas de hotel.",
    version="1.0.0"
)

templates = Jinja2Templates(directory="app/templates")

app.include_router(quartos_router)
app.include_router(hospedes_router)
app.include_router(reservas_router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/pagina-hospedes")
def pagina_hospedes(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="hospedes.html"
    )


@app.get("/pagina-reservas")
def pagina_reservas(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="reservas.html"
    )
