# -*- coding: utf-8 -*- 

from django.conf.urls import patterns, include, url
from thinbox.app.mobile.views import auth, gateway

urlpatterns = patterns('',

    url(r'^/$',auth.HomeView.as_view(),name='home'),
    url(r'^/settings/$',auth.SettingsView.as_view(),name='settings'),
    
    # gateway
    url(r'^/gateway/(?P<slug>\d+)/home/$',gateway.GatewayHomeView.as_view(),name='gateway_home'),
    
    # interface
    url(r'^/gateway/(?P<slug>\d+)/interface/list/$',gateway.InterfaceListView.as_view(),name='interface_list'),
    
    #wireless
    
    #...
)
