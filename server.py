#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server_listener import ServerListener
from lylidatabase import LyliDatabase
from client_connection import LyliClientConnection

class LyliServer:

    def __init__(self):
        # NOTE: should these values be hard-coded or not?
        self.port = 8771
        self.database = LyliDatabase('links.txt', 'access.log')
        self.listener = ServerListener(self)
        self.threads = []

    def new_connection(self, socket, address):
        lyliclient = LyliClientConnection(socket, self.database)

    def run(self):
        self.listener.serve_forever()

    def stop(self):
        print 'Stopping server'
