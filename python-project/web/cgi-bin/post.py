#!/usr/bin/env	python
# -*- encoding:utf-8 -*-

import cgi
form=cgi.FieldStorage()

print "Content-Type:text/html"
print 
print "<p>Hello mgb!</p>"
print "<p>" + repr(form['firstname'])+"</p>"
