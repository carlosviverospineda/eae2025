from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ClienteBase(BaseModel):
    nombre:str
    apellido: str
    email: EmailStr
    telefono: Optional[str]
    direccion: Optional[str]

class ClienteResponse(ClienteBase):
    id: int

# Modelo para la respuesta de ventas por cliente
class ClienteVentaResponse(BaseModel):
    id_cliente: int
    fecha_venta: datetime
    total_venta: float
