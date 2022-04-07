from flask import Blueprint

ub = Blueprint('users', __name__)

from . import users, auth
