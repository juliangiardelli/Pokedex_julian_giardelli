# Pokédex

Aplicación web desarrollada en **Python y Django** como trabajo práctico de **Introducción a la Programación**, en la Universidad Nacional de General Sarmiento (UNGS).

El proyecto consume la API pública de [PokéAPI](https://pokeapi.co/) para obtener información de Pokémon y mostrarla en una galería de tarjetas.

## Funcionalidades implementadas

- Galería de Pokémon obtenidos desde PokéAPI (IDs del 1 al 29).
- Visualización de imagen, nombre, número, tipos, altura, peso y experiencia base.
- Búsqueda por nombre, sin distinguir mayúsculas y minúsculas.
- Filtros por tipo: fuego, agua y planta.
- Tarjetas con bordes diferenciados según el tipo de Pokémon.
- Organización del código mediante una arquitectura por capas.

## Estado del proyecto

La galería, la integración con PokéAPI, la búsqueda y los filtros principales están implementados.

La funcionalidad de **favoritos** quedó parcialmente desarrollada: existen el modelo y parte de la estructura necesaria, pero la gestión completa de favoritos no está finalizada. Por eso, no se presenta como una característica funcional.

## Tecnologías y herramientas

- Python
- Django 4.2.10
- Requests
- SQLite
- Bootstrap 5
- PokéAPI

## Arquitectura

El proyecto está organizado en distintas capas, con responsabilidades diferenciadas:

- **Presentation:** vistas de Django y templates HTML.
- **Services:** lógica de negocio y coordinación de operaciones.
- **Transport:** comunicación con la API externa.
- **Persistence:** acceso a los datos almacenados en SQLite.
- **Utilities:** clases auxiliares y conversión de respuestas de la API a objetos utilizados por la aplicación.

## Instalación y ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/juliangiardelli/Pokedex_julian_giardelli.git
   cd Pokedex_julian_giardelli
   ```

2. Crear y activar un entorno virtual:

   **Windows (PowerShell)**
   ```powershell
   python -m venv venv
   .\\venv\\Scripts\\Activate.ps1
   ```

   **Linux / macOS**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configurar la clave secreta de Django. Se genera localmente y no debe subirse al repositorio.

   **Windows (PowerShell)**
   ```powershell
   $env:DJANGO_SECRET_KEY = python -c "import secrets; print(secrets.token_urlsafe(50))"
   $env:DJANGO_DEBUG = "True"
   ```

   **Linux / macOS**
   ```bash
   export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
   export DJANGO_DEBUG=True
   ```

   Estas variables deben configurarse en la misma terminal desde la que se ejecutará Django. `DJANGO_DEBUG=True` se utiliza únicamente para desarrollo local.

5. Crear las tablas de la base de datos local:

   ```bash
   python manage.py migrate
   ```

6. Iniciar el servidor:

   ```bash
   python manage.py runserver 3000
   ```

7. Abrir [http://localhost:3000](http://localhost:3000) en el navegador.

> La base SQLite local (`db.sqlite3`) no está incluida en el repositorio. Django la crea al ejecutar las migraciones.

## Seguridad

- La clave secreta se obtiene de la variable de entorno `DJANGO_SECRET_KEY`; no se almacena en el código.
- `DEBUG` está desactivado por defecto y se puede activar localmente con `DJANGO_DEBUG=True`.
- La base de datos local y los archivos de entorno están excluidos mediante `.gitignore`.

## Contexto académico

- **Institución:** Universidad Nacional de General Sarmiento (UNGS).
- **Materia:** Introducción a la Programación.
- **Período:** primer semestre de 2025.
- **Resultado:** calificación 10.

## Autor

**Julián Giardelli**

Proyecto realizado de manera individual.
