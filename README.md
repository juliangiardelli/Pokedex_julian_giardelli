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

2. Crear y activar un entorno virtual (recomendado):

   **Windows**
   ```bash
   python -m venv venv
   venv\\Scripts\\activate
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

4. Iniciar el servidor de desarrollo:

   ```bash
   python manage.py runserver 3000
   ```

5. Abrir [http://localhost:3000](http://localhost:3000) en el navegador.

## Contexto académico

- **Institución:** Universidad Nacional de General Sarmiento (UNGS).
- **Materia:** Introducción a la Programación.
- **Período:** primer semestre de 2025.
- **Resultado:** calificación 10.

## Autor

**Julián Giardelli**

Proyecto realizado de manera individual.
