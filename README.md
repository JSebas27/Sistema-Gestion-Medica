# 🏥 Sistema de Gestión Médica

## 📌 Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión médica que permite administrar pacientes, médicos y citas, integrando una arquitectura híbrida con bases de datos SQL y NoSQL.

El sistema implementa **persistencia políglota**, utilizando:

* Base de datos relacional (SQLite) para datos estructurados.
* Base de datos NoSQL (MongoDB) para información médica flexible.

---

## 🎯 Objetivo

Escalar la aplicación mediante el uso de una base de datos NoSQL para gestionar información no estructurada, mejorando la flexibilidad y el rendimiento del sistema.

---

## ⚙️ Tecnologías Utilizadas

* Python
* Flask
* SQLite
* MongoDB
* PyMongo
* SQLAlchemy

---

## 🧠 Arquitectura del Sistema

El sistema sigue una arquitectura híbrida:

* **SQL (SQLite):**

  * Pacientes
  * Médicos
  * Citas

* **NoSQL (MongoDB):**

  * Información médica del paciente
  * Alergias
  * Hábitos
  * Medicamentos

Ambas bases de datos se integran mediante el campo:

```
id_paciente
```

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

```
git clone https://github.com/JSebas27/Sistema-Gestion-Medica.git
cd Sistema-Gestion-Medica
```

---

### 2. Crear entorno virtual

```
python -m venv .venv
```

Activar entorno:

**Windows:**

```
.venv\\Scripts\\activate
```

---

### 3. Instalar dependencias

```
pip install flask flask_sqlalchemy pymongo
```

---

### 4. Ejecutar MongoDB

Asegúrate de que MongoDB esté corriendo:

```
mongosh
```

---

### 5. Ejecutar la aplicación

```
python app.py
```

---

## 🔥 Endpoint Principal (Integración SQL + NoSQL)

### 📍 GET /perfil_paciente/<id>

Este endpoint implementa persistencia políglota combinando:

* Datos estructurados desde SQL
* Datos dinámicos desde MongoDB

---

## 🧪 Ejemplo de uso

### Request:

```
http://127.0.0.1:5000/perfil_paciente/1
```

### Response:

```json
{
  "id": 1,
  "nombre": "Juan Perez",
  "correo": "juan@email.com",
  "telefono": "123456789",
  "alergias": ["Polen"],
  "habitos": {
    "fuma": false
  },
  "medicamentos": [
    {
      "nombre": "Ibuprofeno",
      "dosis": "400 mg"
    }
  ]
}
```

---

## 🧩 Persistencia Políglota

El sistema implementa una integración entre dos modelos de bases de datos:

* **SQL:** garantiza consistencia y estructura
* **NoSQL:** permite flexibilidad y escalabilidad

Esto permite combinar lo mejor de ambos enfoques en una sola aplicación.

---

## 📸 Evidencia de Ejecución

El endpoint fue probado correctamente mostrando la integración entre SQL y MongoDB, devolviendo un JSON con información combinada.

*(Aquí puedes agregar una captura de pantalla si el profesor lo solicita)*

---

## 📌 Conclusión

El sistema cumple con los requisitos de escalabilidad mediante el uso de NoSQL, logrando una solución eficiente, flexible y preparada para manejar datos médicos complejos.

---

## 👨‍💻 Autor(es)

* José Romo
* Nicolás García

---
