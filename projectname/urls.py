from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', direct_to_template,
                           dict(template="index.html"),
                           name="root"),
                       # Example:
                           # (r'^project/', include('project.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                           # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                           # (r'^admin/', include(admin.site.urls)),
                       )
