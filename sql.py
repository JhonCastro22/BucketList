import sqlite3

conn = sqlite3.connect("mi_base.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS actividades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        actividad TEXT NOT NULL,
        fecha TEXT NOT NULL,
        cumplido INTEGER NOT NULL DEFAULT 0  -- 0 = no cumplido, 1 = cumplido
    )
''')
conn.commit()
conn.close()
