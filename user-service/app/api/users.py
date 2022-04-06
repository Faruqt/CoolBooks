from . import ub
from ..models import User
from .. import db
from .errors import bad_request
from flask import make_response, request, jsonify

@ub.route('/api/users', methods=['GET'])
def get_users():
    data = []
    for row in User.query.all():
        data.append(row.to_dict())

    response = jsonify(data)
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
    username = data['username']
    user = User.query.filter_by(username=username).first()
    if user:
        if sha256_crypt.verify(str(data['password']), user.password):
            user.encode_api_key()
            db.session.commit()
            login_user(user)

            return make_response(jsonify({'message': 'User logged in', 'api_key': user.api_key}))

    return make_response(jsonify({'message': 'User not logged in'}), 401)

@ub.route('/api/user/logout', methods=['POST'])
def post_logout():
    if current_user.is_authenticated:
        logout_user()
        return make_response(jsonify({'message': 'You are logged out'}))
    return make_response(jsonify({'message': 'You are not logged in'}))

# @login_required
# @ub.route('/api/user', methods=['GET'])
# def get_user():
#     if current_user.is_authenticated:
#         return make_response(jsonify({'result': current_user.to_json()}))

#     return make_response(jsonify({'message': 'Not logged in'})), 401

