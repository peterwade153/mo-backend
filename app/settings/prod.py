import dj_database_url7
from .base import *


DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
