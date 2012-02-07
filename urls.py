from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

if settings.DEBUG:
  urlpatterns = patterns('',
    #
    ## Device
    #
    # New device registration [POST]
    url(r'^device/$', 'device.views.create_device'),

    #
    ## Manifest
    #
    # Download Manifest [GET]
    url(r'^manifest/(?P<deviceId>[A-Z0-9]\w+)/$', 'manifest.views.download_manifest'),

    #
    ## Logger
    #
    # POST Logfiles [POST]
    url(r'^log/(?P<deviceId>[A-Z0-9]\w+)/$', 'datalogger.views.upload_log'),

    #
    ## Application
    #
    # Download Application [GET]
    url(r'^experiment/(?P<deviceId>[A-Z0-9]\w+)/$', 'application.views.get_download'),

    #
    ## Error
    #
    # Error Handling [POST]
    url(r'^error/(?P<deviceId>[A-Z0-9]\w+)/$', 'error.views.create_error'),
  )
