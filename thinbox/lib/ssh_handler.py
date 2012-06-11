# -*- coding: utf-8 -*- 

import paramiko 
import socket

class SSHHandler:    
    def __init__(self,dest):
        self.host = dest      
        self.ssh = paramiko.SSHClient()
            
    def connect(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh.connect(hostname=self.host.get('host'),
                        port=self.host.get('port') or 22,
                        username=self.host.get('username'),
                        password=self.host.get('password'),
                        timeout=self.host.get('timeout') or 20)
            return True, None            
        except paramiko.AuthenticationException, e: return False, e
        except paramiko.BadHostKeyException, e: return False, e
        except paramiko.ChannelException, e: return False, e
        except paramiko.PasswordRequiredException, e: return False, e
        except paramiko.SSHException, e: return False, e
        except socket.error,e: return False, e
        except socket.timeout,e: return False, e
    
        return False, None
        
    def close(self):
        try:
            self.ssh.close()
        except:
            pass
            
    def run(self,*args,**kwargs):
        stdin, stdout, stderr = self.ssh.exec_command(kwargs.get('command'))
        if kwargs.get('stdin'):
            for sin in kwargs.get('stdin'):
                stdin.write(sin)
            stdin.flush() 
               
        if kwargs.get('ret') == 'read':         result = stdout.read()
        elif kwargs.get('ret') == 'readlines':  result = stdout.readlines()
        else: result = stdout      
        return stderr.readlines(), result
        
