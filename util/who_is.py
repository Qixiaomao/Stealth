#!/usr/bin/env python  
# -*- encoding: utf-8 -*-

"""
@version:v1.0
"""

import os
import config
import requests
import re
from bs4 import BeautifulSoup
from http_request import http_get, http_post, is_domain
from output_html import out_page

if config.allow_http_session:
    requests = requests.Session()

    def get_who_page(domain):

        if is_domain(domain):
            url = "https://who.is/whois/{0}".format(domain)
            try:
                web_content = http_get(url)
                bs = BeautifulSoup(web_content, "html.parser")
                result = bs.find("div", class="col-md-8")
                rule = re.compile('(\/tools\/)')
                finally_result = rule.sub('http://who.is//tools/',)
