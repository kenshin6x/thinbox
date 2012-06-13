# -*- coding: utf-8 -*- 

from django.conf.urls.defaults import *
from thinbox.app.rest.handlers import *
from piston.authentication import HttpBasicAuthentication

auth = HttpBasicAuthentication(realm="Thinbox Authentication")

#gateway_handler = Resource(GatewayHandler, authentication=auth)
validate_handler = Resource(ValidateHandler)

urlpatterns = patterns('',

    url(r'^/validate/$',validate_handler),


)