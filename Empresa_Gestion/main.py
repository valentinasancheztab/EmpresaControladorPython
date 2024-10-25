from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.routers import router

app = FastAPI() #es la base sobre la cual se construye toda la lógica y funcionalidad de la aplicación web.

# Configuración de CORS
# Permite que la aplicación acepte solicitudes de diferentes dominios.
app.add_middleware(
    CORSMiddleware, # Añade el middleware CORSMiddleware para habilitar CORS.
    allow_origins=["*"], # Permite solicitudes de cualquier dominio.
    allow_credentials=True, # Permite el uso de credenciales (cookies, autenticación, etc.).
    allow_methods=["*"], # Permite todos los métodos HTTP (GET, POST, etc.).
    allow_headers=["*"], # Permite todas las cabeceras HTTP en las solicitudes.
)


app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
