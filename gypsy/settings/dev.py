# -*- coding: utf-8 -*-
"""settings.dev -- development settings

Copyright 2011 David Eyk. All rights reserved.
"""
from ._common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
MEDIA_DEV_MODE = True

INSTALLED_APPS += (
    'debug_toolbar',
    )
