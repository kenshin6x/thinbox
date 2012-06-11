from thinbox.lib.routeros.routeros_ssh_handler import RouterOSSSHHandler
from thinbox.app.core import models as cmodels, constants as cconstants

class RouterOSHandler:
    gateway = None
    result = None
    handler = None

    def __init__(self,gateway,*args,**kwargs):
        self.gateway = gateway
        try:
            if self.gateway.access_method == cconstants.ACCESS_METHOD_SSH:
                self.result = self.ssh_exec()
                self.handler = RouterOSSSHHandler

            if self.gateway.access_method == cconstants.ACCESS_METHOD_TELNET:
                self.result = self.telnet_exec()

            if self.gateway.access_method == cconstants.ACCESS_METHOD_API:
                self.result = self.api_exec()

        except AttributeError:
            self.result = None


class InterfaceList(RouterOSHandler):
    def ssh_exec(self):
        self.result = self.handler.run(gateway,'ip ')
        return self.result
