## Import libaries, database config file and DAO from seprate files
from flask import Flask, jsonify, abort, request, session
#from flask_session import Session   
from bookmarksDAO import bookmarkDAO
import dbconfig as cfg
import re

   

# Creating the Flask
app = Flask(__name__, static_url_path='', static_folder='static')

# secret_key for session
app.secret_key = 'hello'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#Session(app)


############################################################################


# Homepage route
@app.route('/')
def index():
    if not 'username' in session:
        return app.send_static_file('index.html')



# Login 
@app.route("/login", methods = ["POST"])
def login():

    if request.method == "POST":
        account = {
            "username":request.json["username"],
            "password":request.json["password"]       
        }

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

    if account:
        return jsonify({"message":"Account already exists"})

    elif not re.match(r'[^@]+@[^@]+\.[^@]+', account[1]):
        return jsonify({"message": "Invalid email address"})

    elif not account[0] or not account[2] or not account[1]:
        return jsonify({"message":"invaild entry"})
        
    else:
        return jsonify(bookmarkDAO.register(account))
    


# Get all bookmarks 
@app.route("/bookmark")
def getAll():
    #user_id = bookmarkDAO.findUserByID(id=user_id).first()
    return jsonify(bookmarkDAO.get_all())



# Find bookmark by id 
@app.route("/bookmark/<int:id>")
def findById(id):
    current_bookmark = bookmarkDAO.find_bookmark_by_id(id)
    print(current_bookmark)
    return jsonify(current_bookmark)



# Create a bookmark
@app.route("/bookmark", methods = ["POST"])
def create():

    if not request.json:
        abort(400)

    bookmark = {
        "url":request.json["url"],
        "description":request.json["description"],
        "category":request.json["category"]
        #"user_id": request.json("username")

    }
    return jsonify(bookmarkDAO.create_bookmark(bookmark))



# Update bookmark
@app.route("/bookmark/<int:id>", methods = ["PUT"])
def update(id):
    foundBook = bookmarkDAO.find_bookmark_by_id(id)
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

    values = (foundBook['url'],foundBook['description'],foundBook['category'],foundBook['id'])

    bookmarkDAO.update_bookmark(values)
    return jsonify(foundBook)
        



# Delete a bookmark
@app.route("/bookmark/<int:id>", methods = ["DELETE"])
def delete(id):

    bookmarkDAO.delete_bookmark(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)

    print('flask is running')