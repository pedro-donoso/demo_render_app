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
   ```

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

## 📌 El problema resuelto
La aplicación aborda la necesidad de **organizar y visualizar coordenadas geográficas** de manera clara e interactiva.  
En muchos contextos (educación, turismo, logística, investigación) los datos de latitud y longitud suelen quedar dispersos en hojas de cálculo o notas poco prácticas.  
El producto resuelve este problema al:
- Centralizar registros en una **tabla gestionable** (agregar nuevos datos, permanencia en BD con Postgresql).  
- Mostrar cada registro como **marcador en un mapa satélite**.  
- Permitir que al seleccionar un registro en la tabla el mapa se centre automáticamente en ese punto con zoom y popup.  
- Ofrecer una interfaz **responsiva y accesible**, con feedback visual inmediato.

---

## 🛠️ Tecnologías utilizadas
- **Backend:** Django (Python).  
- **Frontend:** Tailwind CSS para estilos responsivos y Leaflet.js para mapas interactivos.  
- **Base de datos:** SQLite en desarrollo, PostgreSQL en producción.  
- **Mapa satélite:** Esri World Imagery como capa base.  
- **Servidor:** Gunicorn y despliegue en Render.  

---

## 🚀 Enfoque de desarrollo seguido
Se aplicaron buenas prácticas del ciclo de vida del software:

1. **Planificación:** definición del problema, alcance mínimo viable. 
2. **Diseño:** arquitectura MVC con Django, modelo `Registro`, interfaz con formulario, tabla y mapa satélite.  
3. **Implementación:**    
   - Integración de Leaflet con marcadores dinámicos.  
   - Conexión tabla–mapa mediante eventos de clic.  .  
4. **Pruebas:** verificación de interactividad tabla–mapa y responsividad en distintos dispositivos.  
5. **Despliegue:** configuración de Gunicorn y Render. 








