#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread

class LyliClientConnection(Thread):

    def __init__(self, socket, database):
        Thread.__init__(self)
        self.socket = socket
        self.database = database
        self.daemon = True
        self.start()

    def run(self):
        self.socket.settimeout(60)
        request = self.socket.makefile().readline()
        response = self.database.request(request)
        self.socket.send(response + '\n')
        self.socket.close()
