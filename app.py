from flask import Flask, request, jsonify
import sqlite3

from models import db, Paciente, Medico, Cita
from config import Config

from db_nosql import coleccion

app = Flask(__name__)
app.config.from_object(Config)


# INICIALIZAR SQLALCHEMY

with app.app_context():
    db.init_app(app)
    db.create_all()


# CONEXION SQLITE (CRUD MANUAL)

def get_db():
    return sqlite3.connect("clinica.db")


# PACIENTES SQLALCHEMY

@app.route("/pacientes", methods=["GET"])
def get_pacientes():
    pacientes = Paciente.query.all()

    return jsonify([
        {
            "id": p.id_paciente,
            "nombre": p.nombre,
            "telefono": p.telefono,
            "correo": p.correo
        }
        for p in pacientes
    ])

@app.route("/pacientes", methods=["POST"])
def crear_paciente_sql():
    data = request.json

    nuevo = Paciente(
        nombre=data["nombre"],
        telefono=data["telefono"],
        correo=data["correo"]
    )

    db.session.add(nuevo)
    db.session.commit()

    return {"mensaje": "Paciente creado (SQLAlchemy)"}


# MEDICOS

@app.route("/medicos", methods=["GET"])
def get_medicos():
    medicos = Medico.query.all()

    return jsonify([
        {"id": m.id_medico, "nombre": m.nombre}
        for m in medicos
    ])

@app.route("/medicos", methods=["POST"])
def crear_medico():
    data = request.json

    nuevo = Medico(
        nombre=data["nombre"],
        id_especialidad=1
    )

    db.session.add(nuevo)
    db.session.commit()

    return {"mensaje": "Médico creado"}


# CITAS

@app.route("/citas", methods=["POST"])
def crear_cita():
    data = request.json

    nueva = Cita(
        id_paciente=data["id_paciente"],
        id_medico=data["id_medico"],
        fecha=data["fecha"],
        hora=data["hora"],
        estado="Pendiente"
    )

    db.session.add(nueva)
    db.session.commit()

    return {"mensaje": "Cita creada"}

@app.route("/citas/<int:id>", methods=["GET"])
def get_cita(id):
    cita = Cita.query.get(id)

    if not cita:
        return {"error": "No encontrada"}, 404

    return {
        "id": cita.id_cita,
        "fecha": cita.fecha,
        "hora": cita.hora,
        "estado": cita.estado
    }


# MONGO CRUD

@app.route("/mongo/paciente", methods=["POST"])
def crear_mongo():
    data = request.json
    coleccion.insert_one(data)
    return {"mensaje": "Guardado en MongoDB"}

@app.route("/mongo/test")
def test_mongo():
    return {"mensaje": "Mongo conectado"}


# HIBRIDO SQL + MONGO

@app.route("/paciente/completo/<int:id>")
def paciente_completo(id):

    # SQL
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE id=?", (id,))
    sql_data = cursor.fetchone()
    conn.close()

    # Mongo
    nosql_data = coleccion.find_one(
        {"paciente_id": id},
        {"_id": 0}
    )

    return jsonify({
        "sql": sql_data,
        "nosql": nosql_data
    })


# CRUD COMPLETO SQL + MONGO

@app.route("/paciente", methods=["POST"])
def crear():
    data = request.json

    # SQL
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pacientes (id, nombre, edad) VALUES (?, ?, ?)",
        (data["id"], data["nombre"], data["edad"])
    )
    conn.commit()
    conn.close()

    # MONGO
    coleccion.insert_one({
        "paciente_id": data["id"],
        "informacion_medica": data["info_medica"]
    })

    return {"mensaje": "Paciente creado"}

@app.route("/paciente/<int:id>", methods=["GET"])
def leer(id):

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE id=?", (id,))
    sql_data = cursor.fetchone()
    conn.close()

    nosql_data = coleccion.find_one({"paciente_id": id})

    return jsonify({
        "sql": sql_data,
        "nosql": nosql_data
    })

@app.route("/paciente/<int:id>", methods=["PUT"])
def actualizar(id):
    data = request.json

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE pacientes SET nombre=?, edad=? WHERE id=?",
        (data["nombre"], data["edad"], id)
    )
    conn.commit()
    conn.close()

    coleccion.update_one(
        {"paciente_id": id},
        {"$set": {"informacion_medica": data["info_medica"]}}
    )

    return {"mensaje": "Actualizado"}

@app.route("/paciente/<int:id>", methods=["DELETE"])
def eliminar(id):

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id=?", (id,))
    conn.commit()
    conn.close()

    coleccion.delete_one({"paciente_id": id})

    return {"mensaje": "Eliminado"}


if __name__ == "__main__":
    app.run(debug=True)