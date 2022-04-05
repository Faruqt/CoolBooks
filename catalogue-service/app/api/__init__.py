from flask import Blueprint

cb = Blueprint('catalogue', __name__)

from . import catalogue
