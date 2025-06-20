import os
import sys

# Agregar el directorio del proyecto al path de Python
path = '/home/DraPatriciaAlejandraMartin/PortfolioPatri'
if path not in sys.path:
    sys.path.insert(0, path)

# Configurar la variable de entorno para Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'PortfolioPatri.settings_production'

# Importar la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 