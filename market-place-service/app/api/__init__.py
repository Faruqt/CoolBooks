from flask import Blueprint

mb = Blueprint('market', __name__)

from . import market
