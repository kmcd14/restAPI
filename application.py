# Import libaries, database config file and DAO from seprate files
from flask import Flask, jsonify, abort, request, session
from bookmarksDAO import bookmarkDAO
import dbconfig 

   

# Creating the Flask and setting secret key for session
app = Flask(__name__, static_url_path='', static_folder='static_pages')
app.config['SECRET_KEY'] = 'secret'


# ############################################################################


# Homepage route
@app.route('/')
def index():
    if not 'username' in session:
        return app.send_static_file('/index.html')



# Login 
@app.route("/login", methods = ["POST"])
def login():

    if request.method == "POST":
        account = {
            "username":request.json["username"],
            "password":request.json["password"]       
        }

    session['username'] = account["username"]

    return jsonify(bookmarkDAO.login(account))



# Logout 
@app.route("/logout", methods = ["POST"])
def logout():
    session.pop("username", None)

    return app.send_static_file('index.html')
 


# Register a new user
@app.route('/register', methods = ["POST"])
def register():

    account = {
        "username":request.json["username"],
        "email":request.json["email"],
        "password":request.json["password"]
    }

    return jsonify(bookmarkDAO.register(account))
    


# Get all users 
# curl "http://127.0.0.1:5000/users"
@app.route("/users", methods=["GET"])
def getAllUsers():
    return jsonify(bookmarkDAO.getAllUsers())



# Get all bookmarks 
# curl "http://127.0.0.1:5000/bookmark"
@app.route("/bookmark", methods=["GET"])
def getAll():
    return jsonify(bookmarkDAO.getAllBookmarks())



# Find bookmark by id 
# curl "http://127.0.0.1:5000/bookmark/1"
@app.route("/bookmark/<int:id>")
def findById(id):
    current_bookmark = bookmarkDAO.bookmarkById(id)
    print(current_bookmark)
    return jsonify(current_bookmark)



# Create a bookmark
# curl -i -H "Content-Type:application/json" -X POST -d "{\"url\":\"www.google.com\",\"description":\"google homepage\",\"category\":research}" http://127.0.0.1:5000/bookmark
@app.route("/bookmark", methods = ["POST"])
def create():

    if not request.json:
        abort(400)

    bookmark = {
        "url":request.json["url"],
        "description":request.json["description"],
        "category":request.json["category"],
        "username":request.json["username"]
    }

    return jsonify(bookmarkDAO.createBookmark(bookmark))



# Update bookmark
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"url\":\"www.google.com/images\",\"description\":\"updated from homepage to google images\",\"category\":images}" http://127.0.0.1:5000/bookmark/1
@app.route("/bookmark/<int:id>", methods = ["PUT"])
def update(id):
    foundBook = bookmarkDAO.bookmarkById(id)

    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)

    if 'url' in request.json:
        foundBook['url'] = request.json['url']
    if 'description' in request.json:
        foundBook['description'] = request.json['description']
    if 'category' in request.json:
        foundBook['category'] = request.json['category']

    values = (foundBook['url'], foundBook['description'], foundBook['category'], foundBook['username'])

    bookmarkDAO.updateBookmark(values)
    return jsonify(foundBook)
        


# Delete a bookmark
# curl -X DELETE http://127.0.0.1:5000/bookmark/1
@app.route("/bookmark/<int:id>", methods = ["DELETE"])
def delete(id):
    bookmarkDAO.deleteBookmark(id)
    return jsonify({"done":True})



# Find bookmark by category 
# curl "http://127.0.0.1:5000/bookmark/reference"
@app.route("/bookmark/<category>", methods=["GET"])
def getCategory(category):
    current_bookmark = bookmarkDAO.getCategory(category)
    print(current_bookmark)
    return jsonify(current_bookmark)



# Find bookmark by user
# curl "http://127.0.0.1:5000/katie"
@app.route("/<username>",methods=["GET"])
def UserBookmarks(username):
    current_bookmark = bookmarkDAO.getUserBookmarks(username)
    print(current_bookmark)
    return jsonify(current_bookmark)




if __name__ == '__main__' :
    app.run(debug= True)

    print('flask is running')