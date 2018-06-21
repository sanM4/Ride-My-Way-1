from flask import Blueprint

Bluep = Blueprint('api', __name__)

from APP.API import routes
