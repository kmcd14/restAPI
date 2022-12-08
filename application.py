from flask import Flask, jsonify, abort

app = Flask(__name__, static_url_path='', static_folder='static')


bookmarks = [
    {'name':'www.twitter.com'},
    {'name':'www.google.com'},
    {'name':'www.github.com'},
    ]


# Homepage
@app.route('/')
def homepage():
    return jsonify({'message': 'home'})


# Get bookmarks
@app.route("/bookmarks", methods=['GET'])
def getAllBookmarks():
        return jsonify(bookmarks)


# Delete 
@app.route('/vote/all', methods=['DELETE'])
def deleteBookmark():
    return jsonify({'done':True})



if __name__ == "__main__":
  app.run(debug=True)