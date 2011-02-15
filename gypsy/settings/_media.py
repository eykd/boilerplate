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
     'css/_oocss/core/grid/grids_debug.css',
     'css/_oocss/core/module/mod_debug.css',
     'css/_oocss/core/media/media_debug.css',
     'css/_oocss/core/table/table_debug.css',
     ),

    ## Browser-specific patches
    ########
    ('win-ie-all.css',
     ########
     'css/_patches/win-ie-all.css',
     ),
    
    ("win-ie7.css",
     ########
     "css/_patches/win-ie7.css",
     ),

    ("win-ie-old.css",
     ########
     "css/_patches/win-ie-old.css",
     ),

    ("win-ie6-below.css",
     ########
     "css/_patches/win-ie6-below.css",
     ),

    ("win-ie5.css",
     ########
     "css/_patches/win-ie5.css",
     ),


    ##########
    ######  JS
    ##########

    ('modernizr.js',
     ########
     'js/_lib/modernizr.min.js',
     ),

    ('main.js',
     ########
     'js/_lib/json2.js',
     'js/_lib/jquery.js',
     'js/_lib/underscore.js',
     'js/_lib/backbone.js',
     'js/_lib/markdown.js',
     'js/_lib/crafty.js',

     ## plugins
     'js/_plugins/ba-debug.js',
     'js/_plugins/namespace.js',
    ),

    ('dd_belatedpng.js',
     ########
     'js/_lib/dd_belatedpng.js',
     ),

    ('ie9.js',
     ########
     'js/_patches/IE9.js',
     ),

    ('ie7.js',
     ########
     'js/_patches/ie7-squish.js',
     ),

    ('profiling.js',
     ########
     'js/_dev/profiling/yahoo-profiling.js',
     'js/_dev/profiling/config.js',
     ),
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
