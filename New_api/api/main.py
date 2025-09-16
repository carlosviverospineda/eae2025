from fastapi import FastAPI
from api.routes.cliente_route import router as cliente_router

api = FastAPI()

#@api.get("/")
#def read_root():
#    return {"Hello": "World"}

api.include_router(cliente_router, prefix = "/api", tags = ["Clientes"])
