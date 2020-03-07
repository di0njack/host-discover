#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DEVELOPED BY Di0nJ@ck - May 2019 - v1.0
__author__      = 'Di0nj@ck'
__version__     = 'v1.0'
__last_update__ = 'May 2019'

import socket
import ipaddress


results = []
host_name = ""
networks = ["127.0.0.1","192.168.0.1"]


for network in networks:
    print ("- Processing network: " + network + '\n')
    for ip in ipaddress.IPv4Network(network):
        ip_addr = ip._string_from_ip_int(ip._ip)

       
        #print ("   * IPv4: " +  ip_addr + '\n')
        
        
        try:
            host_name = socket.gethostbyaddr(ip_addr) #CHECKS IF HOST IS ALIVE
            print ("      > Found hostname: " + str(host_name) + '\n')
        except Exception as e:
            print ("      > Error!: " + str(e) + '\n') 
            continue
            
        if "some_keyword" in host_name: #CHOOSE A KEYWORD IDENTIFYING YOUR PENTEST SCOPE FOR FILTERING OUT RELATED HOSTS
            results.append(host_name)
  

print (results)