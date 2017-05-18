# cf-conda-pyodbc
Using pyodbc on Cloud Foundry with Conda package manager

The app expects the following user-provided service to be running:

`cf cups mssql -p '{"server":"HOST","port":"PORT","uid":"UID","pwd":"PASSWORD","database":"DATABASE"}'`
