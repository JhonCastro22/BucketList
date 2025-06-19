from flask import Flask, render_template, request, jsonify
import pymysql

# Conexión a la base de datos MySQL de PythonAnywhere
conn_params = {
    "host": "JhonCastro.mysql.pythonanywhere-services.com",
    "user": "JhonCastro",
    "password": "Jhoncv2206git_",
    "database": "JhonCastro$default"
}

app = Flask(__name__)

def get_connection():
    return pymysql.connect(**conn_params)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/actividades", methods=["GET"])
def obtener_actividades():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, actividad, fecha, cumplido FROM actividades")
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(datos)

@app.route("/agregar", methods=["POST"])
def agregar():
    actividad = request.form["actividad"]
    fecha = request.form["fecha"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO actividades (actividad, fecha, cumplido) VALUES (%s, %s, %s)", (actividad, fecha, 0))
    conn.commit()
    cursor.close()
    conn.close()
    return "ok", 200

@app.route("/actualizar", methods=["POST"])
def actualizar_realizado():
    id_actividad = request.form["id"]
    realizado = request.form["realizado"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE actividades SET cumplido = %s WHERE id = %s", (realizado, id_actividad))
    conn.commit()
    cursor.close()
    conn.close()
    return "ok", 200

if __name__ == "__main__":
    app.run(debug=True)
