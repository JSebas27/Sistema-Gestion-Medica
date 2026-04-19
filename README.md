# 🏥 Sistema de Gestión Médica

API REST desarrollada en Flask para la gestión de pacientes, médicos y citas, integrando bases de datos SQL (SQLite) y NoSQL (MongoDB).

---

## 📌 Descripción del proyecto

Este sistema simula un entorno médico real donde la información se divide según su naturaleza:

- 🟦 SQL (SQLite): datos estructurados como pacientes, médicos y citas.
- 🟢 NoSQL (MongoDB): datos flexibles como alergias, hábitos e información médica adicional.

El objetivo es demostrar la integración de ambos tipos de bases de datos en una sola aplicación funcional.

---

## ⚙️ Tecnologías utilizadas

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite
- MongoDB
- PyMongo

---

## 🧠 Arquitectura del sistema

El sistema trabaja con dos bases de datos independientes:

### 🟦 SQL (SQLite)
Se encarga de almacenar información estructurada:

- Pacientes (nombre, teléfono, correo)
- Médicos
- Citas médicas

Esta información se gestiona mediante SQLAlchemy.

---

### 🟢 NoSQL (MongoDB)
Se encarga de información médica flexible:

- Alergias
- Hábitos (fuma, alcohol)
- Datos médicos adicionales

Cada documento se relaciona con el paciente mediante:
paciente_id


---

## 🔗 Integración SQL + NoSQL

La integración se realiza mediante el **ID del paciente**, permitiendo combinar datos estructurados (SQL) y no estructurados (MongoDB).

---

## ⚙️ Endpoint de integración (PUENTE)
GET /paciente/completo/<id>


### 🔄 Funcionamiento paso a paso:

1. El sistema recibe el ID del paciente.
2. Busca los datos del paciente en SQLite (SQL).
3. Busca la información médica en MongoDB (NoSQL).
4. Combina ambos resultados en una sola respuesta JSON.

---

## 📦 Ejemplo de respuesta

```json
{
  "sql": [1, "Juan Pérez", 30],
  "nosql": {
    "paciente_id": 1,
    "informacion_medica": {
      "alergias": ["Penicilina", "Polen"],
      "habitos": {
        "fuma": false,
        "alcohol": "ocasional"
      }
    }
  }
}

# 🚀 PASO A PASO DEL FUNCIONAMIENTO

## 1️⃣ Inicio del servidor
Se ejecuta la aplicación Flask:

```bash
python app.py

http://127.0.0.1:5000

##2️⃣ Base de datos SQL (SQLite)
📌 Qué hace

Guarda información estructurada como:

Pacientes
Médicos
Citas
📌 Ejemplo de flujo
Se crea un paciente desde el endpoint /pacientes
Se guarda en SQLite usando SQLAlchemy
Los datos quedan almacenados en la tabla pacientes

##3️⃣ Base de datos NoSQL (MongoDB)
📌 Qué hace

Guarda información flexible del paciente como:

Alergias
Hábitos
Información médica adicional
📌 Ejemplo de flujo
Se envía información al endpoint /mongo/paciente
Se guarda en la colección info_paciente
Cada documento se relaciona con un paciente mediante paciente_id

##4️⃣ Relación entre SQL y NoSQL

Ambas bases de datos se conectan mediante:
id del paciente (id_paciente)

##5️⃣ Endpoint puente (INTEGRACIÓN)
📌 Endpoint principal:
GET /paciente/completo/<id>

##Resultado final

El sistema responde con algo como:
{
  "sql": [1, "Juan Pérez", 30],
  "nosql": {
    "paciente_id": 1,
    "informacion_medica": {
      "alergias": ["Penicilina", "Polen"],
      "habitos": {
        "fuma": false,
        "alcohol": "ocasional"
      }
    }
  }
}

## Integrantes

* José Romo
* Nicolás García

---

## Asignatura

Nuevas Tecnologías de Desarrollo

---

## Notas

Este proyecto corresponde a un desarrollo académico enfocado en la implementación de APIs REST y modelado de datos relacional.
