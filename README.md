# 🌍 Aplicación de Coordenadas con Django, Tailwind y Leaflet

## 📄 Descripción del producto
Aplicación web que permite **registrar ubicaciones mediante nombre y coordenadas (latitud/longitud)**, gestionarlas en una tabla y visualizarlas en un **mapa satélite interactivo**.  
Incluye funcionalidades de agregar, feedback visual, formularios y navegación responsiva con Tailwind.

---

## 🎯 Objetivos resueltos
- **Organización de datos geográficos:** centralizar coordenadas en una interfaz clara.  
- **Visualización interactiva:** mostrar cada registro como marcador en un mapa satélite.   
- **Usabilidad:** feedback visual inmediato, responsive design y conexión tabla–mapa.  
- **Portafolio profesional:** demostrar dominio de Django, Tailwind y Leaflet en un proyecto funcional y desplegado.

---

## 🛠️ Tecnologías utilizadas
- **Backend:** Django (Python), Gunicorn.  
- **Frontend:** Tailwind CSS, Leaflet.js.  
- **Base de datos:** SQLite (desarrollo), PostgreSQL (producción).  
- **Despliegue:** Render.  
- **Extras:** Esri World Imagery (capa satélite).

---

## 📸 Funciones
- **Formulario de registro:** campos de nombre, latitud y longitud con validación.  
- **Mapa satélite:** marcadores dinámicos, zoom automático al seleccionar fila.   
- **Navbar responsiva:** navegación con menú hamburguesa en móviles.  

*(Agrega aquí tus capturas de pantalla o GIF mostrando la interacción tabla–mapa)*

---

## 🚀 Instalación y uso

## Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repo-coordenadas.git
   cd tu-repo-coordenadas

## Crear entorno virtual e instalar dependencias:

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
## Migrar base de datos:

```
python manage.py migrate
```

## Ejecutar servidor:

```
python manage.py runserver
```

## Abrir en navegador:

👉 http://127.0.0.1:8000








