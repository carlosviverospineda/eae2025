from api.models.db import connection_db
from api.schemas.cliente import ClienteResponse


def get_clientes():

    with connection_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("select c.id , v.fecha_venta , v.total  "
                           "from clientes as c "
                           "inner join ventas v on c.id = v.cliente_id ;")
            clientes = cursor.fetchall()
    return [
        {"id_cliente": c[0], "fecha_venta": c[1], "total_venta": c[2]} for c in clientes
    ]

