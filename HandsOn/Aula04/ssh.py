#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:05:25 2017
@author: Everton
"""

from paramiko.client import SSHClient
import paramiko 

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print client

host = '192.168.202.1'
user = 'noturno'
password = '4linux'

client.connect(hostname=host,username=user,password=password)
stdin, stdout, stder = client.exec_command('ls -la')

print stdout.read()