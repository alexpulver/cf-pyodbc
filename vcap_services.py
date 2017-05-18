import json
import os


def get_config():
    config = {}

    vcap_services = os.environ.get('VCAP_SERVICES')
    if not vcap_services:
        return None

    vcap_services_obj = json.loads(vcap_services)
    for service in vcap_services_obj['user-provided']:
        if service['name'] == 'mssql':
            _update_mssql_config(config, service['credentials'])

    return config


def _update_mssql_config(config, credentials):
    config['MSSQL_SERVER'] = credentials['server']
    config['MSSQL_PORT'] = credentials['port']
    config['MSSQL_UID'] = credentials['uid']
    config['MSSQL_PWD'] = credentials['pwd']
    config['MSSQL_DATABASE'] = credentials['database']
