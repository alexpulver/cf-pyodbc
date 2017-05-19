#!/usr/bin/env python

import os
import sys

import pyodbc
from flask import Flask

import vcap_services


app = Flask(__name__)
app.config.from_mapping(vcap_services.get_config())


@app.route('/')
def index():
    db_config = {  
        'DRIVER': '{FreeTDS}',  # Here DRIVER is literal string all uppercase.  
        'server': app.config['MSSQL_SERVER'],
        'port': app.config['MSSQL_PORT'],
        'uid': app.config['MSSQL_UID'],
        'pwd': app.config['MSSQL_PWD'],
        'database': app.config['MSSQL_DATABASE']
    }
    
    connection = pyodbc.connect(**db_config)  
    cursor = connection.cursor()  
    query = ("SELECT @@version")  
    rows = [row for row in cursor.execute(query)]
    connection.close()  
    
    return rows[0][0].replace('\n\t', '<br>')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
