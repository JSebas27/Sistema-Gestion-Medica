import sqlite3

conn = sqlite3.connect("clinica.db")
cursor = conn.cursor()

cursor.execute("""
INSERT OR REPLACE INTO pacientes (id, nombre, edad)
VALUES (1, 'Juan', 30)
""")

conn.commit()
conn.close()