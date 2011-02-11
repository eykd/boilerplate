# -*- coding: utf-8 -*-
"""settings._paths -- common path settings

Copyright 2010 David Eyk. All rights reserved.
"""
import sys
from paver.easy import path
__path__ = path(__file__).abspath().dirname()

SITE_ROOT = __path__.dirname()
PROJECT_ROOT = SITE_ROOT.dirname()

APPS_ROOT = SITE_ROOT / 'apps'
LIB_ROOT = SITE_ROOT / 'lib'

sys.path.append(PROJECT_ROOT)

if APPS_ROOT.exists():
    sys.path.append(APPS_ROOT)

if LIB_ROOT.exists():
    sys.path.append(LIB_ROOT)
