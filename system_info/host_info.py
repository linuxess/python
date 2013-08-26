#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import socket
import os, statvfs
from commands import getstatusoutput
 
 
class System(object):
    def __init__(self,ip):
        self.ip = ip        
        self.return_dict = {"hostname":"","load":{"one_min":"","five_min":"","fifteen_min":""},"cores":4,\
                "mem":{"total":"","used":"","buffers":"","cached":""},"disk":{"home":"","root":""}}
 
    def remote_cmd(self,cmd):
            cmd = 'ssh %s \"%s\"' % (self.ip,cmd)
            (status,result)=getstatusoutput(cmd)
            return result
 
    def host_name(self):
        try:
            hostname = socket.gethostbyaddr(self.ip)
            self.return_dict['hostname'] = hostname[0]
        except:
            return False 
 
    def load_stat(self):
        loadavg = {}
        #f = open("/proc/loadavg")
        cmd = "cat /proc/loadavg"
        result = self.remote_cmd(cmd)
        con = result.split()
        #f.close()
        self.return_dict['load']['one_min']=con[0]
        self.return_dict['load']['five_min']=con[1]
        self.return_dict['load']['fifteen_min']=con[2]
 
 
    def cpu_cores(self):
        import multiprocessing
        cores = multiprocessing.cpu_count()    
        return_dict['cores'] = cores
 
    def mem_info(self):
        cmd = "free -m|sed -n '2p'"
        result = self.remote_cmd(cmd).split()
        self.return_dict['mem']['total'] = result[1]
        self.return_dict['mem']['used'] = result[2]
        self.return_dict['mem']['buffers'] = result[5]
        self.return_dict['mem']['cached'] = result[6]
 
 
    def disk_stat(self): 
        cmd_root = "df / |tail -1"
        cmd_home = "df /home |tail -1"
        result_root = self.remote_cmd(cmd_root)
        result_home = self.remote_cmd(cmd_home)
        self.return_dict['disk']['root'] = result_root.split()[4][:-1]
        self.return_dict['disk']['home'] = result_home.split()[4][:-1]
 
    def main(self):
        self.host_name()
        self.load_stat()
        self.mem_info()
        self.disk_stat()
        return self.return_dict
 
 
 
if __name__ == "__main__":
    host_list = ['1.1.1.1','1.1.1.2']
    a=[]
    for i in host_list:
        A = System(i)
        a.append(A.main())
    print a

