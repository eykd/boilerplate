# -*- coding: utf-8 -*-
"""settings.production -- production settings for Livestead.

Copyright 2010 David Eyk. All rights reserved.
"""
import logging
import sys

from _paths import *
from _common import *

META_ROOT = path('/home/livestead/sites/livestead.com')

DEBUG = False
TESTING = DEBUG
TEMPLATE_DEBUG = DEBUG
MEDIA_DEV_MODE = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'livestead',
        'USER': 'livestead',
        'PASSWORD': (META_ROOT / 'secrets' / 'db_password.txt').text(),
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        },
    }
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

SERVE_MEDIA = False

logger = logging.getLogger()
logger.addHandler(CONSOLE_HANDLER)
logger.setLevel(logging.INFO)

DOMAIN_ROOT = 'livestead'

# Make this unique, and don't share it with anybody.
SECRET_KEY = (META_ROOT / 'secrets' / 'secret_key.txt').text()

AWS_ACCESS_KEY_ID = (META_ROOT / 'secrets' / 'aws_access_key_id').text()
AWS_SECRET_ACCESS_KEY = (META_ROOT / 'secrets' / 'aws_secret_access_key').text()
