from . import ub
from ..models import User
from .errors import bad_request
from flask import make_response, request, jsonify
from flask_jwt_extended import jwt_required

@ub.route('/')
def user_service():
    response = "Welcome to Cool Books user service"
    return response

@ub.route('/api/users', methods=['GET'])
@jwt_required()
def get_users():
    data = []
    for row in User.query.all():
        data.append(row.to_json())

    response = jsonify(data)
    return response

@ub.route('/api/user/<username>', methods=['GET'])
@jwt_required()
def get_user(username):

    user = User.query.filter_by(username=username).first_or_404()

    response = user.to_json()
    return response


