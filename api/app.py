from flask import Flask
from flask_cors import CORS
from logging import getLogger
from os import environ
from bs4 import BeautifulSoup
import requests

logger = getLogger(__name__)
app = Flask(__name__)
CORS(app)

domain = "www.geocaching.com"
url_site = "https://"+domain

@app.route('/')
def main():
    with requests.Session() as s:
        page = requests.get('https://www.geocaching.com/geocache/GC949T0_a-mineiria-compostelana?guid=a1297718-49ad-4d5e-a782-323e756bcb93')
        #print(p.text)
        #base_page = s.get('https://www.geocaching.com/account/settings/profile')
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup)
        totals = soup.find('p', attrs={'class' : 'LogTotals'})
        print(totals)
    return '', 200


def generate_auth_data(s):
    s.get(url_site+"/account/signin")
    cookies = get_cookies(s.cookies)
    data = {
       "UsernameOrEmail": "ogolpe",
        "Password": "unraposo"
    }
    for cookie in cookies:
        data[cookie["name"]] = cookie["value"]
    return data


def get_cookies(cookiejar):
    cookies = []
    for cookie in cookiejar:
        if cookie.domain == domain:
            cookies.append({
                "name": cookie.name,
                "value": cookie.value
            })
    return cookies

if environ.get("DEV", "0") == "1":
    app.run(host="0.0.0.0", port=5000, debug=True)
else:
    app.run(host="0.0.0.0", port=5000)
