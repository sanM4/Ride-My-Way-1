from flask import Flask

app = Flask(__name__)

from APP.API import Bluep as api_bluep

app.register_blueprint(api_bluep, url_prefix='/api/v1')
