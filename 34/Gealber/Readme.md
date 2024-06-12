# Code Challenge fetcher
This is a simple API to fetch the Code challenges in codechalleng.es/challenges/.

Before using this __API__ you should run *fetcher.py*. This script will retrieve the current code challenges and store it in *db.sqlite3*.
## Endpoints

| Endpoint | Method | Info |
|----------|--------|------|
|/challenges| GET   |fetches all the availables challenges|
|/challenges/i/| GET | fetches the i-th challenge|

It would be nice the extend this idea for the pybites as well.
Maybe implement a __*cli*__ that would get the pybites available for
a current user, but for that we will need some kind of authorization.
