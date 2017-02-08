#!/usr/bin/python
import os
import sys

VIRTUAL_PATH = '/var/www/idof'
ACTIVATE_THIS = VIRTUAL_PATH + '/env/bin/activate_this.py'

if os.path.isfile(ACTIVATE_THIS):
    sys.path.insert(0,VIRTUAL_PATH)
    #Activate the virtual environment
    with open(ACTIVATE_THIS, 'r') as f:
        code = compile(f.read(), ACTIVATE_THIS, 'exec')
        exec(code, dict(__file__=ACTIVATE_THIS))

import app
application = app.create_app()
