#!/usr/local/bin/python3.4
import cgitb; cgitb.enable()  # This line enables CGI error reporting
from wsgiref.handlers import CGIHandler
import sys
sys.path.append("/home/users/2/punyu.jp-studiokura/pythonmodules")
from server import app

CGIHandler().run(app)
