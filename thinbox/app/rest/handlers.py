# -*- coding: utf-8 -*- 

from piston.handler import BaseHandler
from piston.resource import Resource
from thinbox.app.core import models as cmodels

class ValidateHandler(BaseHandler):
   allowed_methods = ('GET',)

   def read(self, request, gateway_id=None):
        results = []
        
        results.append({
                "response" : True,
        })

        return results