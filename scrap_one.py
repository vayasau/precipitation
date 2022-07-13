# nuskaitomas paveiksliukas ir issaugomas atmintyje

import requests
from io import BytesIO


def web_image():
    file = BytesIO()
    r = requests.get('https://beta.meteo.lt/data/radar/radarlarge+36.gif')
    if r.status_code == 200:
        file.write(r.content)
        return file
