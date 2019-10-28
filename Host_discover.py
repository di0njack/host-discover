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
networks = ["185.65.184.0/22","212.63.96.0/21","89.42.164.0/22","37.98.200.0/22","185.67.112.0/22","109.232.64.0/21","146.66.136.0/21","37.152.80.0/21","185.15.148.0/22","146.66.136.0/24","146.66.137.0/24","146.66.138.0/24","109.232.68.0/24","109.232.69.0/24","109.232.70.0/24","109.232.71.0/24","185.65.64.0/22","176.56.119.0/24"]


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