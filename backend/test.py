from requests import Session
from bs4 import BeautifulSoup as bs
import json
from lib.logger import EEL

domain = "www.geocaching.com"
url_site = "https://"+domain

def main():
    with Session() as s:
        result = log_in(s, "ogolpe", "unraposo")

@EEL("Log In")
def log_in(session, username, password):
    url = url_site+"/account/signin"
    site = session.get(url)
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name": "__RequestVerificationToken"})["value"]
    login_data = {
        "UsernameOrEmail": username,
        "Password": password, 
        "__RequestVerificationToken": token
    }
    page = session.post(url, login_data)
    soup = bs(page.content, 'html.parser')
    return soup

def get_logged_visits(session, link):
    result = {
        "total": 0,
        "detail": []
    }
    page = session.get(url_site+link)
    soup = bs(page.content, "html.parser")
    total = soup.find("p", {"class":"LogTotals"})
    for index, tag in enumerate(list(total)):
        if index % 2:
            value = int(tag.replace(",", "").replace(".", ""))
            result["total"] += value
            result["detail"].append({
                "type": type,
                "value": value
            })
        else:
            type = tag["title"]
    return result

def get_my_caches(session):
    url = "https://www.geocaching.com/my/owned.aspx"
    page = session.get(url)
    soup = bs(page.content, "html.parser")
    table = soup.find("table", {"class":"MyOwnedCachesTable"})
    yours = table.find_all("tr", {"class": "UserOwned"})
    return yours

def format_my_caches(session, caches):
    result = []
    for cache in caches:
        cells = cache.find_all("td")
        description = cells[3]
        link = description.find("a", href=True)["href"]
        name = description.select("a span")[0].text
        code = description.find("span", {"class":"small"}).text.split("|")[1].strip()
        logged_visits = get_logged_visits(session, link)
        result.append({
            'link': link,
            'name': name,
            'id': code,
            'logged_visits': logged_visits
        })
    return result

def get_caches_yours(session, filename):
    caches = get_my_caches(session)
    caches = format_my_caches(session, caches)
    with open(filename, 'w') as f:
        f.write(f"[{','.join(str(caches))}]")
        
def print_to_file(filename, result):
    with open(filename, 'w') as f:
        f.write("{")
        for item in result:
            f.write(f"{item}")
        f.write("}")
if __name__ == "__main__":
    main()