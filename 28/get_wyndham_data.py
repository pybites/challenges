import requests
import pandas as pd

URL = "https://data.gov.au/data/dataset/aa75879c-1d3e-4ad2-b331-826032c6b84b/resource/6e309687-023b-436b-9079-582b7e2fb074/download/wyndham-solar-energy-production.json"

r = requests.get(URL)

with open('wyndham_data.txt','w') as f:
    f.write(r.text)
    f.close