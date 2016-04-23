#!/usr/bin/env python 

from fabric.api import *  
from fabric.context_managers import *  
from fabric.contrib.console import confirm  

host_1 = '10.136.64.101'
host_2 = '10.136.64.102'
host_3 = '10.136.64.103'
host_4 = '10.136.64.112'
host_5 = '10.136.64.114'

env.hosts = [host_1, host_2, host_3, host_4, host_5] 
env.passwords = {
	host_1 : 'operator@htscl',
	host_2 : 'core09',
	host_3 : 'core09',
	host_4 : 'core09',
	host_5 : 'core09',
}
env.roledefs = {
    'ArchiveEngin': [host_2, host_3],
    'IOCServer': [host_2],
    'CssDeveloper': [host_4], 
    'SddDeveloper': [host_5], 
    'WebServer': [host_1], 
    'OPI': [host_1, host_2, host_3, host_4, host_5], 
}

@roles('ArchiveEngin')
@serial
def taska():
#    run('ifconfig')
    pass

@roles('IOCServer')
@parallel(pool_size = 5)
def taskb():
#    run('ls /var/www')
    pass
