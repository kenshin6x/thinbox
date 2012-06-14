from django.conf import settings
from django.http import HttpResponse
import re

class MobileDetectionMiddleware(object):
    def __init__(self):
        self.urls = tuple([re.compile(url) for url in settings.MOBILE_DEVICE_REQUIRED])
    
    def process_request(self, request):
        for url in self.urls:
            if url.match(request.path):
                if not request.is_ajax():
                    is_mobile = False;
            
                    if request.META.has_key('HTTP_USER_AGENT'):
                        user_agent = request.META['HTTP_USER_AGENT']
            
                        # Test common mobile values.
                        pattern = "(up.browser|up.link|mmp|symbian|smartphone|midp|wap|phone|windows ce|pda|mobile|mini|palm|netfront)"
                        prog = re.compile(pattern, re.IGNORECASE)
                        match = prog.search(user_agent)
            
                        if match:
                            is_mobile = True;
                        else:
                            # Nokia like test for WAP browsers.
                            # http://www.developershome.com/wap/xhtmlmp/xhtml_mp_tutorial.asp?page=mimeTypesFileExtension
            
                            if request.META.has_key('HTTP_ACCEPT'):
                                http_accept = request.META['HTTP_ACCEPT']
            
                                pattern = "application/vnd\.wap\.xhtml\+xml"
                                prog = re.compile(pattern, re.IGNORECASE)
            
                                match = prog.search(http_accept)
            
                                if match:
                                    is_mobile = True
            
                        if not is_mobile:
                            # Now we test the user_agent from a big list.
                            user_agents_test = ("w3c ", "acs-", "alav", "alca", "amoi", "audi",
                                                "avan", "benq", "bird", "blac", "blaz", "brew",
                                                "cell", "cldc", "cmd-", "dang", "doco", "eric",
                                                "hipt", "inno", "ipaq", "java", "jigs", "kddi",
                                                "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
                                                "maui", "maxo", "midp", "mits", "mmef", "mobi",
                                                "mot-", "moto", "mwbp", "nec-", "newt", "noki",
                                                "xda",  "palm", "pana", "pant", "phil", "play",
                                                "port", "prox", "qwap", "sage", "sams", "sany",
                                                "sch-", "sec-", "send", "seri", "sgh-", "shar",
                                                "sie-", "siem", "smal", "smar", "sony", "sph-",
                                                "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
                                                "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
                                                "wapi", "wapp", "wapr", "webc", "winw", "winw",
                                                "xda-",)
            
                            test = user_agent[0:4].lower()
                            if test in user_agents_test:
                                is_mobile = True
                                
            
                    request.is_mobile = is_mobile
                    
                    if request.is_mobile:
                        if request.session.get(settings.MOBILE_AUTH_TOKEN_NAME, False):
                            return None
                        elif request.GET.get(settings.MOBILE_AUTH_TOKEN_NAME) == settings.MOBILE_AUTH_TOKEN_VALUE:
                            return None
                        else:
                            return HttpResponse("Access Denied. Token not found.");
                    
                    else:
                        return HttpResponse("Access Denied. Only mobile devices can get access.");
    