#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lylidatabase

l = lylidatabase.LyliDatabase('links.txt', 'access.log')
while True:
    print l.request(raw_input())
