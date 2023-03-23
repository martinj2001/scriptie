import requests
from datetime import datetime

file_location = 'https://algoritmes.overheid.nl/api/file/algoritme'
date = datetime.today().strftime('%Y%m%d')
file_name = f'/Users/martin/projects/scriptie/backend/data/algoritmeregister_{date}.csv'

res = requests.get(file_location, allow_redirects=True)

file = open(file_name, 'wb')
file.write(res.content)
file.close()
