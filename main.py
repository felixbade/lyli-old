#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from os import fork

from server import LyliServer

pid = fork()
if pid > 0:
    print 'PID: %d' % pid
    exit(0)
elif pid < 0:
    print 'ERROR'
    exit(1)

server = LyliServer()

try:
    server.run()
except KeyboardInterrupt:
    print
    server.stop()
