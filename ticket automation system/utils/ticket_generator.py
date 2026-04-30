import uuid
from datetime import datetime

def create_ticket(nombre, problema, prioridad):
    return {
        "id": str(uuid.uuid4())[:8],
        "nombre" : nombre,
        "problema" : problema,
        "prioridad" : prioridad,
        "fecha" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
