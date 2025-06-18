from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Obtener actividades desde la base de datos
@app.route("/actividades", methods=["GET"])
def obtener_actividades():
    conn = sqlite3.connect("mi_base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, actividad, fecha, cumplido FROM actividades")
    datos = cursor.fetchall()
    conn.close()
    return jsonify(datos)

# Insertar nueva actividad (por defecto no realizada)
@app.route("/agregar", methods=["POST"])
def agregar():
    actividad = request.form["actividad"]
    fecha = request.form["fecha"]
    conn = sqlite3.connect("mi_base.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO actividades (actividad, fecha, cumplido) VALUES (?, ?, 0)", (actividad, fecha))
    conn.commit()
    conn.close()
    return "ok", 200
@app.route("/actualizar", methods=["POST"])
def actualizar_realizado():
    id_actividad = request.form["id"]
    realizado = request.form["realizado"]

    conn = sqlite3.connect("mi_base.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE actividades SET cumplido = ? WHERE id = ?", (realizado, id_actividad))
    conn.commit()
    conn.close()
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True)

