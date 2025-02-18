# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
from decouple import config

ALL_DATABASES = {
    'default': {
    },
    "pgsql": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_NAME'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT'),
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME':config('MONGODB_NAME'),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': "localhost",
            'port': 27017,
        }
    },
    'sqlite' : {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "backend" / "api" / "database" / "sqlite" / "db.sqlite",
    },
    
#     'cassandra': {
#         'ENGINE': 'django_cassandra_engine',
#         'NAME': os.getenv('CASSANDRA_KEYSPACE'),
#         'HOST': os.getenv('CASSANDRA_HOST'),
#         'PORT': os.getenv('CASSANDRA_PORT'),
#         'USER': os.getenv('CASSANDRA_USER'),
#         'PASSWORD': os.getenv('CASSANDRA_PASSWORD'),    }
}
ALL_DATABASES['default'] = ALL_DATABASES['sqlite']