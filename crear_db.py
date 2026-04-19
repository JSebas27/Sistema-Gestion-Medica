import sqlite3

conn = sqlite3.connect("clinica.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
""")

conn.commit()
conn.close()