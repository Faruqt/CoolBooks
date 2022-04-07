from . import ub
from ..models import User
from .. import db
from .errors import bad_request
from datetime import datetime, timedelta, timezone
from flask import make_response, request, jsonify
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
							   set_access_cookies, unset_jwt_cookies


@ub.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

@ub.route('/api/user/create', methods=['POST'])
def post_register():
    data = request.get_json()

    if data['username'] == '' or data['email'] == '' or data['password'] == '':
        return bad_request('Please make sure all fields are filled in correctly')
    if User.query.filter_by(email=data['email'].lower()).first():
        return bad_request('email address already registered')
    if User.query.filter_by(username=data['username'].lower()).first():
        return bad_request('username already exists')

    user = User()
    user.email = data['email']
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['username']
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    response = user.to_dict()
    status_code = 201

    return make_response(response, status_code)

@ub.route('/api/user/login', methods=['POST'])
def post_login():
    data = request.get_json() 
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user is not None and user.check_password(password):
        access_token = create_access_token(identity=email)
        return make_response(jsonify({'message': 'User logged in', 'access_token': access_token}))

    return make_response(jsonify({'message': 'User not logged in'}), 401)

@ub.route('/api/user/logout', methods=['POST'])
def post_logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response
