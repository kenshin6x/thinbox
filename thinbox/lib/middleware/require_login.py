from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import re

class RequireLoginMiddleware(object):
    url = None
    
    def __init__(self):
        self.urls = tuple([re.compile(url) for url in settings.LOGIN_REQUIRED_URLS])
    
    def process_request(self, request):
        for url in self.urls:
            if url.match(request.path) and (request.user.is_anonymous() or not request.user.is_staff):
                if not request.is_ajax():
                    
                    if request.GET.get(settings.MOBILE_AUTH_TOKEN_NAME):
                        self.url = '%s?next=%s&%s=%s' % (settings.LOGIN_URL, request.path,settings.MOBILE_AUTH_TOKEN_NAME,request.GET.get(settings.MOBILE_AUTH_TOKEN_NAME))
                    else:
                        self.url = '%s?next=%s' % (settings.LOGIN_URL, request.path)
                    
                    return HttpResponseRedirect(self.url)
                else:
                    return render_to_response('401.html',{
                                               'LOGINURL': settings.LOGIN_URL
                                               })
