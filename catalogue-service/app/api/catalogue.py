from flask import jsonify, request, make_response
from .auth import UserClient
from . import cb
from .errors import bad_request, error_response
from ..models import Catalogue
from .. import db
from cloudinary.uploader import upload

@cb.route('/api/catalogue', methods=['GET'])
def catalogue_items():
    data = []
    for row in Catalogue.query.all():
        data.append(row.to_json())

    response = jsonify(data)
    return response

@cb.route('/api/catalogue/<id>', methods=['GET'])
def catalogue_item(id):
    book = Catalogue.query.filter_by(id=id).first_or_404()

    response = book.to_json()
    return response


@cb.route('/api/catalogue/create', methods=['POST'])
def catalogue_add_item():
    #confirm that token was added to the header
    api_key = request.headers.get('Authorization')
    if not api_key:
        return make_response(jsonify({'message': 'Please provide Authorization header '}), 401)
    
    #verify that user is logged in
    response = UserClient.get_user(api_key)
    if response == 'network error':
        return error_response(502, 'Error connecting to the user-service, confirm the service is running')
    if not response:
        return make_response(jsonify({'message': 'You are not logged in'}), 401)

    #get form data
    data = request.form.to_dict() or {}
    
    if 'file' not in request.files:
        return bad_request('Please add a cover image for the book')

    for field in ['title', 'author', 'desc']:
        if field not in data:
            return bad_request('Please make sure all fields are filled in correctly')

    if Catalogue.query.filter_by(book_title=data['title'].lower()).first():
        return bad_request('Book already exists in the catalogue')

    #call function to upload image to cloudinary
    book_image = request.files['file']
    image = upload_to_cloudinary(book_image)

    title = data['title'].lower()
    author = data['author']
    desc = data['desc']

    # create new book in the catalogue
    catalogue = Catalogue(book_title=title, author=author, 	
                            description=desc, cover_pic=image)

    db.session.add(catalogue)
    db.session.commit()

    response = {'result': catalogue.to_json()}
    return response


def upload_to_cloudinary(file_to_upload):
    # upload image to cloudinary
    upload_result = upload(file_to_upload, 
                            folder = "Catalogue/", 
                            public_id = file_to_upload.filename)

	# and then get the url for the transitioned uploaded file and store it in the database
    file= upload_result.get('secure_url')

    return file
