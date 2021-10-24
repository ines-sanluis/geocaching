from requests import Session
from bs4 import BeautifulSoup as bs
from os import environ
from logging import getLogger

DOMAIN = environ.get("DOMAIN", "www.geocaching.com")
BASE_URL = f"https://{DOMAIN}"
logger = getLogger(__name__)

def log_in(session: Session, username: str, password: str) -> bool:
    url = f"{BASE_URL}/account/signin"
    success = False
    logger.debug(f"BEGIN - username {username}, password {password}")
    if username and password:
        try:
            site = session.get(url)
        except Exception as e:
            logger.exception(f"Exception encountered {e}")
        token = get_token_from_html_markup(site.content)
        login_data = {
            "UsernameOrEmail": username,
            "Password": password, 
            "__RequestVerificationToken": token
        }
        page = session.post(url, login_data)
        soup = bs(page.content, 'html.parser')
    else:
        logger.error(f"Invalid inputs {username}, {password}")
    logger.debug(f"END - {success}")
    return success

def get_token_from_html_markup(markup: str) -> str:
    bs_content = bs(markup, "html.parser")
    token_input = bs_content.find("input", {"name": "__RequestVerificationToken"})
    if not token_input:
        raise ValueError("Markup did not contain the expected html input tag with attribute name='___RequestVerificationToken'")
    if not "value" in token_input:
        raise ValueError("Input did not have value attribute") 
    return token_input["value"]