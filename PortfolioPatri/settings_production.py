from .settings import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Permitir el dominio de PythonAnywhere
ALLOWED_HOSTS = ['drapatriciaalejandramartin.pythonanywhere.com', 'www.drapatriciaalejandramartin.pythonanywhere.com']

# Configuración de archivos estáticos para producción
STATIC_ROOT = '/home/DraPatriciaAlejandraMartin/PortfolioPatri/static_root'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Configuración de media files (si se necesitan en el futuro)
MEDIA_ROOT = '/home/DraPatriciaAlejandraMartin/PortfolioPatri/media'
MEDIA_URL = '/media/'

# Configuración de seguridad adicional
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY' 