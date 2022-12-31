# Script to create the data access object and interact with the database

# Import libaries and config file
import mysql.connector 
import dbconfig as cfg


# Add your own details here to connect to the database and get a cursor
class BookmarkDAO:
    connection=''
    cursor=''
    host=''
    user=''
    password=''
    database=''
        
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']


    # Function to connect to the database
    def getcursor(self): 
        self.connection = mysql.connector.connect(
        host=       self.host,
        user=       self.user,
        password=   self.password,
        database=   self.database,
        )

        self.cursor = self.connection.cursor()
        return self.cursor


    # Function to close connection
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

  
    # Function to register a user
    def register(self, account):
        print(account)     
        cursor = self.getcursor()

        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
        values = [
            account["username"], 
            account["email"],
            account["password"]
        ]
    
        cursor.execute(sql,values)
        self.connection.commit()
        print ("user registered")
        return 1  
        
          
   
    # Function to log a user in
    def login(self, account):
        cursor = self.getcursor()
        sql = "SELECT username, password FROM users WHERE username = %s"
        values = [account["username"]]      
        cursor.execute(sql,values)
        data = cursor.fetchone()
        print(data)
        
        # If no username or password
        if data[0] == "" and data[1]=="":
            print("User not found")
            return 0
        else: # Checking the password matches the username
            if account["password"] == data[1]:
                print("Logged in")
                return 1
            else:
                print("Password is incorrect")
                return 0
        #self.closeAll()            
        


    # Function to return user for given id
    def findUserByID(self, userId):
       cursor = self.getcursor()
       sql = 'select * from users where user_id = %s'
       values = [userId]
       cursor.execute(sql, values)
       result = cursor.fetchone()
       user = self.convertUserToDict(result)
       cursor.close()
       return user


    
    # Function to get all users
    def getAllUsers(self):
        cursor = self.getcursor()     
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()
        return_arr = [] # Empty array to store the data from the dict
        
        for r in result:
            result_as_dict = self.userDict(r)
            return_arr.append(result_as_dict)     
        self.closeAll()
        return return_arr


    
    # Function to convert getAllUsers response to a dict
    def userDict(self,result):
        colnames = ["id","username","email", "password"]
        bookmark= {}

        if result:
            for c, col_name in enumerate(colnames):
                value = result[c]
                bookmark[col_name] = value
        return bookmark



    # Function to create a bookmark
    def createBookmark(self, bookmark):
        print(bookmark) 
        cursor = self.getcursor()

        sql = "INSERT INTO bookmarks(url, description, category, username) VALUES (%s,%s,%s,%s)"
        values = [
            bookmark["url"],
            bookmark["description"],
            bookmark["category"],
            bookmark["username"],
        ]  

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return cursor.lastrowid # Next id
        
        

    # Function to get all bookmarks
    def getAllBookmarks(self):
        cursor = self.getcursor()     
        sql = "SELECT * FROM bookmarks"
        cursor.execute(sql)
        result = cursor.fetchall()
        return_arr = [] # Empty array to store the data from the dict
        
        for r in result:
            result_as_dict = self.convert_to_dict(r)
            return_arr.append(result_as_dict)     
        self.closeAll()
        return return_arr
       


    # Function to convert getAllBookmarks response to a dict
    def convert_to_dict(self,result):
        colnames = ["id","url","description","category", "created", "username"]
        bookmark= {}

        if result:
            for c, col_name in enumerate(colnames):
                value = result[c]
                bookmark[col_name] = value
        return bookmark



    # Function to get a bookmark by id
    def bookmarkById(self,id):
        cursor = self.getcursor()
        
        sql = "SELECT * FROM bookmarks WHERE id = %s"
        values = (id,)

        cursor.execute(sql,values)
        result = cursor.fetchone()
        #self.closeAll()
        return self.convert_to_dict(result)
        


    # Function to get bookmarks by category
    def getCategory(self, category):
      cursor = self.getcursor()

      sql = "SELECT * FROM bookmarks WHERE category = %s"
      values = (category, )

      cursor.execute(sql, values)
      result = cursor.fetchall()
      allBookmarks = []

      for bookmarks in result:
          resultDict = self.convert_to_dict(bookmarks)
          allBookmarks.append(resultDict)     
      self.closeAll()
      return allBookmarks



    # Function to get bookmarks by a user
    def getUserBookmarks(self, username):
      cursor = self.getcursor()
      sql = "SELECT * FROM bookmarks WHERE username = %s"
      values = (username, )
      cursor.execute(sql, values)
      result = cursor.fetchall()
      allBookmarks = []
      for bookmarks in result:
          resultDict = self.convert_to_dict(bookmarks)
          allBookmarks.append(resultDict)     
      self.closeAll()
      return allBookmarks



    # Function to update bookmark
    def updateBookmark(self, bookmark):
        cursor = self.getcursor() 
        sql = "UPDATE bookmarks SET url = %s, description = %s, category = %s WHERE username = %s"
        values = [
            bookmark[0], 
            bookmark[1],
            bookmark[2], 
            bookmark[3]
        ]  

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()


    
    # Function to delete a bookmark
    def deleteBookmark (self, id):
        cursor = self.getcursor()

        sql = "DELETE FROM bookmarks WHERE id = %s"
        values = (id,)

        cursor.execute(sql,values)
        self.connection.commit()
        self.closeAll()
        return {}



# Data Access Object   
bookmarkDAO = BookmarkDAO()

if __name__ == "__main__":
    print('running')

 
    ###### TEST DATA ######
    
    ###### USERS ######
    #user = {"username":"mulder", "email":"spooky@fbi.com", "password": "aliens"}
    #user2 = {"username":"scully", "email":"scully@fbi.com", "password":"sigh"}
    #user3 = {"username":"katie", "email":"g00398279@atu.ie", "password": "password"}
    
    #bookmarkDAO.register(user)
    #bookmarkDAO.register(user2)
    #bookmarkDAO.register(user3)
 
   
    ###### PROJECT REFERENCES ADDED TO DATABASE ######
    #data = {"url":"https://www.space.com/ufos-101-hype-uproar-disinformation-mystery","description":"the truth is out there", "category":"space", "username":"mulder"}
    #data2 = {"url":"https://www.skeptic.com/skepticism-101/", "description":"sure fine whatever", "category":"debunk", "username":"scully"}
    #data3 = {"url":"https://vlegalwaymayo.atu.ie/course/view.php?id=6209", "description": "Beatty A. Data Representation [Internet]. 2022.", "category":"reference", "username":"katie"}
    #data4 = {"url":"https://stackoverflow.com/questions/635937/how-do-i-specify-unique-constraint-for-multiple-columns-in-mysql", "description":"How do I specify unique constraint for multiple columns in MySQL? [Internet]. Stack Overflow.", "category":"reference", "username":"katie"}  
    #data5 = {"url":"https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb", "description":"Venkatesan N. Create and deploy a simple web application with flask and heroku [Internet]. Towards Data Science.", "category":"reference", "username":"katie"}  
    #data6 = {"url":"https://stackoverflow.com/questions/50979667/python-attributeerror-str-object-has-no-attribute-decode","description":"Python AttributeError: “str” object has no attribute “decode” [Internet]. Stack Overflow.", "category":"reference", "username":"katie"}      
    #data7 = {"url":"https://stackoverflow.com/questions/10496748/how-to-read-windows-environment-variable-value","description":"How to read Windows environment variable value? [Internet]. Stack Overflow.", "category":"reference", "username":"katie"}
    #data7 = {"url":"https://codingyaar.com/responsive-bootstrap-navbar-with-logo-centered-above-navbar/","description":"Git. Bootstrap Navbar with logo centered above navbar [Internet]. Coding Yaar. 2020", "category":"reference", "username":"katie"} 
    #data8 = {"url":"https://www.youtube.com/watch?v=5ud9Y2uB4PY", "description":"Framework. How to fix Import could not be resolved from source Pylance [Internet]. Youtube", "category":"reference", "username":"katie"} 
    #data9 = {"url":"https://cdn.pixabay.com/photo/2020/04/26/01/34/books-5093228_960_720.png", "description":"Pixabay.com", "category":"image reference", "username":"katie"}
    #data10 = {"url":"https://pixabay.com/photos/books-bookstore-book-reading-1204029/","description":"Pixabay.com.", "category":"image reference", "username":"katie"}
    #data11 = {"url":"https://www.w3schools.com/howto/howto_js_filter_table.asp", "description":"How to create a filter/search table [Internet]. W3schools.com.", "category":"reference", "username":"katie"}
    #data12 = {"url":"https://stackoverflow.com/questions/24627075/jquery-ajax-url-path-issue", "description":"Jquery Ajax url path Issue [Internet]. Stack Overflow.", "category":"reference", "username":"katie"}
    
    #bookmarkDAO.createBookmark(data)
    #bookmarkDAO.createBookmark(data2)
    #bookmarkDAO.createBookmark(data3)
    #bookmarkDAO.createBookmark(data4)
    #bookmarkDAO.createBookmark(data5)
    #bookmarkDAO.createBookmark(data6)
    #bookmarkDAO.createBookmark(data7)
    #bookmarkDAO.createBookmark(data8)
    #bookmarkDAO.createBookmark(data9)
    #bookmarkDAO.createBookmark(data10)
    #bookmarkDAO.createBookmark(data11)
    #bookmarkDAO.createBookmark(data12)
