from flask import Blueprint, request, jsonify
import validators
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.variables.http_status_codes import *
from src.database import Bookmark, db


# Setting url
bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/bookmarks")


# Create a book mark/return bookmarks for user
@bookmarks.route("/", methods=['POST', 'GET'])
@jwt_required
def post_bookmark():
    current_user = get_jwt_identity()

    if request.method == 'POST':

        description = request.get_json().get('description', '')
        url = request.get_json().get('url', '')

        if not validators.url(url):
            return jsonify({'error': 'invaild url'}), HTTP_400_BAD_REQUEST

        if Bookmark.query.filter_by(url=url).first():
            return jsonify({'error': 'url already exists'}), HTTP_409_CONFLICT


        bookmark = Bookmark(url=url, description=description, user_id=current_user)
        db.session.add(bookmark)
        db.session.commit()

        return jsonify({'id': bookmark.id,'url': bookmark.url,'visit': bookmark.visited,'description': bookmark.description,
            'created': bookmark.created,'updated': bookmark.updated,}), HTTP_201_CREATED

    else:

        bookmarks = Bookmark.query.filter_by(user_id=current_user)

        data = []
        for bookmark in bookmarks:
            data.append({"id":bookmark.id, "description":bookmark.description, "url": bookmark.url, "created":bookmark.created, 
        "updated":bookmark.updated, "visits":bookmark.visited})

        return jsonify({"data":data}), HTTP_200_OK

