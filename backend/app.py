from flask import Flask
from flask_cors import CORS
from logging import getLogger
from os import environ
from blueprints.authentication import blueprint as authn_blueprint
from blueprints.errors.handlers import blueprint as errors_blueprint
import logging
FORMAT = '%(asctime)s | %(funcName)s | %(levelname)s | %(message)s'
app = Flask(__name__)
app.config['RESTPLUS_VALIDATE'] = True
CORS(app)
app.register_blueprint(authn_blueprint, url_prefix="/authn")
app.register_blueprint(errors_blueprint, url_prefix="/errors")

if environ.get("DEV", "0") == "1":
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    app.run(host="127.0.0.1", port=5000, debug=True)
else:
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    app.run(host="127.0.0.1", port=5000)
log = logging.getLogger(__name__)