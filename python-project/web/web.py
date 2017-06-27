#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import BaseHTTPServer
import CGIHTTPServer

HOST=''
PORT=8000

server=BaseHTTPServer.HTTPServer((HOST,PORT),CGIHTTPServer.CGIHTTPRequestHandler)

server.serve_forever()
