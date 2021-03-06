from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'POVRay.views.home', name='home'),
    # url(r'^POVRay/', include('POVRay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^/?$', 'POVRay.views.index', name='home'),
    url(r'^register/?$', 'POVRay.views.register', name='register'),
    url(r'^login/?$', 'POVRay.views.loginPage', name='login'),
    url(r'^logout/?$', 'POVRay.views.logoutPage', name='logout'),
    url(r'^account/?$', 'POVRay.views.account', name='account'),
    url(r'^render/?$', 'POVRay.renders.views.render', name='render'),
    url(r'^my_renders/?$', 'POVRay.renders.views.my_renders', name='my_renders'),
    url(r'^render/ajax/(?P<action>[\w\-_]+)/?$', 'POVRay.renders.views.ajax', name='ajax'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #  url(r'^admin/(.*), admin.site.root),

)
