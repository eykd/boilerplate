# -*- coding: utf-8 -*-
"""settings.test -- common test settings.

Copyright 2011 David Eyk. All rights reserved.
"""


from dev import *

TESTING = True

INSTALLED_APPS = (
    'django_nose',
    # Apps to test...
    )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
