# -*- coding: utf-8 -*- 

from django.utils.translation import ugettext, ugettext_lazy as _
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from django.views.generic import *
from django.contrib.auth.decorators import permission_required

from thinbox.app.mobile import forms as mforms
from thinbox.app.core import models as cmodels
from thinbox.app.core.routeros_handler import * 

class GatewayHomeView(DetailView):
    template_name = 'mobile/gateway/gateway_home.html'
    model = cmodels.Gateway
    context_object_name = 'gateway'
    slug_field = 'id'
    
    
class InterfaceListView(DetailView):
    template_name = 'mobile/gateway/interface_list.html'
    model = cmodels.Gateway
    context_object_name = 'gateway'
    slug_field = 'id'
    
    def get(self,*args,**kwargs):
        result = InterfaceList(gateway=self.get_object()).result
        
        return HttpResponse(result)