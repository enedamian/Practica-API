# simulamos datos de una base de datos
lista_productos = [{"id": 1, "nombre": "laptop", "precio": 800, "cantidad": 4, "fecha_actualizacion": "2023-09-01"},
                    {"id": 2, "nombre": "mouse", "precio": 40, "cantidad": 10, "fecha_actualizacion": "2023-10-21"},
                    {"id": 3, "nombre": "monitor", "precio": 400, "cantidad": 3, "fecha_actualizacion": "2023-09-29"},
                    {"id": 4, "nombre": "teclado", "precio": 80, "cantidad": 5, "fecha_actualizacion": "2023-10-01"},
                    {"id": 5, "nombre": "parlantes", "precio": 100, "cantidad": 2, "fecha_actualizacion": "2023-10-25"},
                    {"id": 6, "nombre": "impresora", "precio": 200, "cantidad": 1, "fecha_actualizacion": "2023-09-28"}]

def validar_producto(producto):
    if "nombre" in producto and "precio" in producto and "cantidad" in producto:
        return True
    else:
        return False
