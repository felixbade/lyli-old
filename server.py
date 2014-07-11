#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server_listener import ServerListener
from lylidatabase import LyliDatabase

class LyliServer:

    def __init__(self):
        # NOTE: should these values be hard-coded or not?
        self.port = 8771
        self.database = LyliDatabase('links.txt', 'access.log')
        self.listener = ServerListener(self)

    def new_connection(self, socket, address):
        # TODO: make this asynchronous
        request = socket.makefile().readline()
        response = self.database.request(request)
        socket.send(response + '\n')
        socket.close()

    def run(self):
        self.listener.serve_forever()

    def stop(self):
        # TODO: kill all (not yet) asynchronous threads
        pass
