from flask import Flask, jsonify, request
import datetime
from productos import lista_productos as productos, validar_producto
#creamos una instancia de la clase Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hola!</h1>"



@app.route("/productos", methods=["GET"])
def getProductos():
    return jsonify({"productos":productos}), 200  # 200 es el codigo de exito

@app.route("/productos/<int:id>", methods=["GET"])
def getProducto(id):
    productosEncontrados = [producto for producto in productos if producto["id"] == id]
    if (len(productosEncontrados) > 0):
        return jsonify({"producto": productosEncontrados[0]}), 200 # 200 es el codigo de exito
    return jsonify({"message": "Producto no encontrado"}), 404 # 404 es el codigo de error de "not found"

# guardamos un nuevo producto
@app.route("/productos", methods=["POST"])
def addProducto():
    if validar_producto(request.json):
        nuevoProducto = {
            "id" : productos[-1]["id"] + 1,
            "nombre": request.json["nombre"],
            "precio": request.json["precio"],
            "cantidad": request.json["cantidad"],
            "fecha_actualizacion": datetime.date.today().strftime("%Y-%m-%d") # formato "YYYY-MM-DD" , opcional: %H-%M-%S = HH:MM:SS
        }
        productos.append(nuevoProducto)
        return jsonify({"message": "Producto agregado exitosamente", "productos": productos}), 201 # 201 es el codigo de exito de "created"
    else:
        return jsonify({"message": "Datos del producto incompletos"}), 400 # 400 es el codigo de error de "bad request"


# actualización de producto
@app.route("/productos/<int:id>", methods=["PUT"])
def updateProducto(id):
    if validar_producto(request.json):
        productosEncontrados = [producto for producto in productos if producto["id"] == id]
        if (len(productosEncontrados) > 0):
            productosEncontrados[0]["nombre"] = request.json["nombre"]
            productosEncontrados[0]["precio"] = request.json["precio"]
            productosEncontrados[0]["cantidad"] = request.json["cantidad"]
            productosEncontrados[0]["fecha_actualizacion"] = datetime.date.today().strftime("%Y-%m-%d")
            return jsonify({"message": "Producto actualizado exitosamente", "producto": productosEncontrados[0], "productos": productos}), 200
        else:
            return jsonify({"message": "Producto no encontrado"}), 404
    else:
        return jsonify({"message": "Datos del producto incompletos"}), 400
    


# eliminación de productos:
@app.route("/productos/<int:id>", methods=["DELETE"])
def deleteProducto(id):
    # en el siguiente list comprehension, como no estamos modificando los elementos, la nueva lista se genera como referencia a la lista original
    productosEncontrados = [producto for producto in productos if producto["id"] == id]
    if (len(productosEncontrados) > 0):
        productos.remove(productosEncontrados[0])
        return jsonify({"message": "Producto eliminado exitosamente", "productos": productos}), 200
    else:
        return jsonify({"message": "Producto no encontrado"}), 404


# el siguiente IF nos permite ejecutar la aplicacion solamente si este archivo es ejecutado como archivo principal
# es decir, si este archivo es importado desde otro archivo, el servidor no se va a ejecutar
if __name__=="__main__":
    app.run(debug=True)

# Ejemplos de uso de datetime:

# Fecha actual
hoy = datetime.date.today()

# Fecha de nacimiento
fecha_nacimiento = datetime.date(2000, 9, 30)

# Diferencia entre ambas fechas
diferencia = hoy - fecha_nacimiento

# Diferencia en días
# print(diferencia.days)

# fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

año = fecha_hora_actual.year
mes = fecha_hora_actual.month
día = fecha_hora_actual.day
hora = fecha_hora_actual.hour
minuto = fecha_hora_actual.minute
segundo = fecha_hora_actual.second

# fecha y hora determinados
fecha_y_hora_nacimiento = datetime.datetime(2000, 9, 26, 10, 30, 0)

# convertir string a datetime
fecha_str = "2021-09-30"
fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
    