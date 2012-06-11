# -*- coding: utf-8 -*- 

from django.conf.urls import patterns, include, url
from django.contrib import admin

from thinbox.app.mobile.views.auth import LoginView, LogoutView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^user/login/$', LoginView.as_view(), name="mobile_login"),
    url(r'^user/logout/$', LogoutView.as_view(), name="mobile_logout"),
    
    (r'^admin/', include(admin.site.urls)),
    (r'm', include('thinbox.app.mobile.urls')),
)
