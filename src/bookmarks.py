from flask import Blueprint, request, jsonify
import validators
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.variables.http_status_codes import *
from src.database import Bookmark, db


# Setting url
bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/bookmarks")


# Create a book mark/return bookmarks for user
@bookmarks.route("/", methods=['POST', 'GET'])

def post_bookmark():
   

    if request.method == 'POST':

        description = request.get_json().get('description', '')
        url = request.get_json().get('url', '')

        if not validators.url(url):
            return jsonify({'error': 'invaild url'}), HTTP_400_BAD_REQUEST

        if Bookmark.query.filter_by(url=url).first():
            return jsonify({'error': 'url already exists'}), HTTP_409_CONFLICT


        bookmark = Bookmark(url=url, description=description)
        db.session.add(bookmark)
        db.session.commit()

        return jsonify({'id': bookmark.id,'url': bookmark.url,'visit': bookmark.visited,'description': bookmark.description,
            'created': bookmark.created,'updated': bookmark.updated,}), HTTP_201_CREATED

    else:

       

        data = []
        for bookmark in bookmarks:
            data.append({"id":bookmark.id, "description":bookmark.description, "url": bookmark.url, "created":bookmark.created, 
        "updated":bookmark.updated, "visits":bookmark.visited})

        return jsonify({"data":data}), HTTP_200_OK



# Get one bookmark
@bookmarks.get("/<int:id>")

def get_one(id):


    bookmark = Bookmark.query.filter_by( id=id).first()

    if not bookmark:
        return jsonify({'message': "bookmark not found"}), HTTP_404_NOT_FOUND

    return jsonify({"id":bookmark.id, "description":bookmark.description, "url": bookmark.url, "created":bookmark.created, 
        "updated":bookmark.updated, "visits":bookmark.visited}), HTTP_200_OK



# Update bookmark
@bookmarks.put('/<int:id>')


def update_bookmark(id):


    bookmark = Bookmark.query.filter_by(id=id).first()

    if not bookmark:
        return jsonify({'message': 'bookmark not found'}), HTTP_404_NOT_FOUND

    description = request.get_json().get('description', '')
    url = request.get_json().get('url', '')

    if not validators.url(url):
        return jsonify({'error': 'invalid url'}), HTTP_400_BAD_REQUEST

    bookmark.url = url
    bookmark.description = description

    db.session.commit() 


    return jsonify({'id': bookmark.id,'url': bookmark.url,'visit': bookmark.visited,'description': bookmark.description,
            'created': bookmark.created,'updated': bookmark.updated,}), HTTP_200_OK


# Delete bookmark
@bookmarks.delete('/<int:id>')

def delete_bookmark(id):


    bookmark = Bookmark.query.filter_by(id=id).first()

    if not bookmark:
        return jsonify({'message': 'bookmark not found'}), HTTP_404_NOT_FOUND


    db.session.delete(bookmark)
    db.session.commit()

    return jsonify({"message": "bookmark deleted"})