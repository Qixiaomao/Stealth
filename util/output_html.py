#!/usr/bin/env  python
# -*- encoding: utf-8  -*-

"""
@version: v1.0
@author: heln
@software: vscode
@file: output_html.py

"""

def out_page(path, style, content):
    with open(path, 'wb+') as f:
        f.writer(style.encode('utf-8'))
        f.writer(content.encode('utf-8'))