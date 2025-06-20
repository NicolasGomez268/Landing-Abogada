# Instrucciones para Deployment en PythonAnywhere

## Portfolio de la Dra. Patricia Alejandra Martín

### Pasos para subir el proyecto:

#### 1. Subir archivos a PythonAnywhere
- Ve a la pestaña "Files" en tu dashboard de PythonAnywhere
- Navega a `/home/DraPatriciaAlejandraMartin/`
- Sube todos los archivos del proyecto o usa Git para clonar el repositorio

#### 2. Instalar dependencias
- Ve a la pestaña "Consoles" 
- Abre una consola Bash
- Ejecuta:
```bash
cd PortfolioPatri
pip install --user -r requirements.txt
```

#### 3. Configurar archivos estáticos
En la consola Bash, ejecuta:
```bash
cd PortfolioPatri
python manage.py collectstatic --settings=PortfolioPatri.settings_production
```

#### 4. Configurar la aplicación web
- Ve a la pestaña "Web" en tu dashboard
- Si no tienes una web app, crea una nueva seleccionando "Manual configuration" y Python 3.10
- En "Code" section:
  - Source code: `/home/DraPatriciaAlejandraMartin/PortfolioPatri`
  - Working directory: `/home/DraPatriciaAlejandraMartin/PortfolioPatri`
  - WSGI configuration file: `/var/www/drapatriciaalejandramartin_pythonanywhere_com_wsgi.py`

#### 5. Editar el archivo WSGI
- Haz clic en el enlace del WSGI configuration file
- Reemplaza todo el contenido con el contenido del archivo `wsgi_pythonanywhere.py`

#### 6. Configurar archivos estáticos
En la sección "Static files":
- URL: `/static/`
- Directory: `/home/DraPatriciaAlejandraMartin/PortfolioPatri/static_root`

#### 7. Recargar la aplicación
- Haz clic en el botón verde "Reload" en la pestaña Web

### URLs del sitio:
- Principal: https://drapatriciaalejandramartin.pythonanywhere.com
- Con www: https://www.drapatriciaalejandramartin.pythonanywhere.com

### Notas importantes:
- El sitio está configurado para producción (DEBUG = False)
- Los archivos estáticos se sirven desde `/static_root/`
- La base de datos SQLite se mantiene en el directorio del proyecto

### Para futuras actualizaciones:
1. Sube los archivos modificados
2. Si hay cambios en modelos, ejecuta: `python manage.py migrate --settings=PortfolioPatri.settings_production`
3. Si hay nuevos archivos estáticos: `python manage.py collectstatic --settings=PortfolioPatri.settings_production`
4. Recarga la aplicación web 