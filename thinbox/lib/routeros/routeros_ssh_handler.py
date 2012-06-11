# -*- coding: utf-8 -*- 

from thinbox.lib import ssh_handler
import logging

logger = logging.getLogger(__name__)

class RouterOSSSHHandler:
    """
     Componente responsável por realizar os comandos no Mikrotik 
     via SSH.

     Necessário serviço de SSH habilitado ( /ip service ssh enable ) 
    """
    def run(self,access_info,cmd,ret='readlines'):
        dest = self.gateway_to_dest(access_info)

        try:
            s = ssh.SSHHandler(dest)
            result, error = s.connect()
            rescmd = []
            if result == True:
                errors, rescmd = s.run(command=cmd,ret=ret)
                s.close()
                if errors:
                    return False, errors
                return True, rescmd
        except Exception, e:
            try:
                return False, e[1]
            except:
                return False, e

    def gateway_to_dest(self,gateway):
        """
         Converte Objeto NAS para dicionário Python
        """
        return  { 
            'host':     gateway.access_ip,
            'port':     gateway.access_port,
            'username': gateway.access_login,
            'password': gateway.access_password,
            'type':     gateway.access_method,
            'timeout':  gateway.access_timeout or 20
        }
