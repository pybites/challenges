# RIPE NCC Request Tool

This script print table with all public prefixes that belong particular AS 
from AS pool managed by RIPE NCC(European Regional Internet Registries)

# Description

Written script make request to RIPE NCC DataBase(http://rest.db.ripe.net/)
and try to retrieve all public prefixes that belongs to public AS. If request 
return response with error script print 'Incorrect AS number' and empty table.
Database request in file request_db.by.
Parsing json output in file program.py

For pretty printing used module named tabulate
