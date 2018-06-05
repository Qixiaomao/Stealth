#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: v1.0
@software: PyCharm
@file: cms_info.py

"""

import os
import requests
import hashlib
import gevent
import time
import config as config
import codecs
from gevent.queue import Queue

class CMS(object):
    def  __init__(self,url):
        self.q = Queue()
        self.url = url.rstrip("/")
        if self.url is None:
            self.url = url
        script_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        finally_path = os.path.join(script_path, 'config/{0}'.format("cms.txt"))
        with codecs.open(finally_path, 'r', encoding="gbk") as f:
            for line in f:
                self.q.put(line.split('|'))

    def get_md5(self, content):
        md = hashlib.md5()
        md.update(content.encode('utf-8'))
        