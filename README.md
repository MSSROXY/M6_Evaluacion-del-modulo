# Gestor de Tareas Django

## Descripción del Proyecto

Este proyecto es una **aplicación web para gestionar tareas personales**, desarrollada con Django. Permite a los usuarios registrarse, iniciar sesión, agregar, visualizar y eliminar tareas. Las tareas se almacenan en un archivo JSON para mantener los datos en memoria de manera persistente, sin necesidad de base de datos para las tareas (solo se usa SQLite para usuarios y sesiones).  

---

---

## Funcionalidades Principales

1. **Autenticación de Usuarios**
   - Registro de nuevos usuarios.
   - Inicio y cierre de sesión.
   - Protección de vistas para que solo usuarios autenticados puedan acceder a sus tareas.

2. **Gestión de Tareas**
   - Crear nuevas tareas mediante un formulario (título y descripción).
   - Visualizar la lista de tareas del usuario autenticado.
   - Ver los detalles de cada tarea individual.
   - Eliminar tareas existentes.
   - Todas las tareas se almacenan en `tareas/tareas.json` y son privadas por usuario.

3. **Interfaz de Usuario**
   - Plantillas diseñadas con **Bootstrap** para responsividad y facilidad de uso.
   - Navegación entre vistas de lista, detalle, agregar, login y registro.

4. **Entorno de Producción**
   - Configuración separada en `settings_produccion.py`:
     - `DEBUG=False`
     - `ALLOWED_HOSTS` configurados
     - Seguridad reforzada con HTTPS, cookies seguras y HSTS
   - Archivos estáticos gestionados mediante `collectstatic`.

---

## Instrucciones de Ejecución

1. Crear un entorno virtual e instalar dependencias:

```bash
python -m venv mi_entorno
source mi_entorno/bin/activate   # Linux/macOS
# mi_entorno\Scripts\activate    # Windows
pip install -r requirements.txt
```

2. Ejecutar migraciones (usuarios y sesiones):
```bash
python manage.py migrate
```

3. (Opcional) Crear un superusuario:
```bash
python manage.py createsuperuser
```

4. Ejecutar servidor en desarrollo:
```bash
python manage.py runserver
```

5. Acceder al proyecto desde el navegador:
```bash
http://127.0.0.1:8000/
```

Las tareas se pueden agregar, visualizar y eliminar, y se guardan en tareas/tareas.json.
