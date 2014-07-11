#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from threading import Lock
from urllib import quote_plus
from urlparse import urlparse

def removeControlCharacters(string):
    delchrs = ''.join([chr(x) for x in range(0x20) + range(0x7f, 0xa0)])
    return string.translate(None, delchrs)

def getNthName(n):
    string = ''
    while True:
        string = chr(97 + n % 26) + string
        n /= 26
        if n == 0:
            return string
        n -= 1

class LyliDatabase:

    def __init__(self, link_database_filename, access_database_filename):
        self.links = []
        self.buildCache(link_database_filename)
        self.accessfile = open(access_database_filename, 'a')
        self.linkfile = open(link_database_filename, 'a')
        self.lock = Lock()
        self.name_counter = 0
   
    def buildCache(self, link_database_filename):
        with open(link_database_filename) as f:
            while True:
                line = f.readline().split()
                if not line:
                    break
                timestamp = line[0]
                name = line[1]
                url = line[2]
                self.links.append((timestamp, name, url))

    def request(self, message):
        with self.lock:
            message = removeControlCharacters(message)
            self.accessfile.write('%d %s\n' % (time(), message))
            self.accessfile.flush()
            
            if message.count(' ') < 1:
                return ''
            command, arguments = message.split(' ', 1)
            arguments = arguments.split()
            if not arguments:
                return ''

            if command == 'GET':
                url = self.getURLByName(quote_plus(arguments[0]))
                if url is None:
                    return 'NONEXISTENT'
                else:
                    return 'URL %s' % url

            elif command == 'CREATE':
                if len(arguments) > 1:
                    name = quote_plus(arguments[1])
                else:
                    name = self.generateName()

                if self.getURLByName(name) is not None:
                    return 'TAKEN'
                else:
                    parsed = urlparse(arguments[0])
                    if not parsed.scheme in ['http', 'https'] or parsed.netloc == '':
                        return 'ILLEGAL'
                    entry = (time(), name, parsed.geturl())
                    self.linkfile.write('%d %s %s\n' % entry)
                    self.linkfile.flush()
                    self.links.append(entry)
                    return 'SUCCESS http://lyli.fi/%s' % name
            else:
                return ''
    
    def getURLByName(self, name): 
        for link in reversed(self.links):
            if link[1] == name:
                return link[2]
        return None

    def generateName(self):
        while True:
            name = getNthName(self.name_counter)
            self.name_counter += 1
            if self.getURLByName(name) is None:
                return name
