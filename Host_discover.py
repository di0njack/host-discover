#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DEVELOPED BY Di0nJ@ck - May 2019 - v1.0
__author__      = 'Di0nj@ck'
__version__     = 'v1.0'
__last_update__ = 'May 2019'

import socket
import ipaddress,argparse,sys


results = []

def file_to_list(file_path): #Read a TXT file with an item per line and returns a load Python list containing these items
   
    my_list = []

    try:
        with open(file_path, 'r+', encoding="utf-8") as infile:
                        lines = filter(None, (line.rstrip() for line in infile))
                        for myline in lines: 
                                if not myline.startswith('#'): #FILTER OUT FILE COMMENTS
                                    my_list.append(myline.strip('\n')) #DELETE NEWLINE CHARACTERS
    except Exception as e:
        print('[!] Error when loading the file: %s.\n\tDetails: %s\n' % (file_path,str(e)))
        sys.exit(1)

    return my_list

def write_file(path,data):
    try:
        with open(path ,'a') as file:
            file.write(data)
    except Exception as e:
        print('[!] Error when writing data to a file: %s.\n\tDetails: %s\n' % (path,str(e)))
        sys.exit(1)

def resolve_ip(ips):
    for ip in ips:
        print ("- Processing IP: " + ip + '\n')
        try:
            ip_obj = ipaddress.IPv4Address(ip)
            ip_addr = ip_obj._string_from_ip_int(ip_obj._ip)
            try:
                host_name = socket.gethostbyaddr(ip_addr) #CHECKS IF HOST IS ALIVE
                print ("      > Found hostname: " + str(host_name) + '\n')
            except Exception as e:
                print ("      > Error!: " + str(e) + '\n') 
                continue
                
            if "some_keyword" in host_name: #CHOOSE A KEYWORD IDENTIFYING YOUR PENTEST SCOPE FOR FILTERING OUT RELATED HOSTS
                results.append(host_name)
        except Exception:
            continue

# *** MAIN CODE ***
if __name__ == '__main__':
     #ARG PARSER
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='Input IP file', dest='input_ip')
    args = parser.parse_args()

    #SAVE INPUT ARGS
    input_file = args.input_ip

    #READ FILE
    ips_list = file_to_list(input_file)

    #RESOLVE IP
    resolve_ip(ips_list)

    #SAVE RESULTS
    write_file("results.txt",results)