#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

from server import LyliServer

server = LyliServer()

try:
    server.run()
except KeyboardInterrupt:
    print
    server.stop()
