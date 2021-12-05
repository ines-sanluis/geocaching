from requests import Session
from bs4 import BeautifulSoup as bs
from os import environ
from logging import getLogger
from flask import Blueprint, request
from flask_restplus import Resource, Api, Namespace, fields
import json
from requests.exceptions import HTTPError, RequestException
from werkzeug.exceptions import HTTPException
from requests import ConnectionError

blueprint = Blueprint('authentication_blueprint', __name__)
api = Api(blueprint, title="Authentication endpoints")
auth_ns = Namespace('', "Authentication")
api.add_namespace(auth_ns, path="")

DOMAIN = environ.get("DOMAIN", "www.geocaching.com")
BASE_URL = f"https://{DOMAIN}"
logger = getLogger(__name__)
http_code_responses = {
    200: 'Success',
    400: 'Input Validation Error',
    500: 'Internal Server Error'
}
@auth_ns.route("/log-in")
class LogIn(Resource):
    user = api.model('User', {
        'username': fields.String,
        'password': fields.String(discriminator=True)
    })
    # @api.expect(user)
    @api.doc(body=user, responses=http_code_responses)
    def post(self):
        success = False
        input = json.loads(request.data.decode('UTF-8'))
        with Session() as session:
            success = log_in(session, input["username"], input["password"])
        return success

def log_in(session: Session, username: str, password: str) -> bool:
    url = f"{BASE_URL}/account/signin"
    success = False
    logger.debug(f"BEGIN - username {username}, password {password}")
    if not username or not password:
        error = "Invalid inputs"
        logger.error(f"{error} - username '{username}', password '{password}'")
        raise ValueError(error, 400)
    else:
        try:
            response = session.get(url)
        except RequestException as ex:
            raise RequestException("HOLA")
        #     logger.error("NEW")
        except OSError as ex:
            logger.error(type(ex))
        return
            # logger.error(f"Failed to connect {ex}")
            #raise Exception("Failed to connect")
        if not response.ok:
            logger.error(f"Failed to log in - {url}")
            raise HTTPException("MY EXCEPTION")
        token = get_token_from_html_markup(response.content)
        if not token:
            raise ValueError("Failed to log in")
        login_data = {
            "UsernameOrEmail": username,
            "Password": password, 
            "__RequestVerificationToken": token
        }
        response = session.post(url, login_data)
        if not response.ok:
            logger.error(f"Failed to log in - {url} {login_data}")
            raise HTTPException("MY EXCEPTION")
        success = True
    logger.debug(f"END - {'Success' if success else 'Failed'}")

def get_token_from_html_markup(markup: str) -> str:
    token = ""
    bs_content = bs(markup, "html.parser")
    token_input = bs_content.find("input", {"name": "__RequestVerificationToken"})
    if not token_input:
        logger.error("Received markup did not contain the expected tag <input name='___RequestVerificationToken'/>")
    token = token_input.get("value", "")
    if not token:
        logger.error(f"Input {token_input} did not have a valid value attribute")
    return token