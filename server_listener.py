#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

class ServerListener:

    def __init__(self, server):
        self.server = server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def serve_forever(self):
        self.socket.bind(('', self.server.port))
        self.socket.listen(10)
        
        port = self.socket.getsockname()[1]
        print 'Server is now listening on port %d' % port
        
        while True:
            connection, address = self.socket.accept()
            self.server.new_connection(connection, address)
