import requests
from datetime import datetime
import os.path

file_location = 'https://algoritmes.overheid.nl/api/file/algoritme'
date = datetime.today().strftime('%Y%m%d')
file_name = f'/Users/martin/projects/scriptie/backend/data/algoritmeregister_{date}.csv'
if(os.path.isfile(file_name)):
    exit()
    
res = requests.get(file_location, allow_redirects=True)

file = open(file_name, 'wb')
file.write(res.content)
file.close()
exit()