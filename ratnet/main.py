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
import sys
import logging

from flask import Flask, render_template, redirect, request, abort

log = logging.getLogger(__name__)

#
# Application configuration
#

app = Flask('ratnet')


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
