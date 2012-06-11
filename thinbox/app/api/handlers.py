# -*- coding: utf-8 -*- 

from piston.handler import BaseHandler
from piston.resource import Resource
from thinbox.app.core import models as cmodels

class GatewayHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = cmodels.Gateway

   def read(self, request, gateway_id=None):
        if gateway_id:
            gateways = self.model.objects.filter(pk=gateway_id)
        else:
            gateways = self.model.objects.all()
            
        results = []
        
        for gateway in gateways:
            results.append({
                "id" : gateway.id,
                "name" : gateway.name,
                "access_ip" : gateway.access_ip,
            })

        return results