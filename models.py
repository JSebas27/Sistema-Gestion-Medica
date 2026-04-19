from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Especialidad(db.Model):
    id_especialidad = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))

class Medico(db.Model):
    id_medico = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    id_especialidad = db.Column(db.Integer, db.ForeignKey('especialidad.id_especialidad'))

class Paciente(db.Model):
    id_paciente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(100))

class Cita(db.Model):
    id_cita = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_medico = db.Column(db.Integer, db.ForeignKey('medico.id_medico'))
    fecha = db.Column(db.String(20))
    hora = db.Column(db.String(10))
    estado = db.Column(db.String(20))

class HistorialClinico(db.Model):
    id_historial = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_cita = db.Column(db.Integer, db.ForeignKey('cita.id_cita'))
    diagnostico = db.Column(db.String(200))
    tratamiento = db.Column(db.String(200))
    notas = db.Column(db.String(300))