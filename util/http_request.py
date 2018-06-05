#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

""" 
@version: v1.0 

"""

import config
import requests
import re

if config.allow_http_session:
   requests = requests.session()

def http_get(domain):
    try:
        if config.allow_http_proxies == {}:
            result = requests.get(domain, headers=config.headers, timeout=config.timeout,verify=config.allow_ssl_verify).text
        else:
            result = requests.get(domain, headers=config.headers, timeout=config.timeout,proxies=config.allow_proxies,verify=config.allow_ssl_verify).text
        
        return result 
                
    except Exception as e:
                print(e) 


def is_domain(domain):
    domain_regex = re.compile(
        r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z0-9-]{2,}(?<!-))\Z' ,re.IGNORECASE)
    
    return True if domain_regex.match(domain)  else  False