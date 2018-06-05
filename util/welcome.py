#!/usr/bin/env/ python
#-*- encoding: utf-8 -*-

"""

@version: v1.0
@author: heln
@software: vscode
@file: Stealth.py
@time: 2018/05/22

"""

from  termcolor import colored


class  Welcome:
    def __init__(self):
        self.__author__, self.__version__, self.__date__ = ("Hong AnQuan ","1.0.0","2018/5/22")
    def headline(self):
        print(colored('                       ☺ Built by {0}  ©{1} Version is {2} ☻                                             '.format
                                       (self.__author__, self.__date__, self.__version__), 'red',attrs=['bold']))  
        print(colored('  █████████   ███████▄██ ███████     ▄████████    ███▄   ▄▄▄████████ ▄█   ███', 'blue'))
        print(colored('  ██        ███        ▀█████  ███▄      ███    ███   ███    ███ █     ██▀▀▀██▄   ███    ███  ', 'red'))
        print(colored('  ██       ▀███       ███▀▀█  █ █ ███ ███      ███         ██████  ███    ███', 'blue'))
        print(colored('  ██                         ███     ▀            ▄██    ███   ███    ███  █   ██  ███ ███', 'red'))
        print(colored('  ██████████         ███     ▀▀███▀▀▀    ▀▀███▀▀▀▀▀█    ███   ███   ▀██    █████████   ', 'blue'))
        print(colored('            █████       ███       █▄▀█████         ██       ██      ███          ███    ███     ███', 'red'))
        print(colored('              ▀███     ███           ██████ ███    ███      ███    ███           ███▌ █        ███', 'blue'))
        print(colored('  ██████████  ▄████▀          ██████████   █████████  ███▀███    ███  █▀  ████', 'red'))