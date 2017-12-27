#!/usr/bin/python3
# Copyright 2017, Ken Bannister
# All rights reserved.
#  
# Released under the Mozilla Public License 2.0, as published at the link below.
# http://opensource.org/licenses/MPL-2.0

'''
Entry point for Ratnet application.

Usage:
   $. ./main.py
'''
import sys, logging

from flask import Flask, render_template, redirect, request, abort
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator

log = logging.getLogger(__name__)

#
# Application configuration
#

app = Flask('ratnet')
Bootstrap(app)

# Defaults for application settings

# Used to generate URI prefix below.
app.config['APPLICATION_ROOT'] = '/'

# Allow override config settings from a file
try:
    app.config.from_envvar('RATNET_CONFIG_FILE')
except:
    log.exception('Can\'t read config file; using defaults')

# Prefix for URI path for web server. Used for app route decorators.
URI_PREFIX = app.config['APPLICATION_ROOT']
if URI_PREFIX == None or URI_PREFIX == '/':
    URI_PREFIX = ''

# Navbar definitions
nav = Nav()
nav.register_element('frontend_top', Navbar(
    View('Ratnet', '.index'),
))
nav.init_app(app)

#
# Routes
#

@app.route('{0}/'.format(URI_PREFIX))
def index():
    return render_template('index.html')

#
# Main startup
#

# Run from command line. Runs web server in threaded mode. Although the
# web server is not designed for production, this allows us to handle
# multiple requests during development.
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                        format='%(asctime)s %(module)s %(message)s')
    log.info('Initializing Ratnet')

    formattedPath = '\n\t'.join(str(p) for p in sys.path)
    log.info('Running Ratnet with sys.path:\n\t{0}'.format(formattedPath))

    try:
        app.run(host='0.0.0.0', threaded=True, debug=False)
    except KeyboardInterrupt:
        pass
    except:
        log.exception('Catch-all handler for Ratnet')
