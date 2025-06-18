from flask import Flask, render_template, request, jsonify
import sqlite3
def eliminar():
    conn = sqlite3.connect("mi_base.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM actividades ")
    conn.commit()
    conn.close()
    return "ok", 200

eliminar()