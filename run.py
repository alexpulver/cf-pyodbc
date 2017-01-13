#!/usr/bin/env python

import os
import sys

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    try:
        import pyodbc
    except:
        error = sys.exc_info()[0].__name__ + ': ' + str(sys.exc_info()[1])
        return 'Could not import pyodbc: ' + error + '\n', 500
    else:
        return str(dir(pyodbc))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
