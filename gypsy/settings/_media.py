# -*- coding: utf-8 -*-
"""settings._media -- common media settings.

Copyright 2011 David Eyk. All rights reserved.
"""
from ._paths import PROJECT_ROOT, SITE_ROOT

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''


# http://www.allbuttonspressed.com/projects/django-mediagenerator
MEDIA_DEV_MODE = True
DEV_MEDIA_URL = '/devmedia/'
PRODUCTION_MEDIA_URL = '/media/'

GLOBAL_MEDIA_DIRS = (
    SITE_ROOT / 'media',
    )

MEDIA_BUNDLES = (
    ('main.css',
     ########
     ## baseline
     'css/_baseline/baseline.reset.css',
     'css/_baseline/baseline.base.css',
     'css/_baseline/baseline.type.css',
     'css/_baseline/baseline.table.css',
     'css/_baseline/baseline.form.css',
     ## oocss
     'css/_oocss/core/template/template.css',
     'css/_oocss/core/grid/grids.css',
     'css/_oocss/core/module/mod.css',
     'css/_oocss/core/module/mod_skins.css',
     'css/_oocss/core/media/media.css',
     'css/_oocss/core/content.css',
     'css/_oocss/core/heading/heading.css',
     'css/_oocss/core/spacing/space.css',
     'css/_oocss/core/table/table.css',
     'css/_oocss/core/table/table_skins.css',
     ## other
     'css/core.css',
     'css/helpers.css',
     'css/logos.css',
    ),

    ('debug.css',
     ########
     'css/_oocss/core/template/template_debug.css',
     'css/_oocss//core/grid/grids_debug.css',
     'css/_oocss//core/module/mod_debug.css',
     'css/_oocss//core/media/media_debug.css',
     'css/_oocss//core/table/table_debug.css',
     ),

    ('main.js',
     ########
     'js/libs/json2.js',
     'js/libs/jquery.js',
     'js/libs/underscore.js',
     'js/libs/backbone.js',
     'js/libs/crafty.js',
    ),

    ('modernizr.js',
     ########
     'js/libs/modernizr.min.js',
     ),

    ('dd_belatedpng.js',
     ########
     'js/libs/dd_belatedpng.js',
     )
    )

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = PROJECT_ROOT / 'external' / 'bin' / 'yuicompressor-2.4.2.jar'

# URL prefix for admin media -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/media/admin/'
