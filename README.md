# Sistema Web de Clínica Dental con Django

## Integrantes

- Velasquez Puma Brigitte Karolay
- Ticona Nina Valeria Abigai
- Lerma Ccopa Jhonatan Javier

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación web orientada a la administración de una clínica dental utilizando el framework Django.

La aplicación permite gestionar información relacionada con pacientes, administración de datos clínicos y operaciones internas mediante el panel administrativo integrado de Django.

El sistema fue desarrollado utilizando:

- Python
- Django
- SQLite/PostgreSQL
- Django Admin
- Entorno virtual (`venv`)

---

# Objetivos del proyecto

- Implementar un entorno de desarrollo aislado con Python.
- Utilizar Django como framework principal.
- Administrar información mediante modelos ORM.
- Utilizar migraciones para la construcción de la base de datos.
- Aprovechar el sistema Auto CRUD integrado en Django Admin.
- Centralizar la administración de la clínica dental en una interfaz web.

---

# Estructura general del proyecto

```text
MyDjangoProject/
│
├── manage.py
├── db.sqlite3
├── MyDjangoProject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── MyWebApps/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
└── templates/
```

---

# Requisitos previos

Antes de ejecutar el proyecto se recomienda tener instalado:

- Python 3.12 o superior
- pip
- Git
- Entorno virtual de Python

---

# Instalación y ejecución del proyecto

## 1. Clonar el repositorio

```powershell
git clone <URL_DEL_REPOSITORIO>
```

---

## 2. Ingresar al proyecto

```powershell
cd MyDjangoProject
```

---

## 3. Crear el entorno virtual

```powershell
python -m venv my_venv
```

### ¿Qué es un entorno virtual?

Un entorno virtual permite aislar las dependencias de Python utilizadas en el proyecto, evitando conflictos con otras aplicaciones instaladas en el sistema.

---

## 4. Activar el entorno virtual

### PowerShell

```powershell
.\my_venv\Scripts\activate
```

### CMD

```cmd
my_venv\Scripts\activate.bat
```

---

## 5. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### Archivo requirements.txt

Este archivo contiene todas las dependencias necesarias para ejecutar correctamente el proyecto.

---

## 6. Aplicar migraciones

```powershell
python manage.py migrate
```

### ¿Qué son las migraciones?

Las migraciones permiten crear y actualizar automáticamente la estructura de la base de datos a partir de los modelos definidos en Django.

---

## 7. Crear un superusuario

```powershell
python manage.py createsuperuser
```

El sistema solicitará:

- Nombre de usuario
- Correo electrónico
- Contraseña

Este usuario tendrá acceso completo al panel administrativo.

---

## 8. Ejecutar el servidor

```powershell
python manage.py runserver
```

Por defecto, Django iniciará el servidor en:

```text
http://127.0.0.1:8000/
```

---

# Acceso al panel administrativo

Django incluye un sistema administrativo integrado que permite realizar operaciones CRUD automáticamente.

## Ingresar al administrador

Abrir en el navegador:

```text
http://127.0.0.1:8000/admin/
```

Luego iniciar sesión con el superusuario creado anteriormente.

---

# Funcionalidades del Django Admin

Desde el panel administrativo es posible:

- Crear registros
- Editar información
- Eliminar datos
- Gestionar usuarios
- Administrar modelos registrados
- Consultar información almacenada

---

# Modelos de Django

Los modelos representan las tablas de la base de datos mediante clases Python.

Ejemplo:

```python
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
```

---

# Método __str__()

El método `__str__()` redefine la representación textual de un objeto dentro del panel administrativo y consultas ORM.

Esto mejora la legibilidad de los registros mostrados en Django Admin.

---

# Registro de modelos en admin.py

Para que los modelos aparezcan en el administrador deben registrarse:

```python
from django.contrib import admin
from .models import Paciente

admin.site.register(Paciente)
```

---

# Archivo .gitignore

El archivo `.gitignore` evita subir archivos innecesarios al repositorio.

Ejemplo:

```text
my_venv/
__pycache__/
db.sqlite3
```

---

# Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Django | Framework web |
| SQLite/PostgreSQL | Base de datos |
| HTML | Plantillas |
| Git | Control de versiones |

---

# Posibles mejoras futuras

- Sistema de autenticación personalizado
- Gestión de citas médicas
- Historial clínico avanzado
- Integración con PostgreSQL en producción
- Diseño responsivo
- Paneles estadísticos

---

# Conclusión

El proyecto demuestra el uso de Django como framework de desarrollo rápido para aplicaciones web administrativas.

Gracias al sistema ORM y al panel Django Admin, es posible construir operaciones CRUD completas con una cantidad reducida de código, facilitando la administración de la información dentro de la clínica dental.
