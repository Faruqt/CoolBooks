from flask import jsonify, request, make_response
from .auth import UserClient
from . import mb
from .errors import bad_request
from ..models import ExchangeRequest
from .. import db
from cloudinary.uploader import upload

@mb.route('/api/market/exchange', methods=['POST'])
def open_request():
    #confirm that token was added to the header
    api_key = request.headers.get('Authorization')
    if not api_key:
        return make_response(jsonify({'message': 'Please provide Authorization header '}), 401)
    
    #verify that user is logged in
    responder = UserClient.get_user(api_key)
    if responder == 'network error':
        return error_response(502, 'Error connecting to the user-service, confirm the service is running')
    if not responder:
        return make_response(jsonify({'message': 'You are not logged in'}), 401)

    user = responder['result']

    # #get form data
    data = request.form.to_dict() or {}
    
    if 'file' not in request.files:
        return bad_request('Please add a cover image for the book')

    for field in ['title', 'author', 'desc', 'type', 'wanted']:
        if field not in data:
            return bad_request('Please make sure all fields are filled in correctly')
    
    # #call function to upload image to cloudinary
    book_image = request.files['file']
    image = upload_to_cloudinary(book_image)

    uid = user['id']
    title = data['title']
    author = data['author']
    descr = data['desc']
    type = data['type']
    wanted = data['wanted']

    # create new book exchange request
    new_request = ExchangeRequest(book_title=title, author=author, 	
                                    user_id=uid, description=descr, 
                                    cover_pic=image, type=type,
                                    wanted_type=wanted)

    db.session.add(new_request)
    db.session.commit()

    response = {'result': new_request.to_json()}
    return response

@mb.route('/api/market/proposals', methods=['GET'])
def proposals():
    book_proposals = []
    matched = []

    #confirm that token was added to the header
    api_key = request.headers.get('Authorization')
    if not api_key:
        return make_response({'message': 'Please provide Authorization header '}, 401)
    
    #verify that user is logged in
    response = UserClient.get_user(api_key)
    if response == 'network error':
        return error_response(502, 'Error connecting to the user-service, confirm the service is running')
    if not response:
        return make_response({'message': 'You are not logged in'}, 401)

    user = response['result']

    # Get all user's open exchange requests that have not been matched yet 
    user_exchange_requests = ExchangeRequest.query.filter_by(user_id=user['id'], request_matched=False).all()

    # Get requests that match user's open exchange requests on the market
    for user_request in user_exchange_requests:
        request_type = ExchangeRequest.query.filter_by(type = user_request.wanted_type).all()
        for match in request_type:
            if match.to_json() not in book_proposals:
                book_proposals.append(match.to_json())

    if not book_proposals:
        response = {'message': 'No matching book request found'}
    else:
        response = {'matching proposals': book_proposals}

    return response


def upload_to_cloudinary(file_to_upload):
    # upload image to cloudinary
    upload_result = upload(file_to_upload, 
                            folder = "Market/", 
                            public_id = file_to_upload.filename)

	# and then get the url for the transitioned uploaded file and store it in the database
    file= upload_result.get('secure_url')

    return file
