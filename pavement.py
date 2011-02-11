# -*- coding: utf-8 -*-
"""modulename -- 

Copyright 2011 David Eyk. All rights reserved.
"""
import warnings
warnings.filterwarnings('ignore', "Parent module 'pavement' not found while handling absolute import")

import re
import os
import site

from paver.easy import *
from paver.setuputils import setup, find_package_data
from paver.virtual import bootstrap

from paved import *
from paved import dist
from paved import django
from paved import util

PROJECT_NAME = 'gypsy'
VERSION = '0.1'

__path__ = path(__file__).abspath().dirname()
WORKON_HOME = path(os.environ['WORKON_HOME'])
VIRTUALENV = WORKON_HOME / PROJECT_NAME

site.addsitedir(__path__)
site.addsitedir(VIRTUALENV / 'lib' / 'python2.6' / 'site-packages')

options(
    minilib = Bunch(
        extra_files=['doctools', 'virtual']
        ), 

    virtualenv = Bunch(
        script_name='bootstrap.py',
        packages_to_install=(
            'nose',
            'django_nose',
            'django-debug-toolbar',
            'Werkzeug',
            ),
        paver_command_line='_virtualenv_post',
        name=PROJECT_NAME,
        workon_home=WORKON_HOME,
        virtualenv=VIRTUALENV,
        requirements=__path__ / 'REQUIREMENTS',
        activate_cmd='source ' + (VIRTUALENV / 'bin' / 'activate'),
        ),
    
    # Requirements for production (setuptools safe)
    #install_requires = INSTALL_REQUIRES,
    setup_requires = ['Paver', 'Paved', 'virtualenv'],

    zip_safe = False,
    )

util.update(
    options.paved.django,
    dict(
        settings = '%s.settings.dev' % PROJECT_NAME,
        syncdb = Bunch(
            fixtures = (__path__ / PROJECT_NAME / 'db').listdir('*.json'),
            ),
        manage_py = __path__ / PROJECT_NAME / 'manage.py',
        test = Bunch(
            settings = '%s.settings.test' % PROJECT_NAME,
            ),
        )
    )

setup(
    name=PROJECT_NAME.title(),
    version=VERSION,
    url="http://eykd.net/",
    author="David Eyk",
    author_email="eykd@eykd.net",

    package_dir = {'': '.'},
    packages = [PROJECT_NAME],

    #dependency_links = ['http://cheese.eykd.net/%s/' % PROJECT_NAME],

    include_package_data = True,
    exclude_package_data = {'.': ['*.c', '*.h', '*.pyx', '*.pxd', '*.g']},

    #install_requires = options.install_requires,
    setup_requires = options.setup_requires,
    zip_safe = options.zip_safe,

    test_suite = "django_nose.NoseTestSuiteRunner",
)

options.paved.clean.patterns.append('*.orig')

### TASKS
#########


@task
def clean_orig():
    """Clean up *.orig files created by merges.
    """
    util.rmFilePatterns("*.orig")


@task
def requirements():
    """Update the REQUIREMENTS file.
    """
    sh('pip -E {virtualenv} freeze > {requirements}'.format(**options.virtualenv))


@task
@needs('bootstrap', 'generate_setup')
def env():
    """Set up the virtual environment.
    """
    util.shv('python setup.py develop')


@task
@needs('generate_setup', 'minilib')
def _virtualenv_post():
    """Further procedures to run after the virtualenv is set up.
    """
    util.shv('pip install -r REQUIREMENTS')
    util.shv('python setup.py develop')


@task
def deploy():
    sh('time fab update')
