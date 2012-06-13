# -*- coding: utf-8 -*- 

from django.conf.urls.defaults import *
from thinbox.app.api.handlers import *
from piston.authentication import HttpBasicAuthentication

auth = HttpBasicAuthentication(realm="Thinbox Authentication")

#gateway_handler = Resource(GatewayHandler, authentication=auth)
gateway_handler = Resource(GatewayHandler)

urlpatterns = patterns('',

    url(r'^gateway/(?P<gateway_id>[^/]+)/', gateway_handler),
    url(r'^gateways/', gateway_handler),


)