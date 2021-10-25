from flask import Blueprint, jsonify
from requests.exceptions import HTTPError, RequestException
from requests.sessions import Request
from werkzeug.exceptions import InternalServerError
blueprint = Blueprint('errors', __name__)


def get_response_body(error: str):
    return jsonify({"error": error})

@blueprint.app_errorhandler(ValueError)
def handle_value_error(ex):
    response = get_response_body(ex.args[0])
    if len(ex.args) == 2:
        response.status_code = ex.args[1]
    else:
        response.status_code = 500
    return response

@blueprint.errorhandler(InternalServerError)
def handle_http_error(ex):
    if len(ex.args) >= 1:
        response = get_response_body(ex.args[0])
    else:
        response = ""
    response.status_code = 500
    return response
    
@blueprint.errorhandler(RequestException)
def handle_http_error(ex):
    print("HOLAAAAAA")
    if len(ex.args) >= 1:
        response = get_response_body(ex.args[0])
    else:
        response = ""
    response.status_code = 500
    return response