from pathlib import Path
from .settings import BASE_DIR 

SECRET_KEY = 'django-insecure-&2h*pd(+0t*3az7(k!=6!f#8h@f%4!3iusg&k+g&_8hj+umiwp'


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'domein', 'www.domain.uz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'it_platform_db',
        'USER': 'postgres',
        'PASSWORD': 'ali',
        'HOST': 'localhost',
        'port': '5432',
    }
}

STATIC_DIR = Path(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = Path(BASE_DIR, 'static')
