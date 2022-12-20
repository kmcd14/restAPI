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
            account["password"],
        ]
        
        cursor.execute(sql,values)
        self.connection.commit()
        print ("user registered")
        self.closeAll()
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
            print("Not Found")
            return 0
        else: # Checking the password matches the username
            if account["password"] == data[1]:
                print("logged in")
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
       

    # Get bookmarks for a user (table join)
    def myBookmarks(self, username):
        cursor = self.getcursor()
        sql="select * from bookmarks inner join users ON bookmarks.username = users.username where users.username = %s"
        values = (username, )
        cursor.execute(sql, values)
        result = cursor.fetchall()
        return_arr = []
 
        for r in result:
            result_as_dict = self.convert_to_dict(r)
            return_arr.append(result_as_dict)     
        self.closeAll()
        return return_arr


    # Function to convert response to a dict
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
          resultDict = self.convertToDict(bookmarks)
          allBookmarks.append(resultDict)     
      self.closeAll()
      return allBookmarks


    # Function to update bookmark
    def updateBookmark(self, bookmark):
        cursor = self.getcursor() 
        sql = "UPDATE bookmarks SET url = %s, description = %s, category = %s WHERE username = %s"
        #values = ("www.google.com/images", "google images", "research", "dana_scully")
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
    print('ughhhhhhhhhhhhhh')


    ###### PROJECT REFERENCES ADDED TO DATABASE ######

    #data =("https://vlegalwaymayo.atu.ie/course/view.php?id=6209","Beatty A. Data Representation [Internet]. 2022.","Reference", "katie")
    #data1 = ("https://stackoverflow.com/questions/635937/how-do-i-specify-unique-constraint-for-multiple-columns-in-mysql","How do I specify unique constraint for multiple columns in MySQL? [Internet]. Stack Overflow.", "Reference", "katie")
    #data2 = ("https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb","Venkatesan N. Create and deploy a simple web application with flask and heroku [Internet]. Towards Data Science.","Reference", "katie")
    #data3 = ("https://stackoverflow.com/questions/50979667/python-attributeerror-str-object-has-no-attribute-decode","Python AttributeError: “str” object has no attribute “decode” [Internet]. Stack Overflow.","Reference", "katie")
    #data4 = ("https://stackoverflow.com/questions/10496748/how-to-read-windows-environment-variable-value","How to read Windows environment variable value? [Internet]. Stack Overflow.","Reference", "katie")
    #data5 = ("https://codingyaar.com/responsive-bootstrap-navbar-with-logo-centered-above-navbar/","Git. Bootstrap Navbar with logo centered above navbar [Internet]. Coding Yaar. 2020","Reference", "katie")
    #data6 = ("https://www.youtube.com/watch?v=5ud9Y2uB4PY","Framework. How to fix Import could not be resolved from source Pylance [Internet]. Youtube","Reference", "katie")
    #data7 = ("https://cdn.pixabay.com/photo/2020/04/26/01/34/books-5093228_960_720.png","Pixabay.com","Image Reference", "katie")
    #data8 = ("https://pixabay.com/photos/books-bookstore-book-reading-1204029/","Pixabay.com.","Image Reference", "katie")
    #data9 = ("https://www.w3schools.com/howto/howto_js_filter_table.asp","How to create a filter/search table [Internet]. W3schools.com.","Reference", "katie")
    
    #bookmarkDAO.createBookmark(data)
    #bookmarkDAO.createBookmark(data1)
    #bookmarkDAO.createBookmark(data2)
    #bookmarkDAO.createBookmark(data3)
    #bookmarkDAO.createBookmark(data4)
    #bookmarkDAO.createBookmark(data5)
    #bookmarkDAO.createBookmark(data6)
    #bookmarkDAO.createBookmark(data7)
    #bookmarkDAO.createBookmark(data8)
    #bookmarkDAO.createBookmark(data9)


    ########### TESTS #############

    # Update user
    #data = ("www.youtube.com", "AAAAAAAAA", "research", 4)
    #bookmarkDAO.updateBookmark(data)

    #a = bookmarkDAO.bookmarkById(4)
    #print(a)

    # Create a bookmark
    #data = ("www.goggle.com", "google homepage", "research", "dana_scully")
    #bookmarksDAO.createBookmark(data)

    # Get one bookmark
    #oneBookmark = bookmarksDAO.getOneBookmark(1)
    #print(oneBookmark)

    # Get all bookmarks
    #bookmarkCount = bookmarksDAO.getAllBookmarks()
    #print(bookmarkCount)

    # Update user
    #data = ("www.google.com/images", "google images", "research", 1)
    #bookmarksDAO.updateBookmark(data)

    # Delete user
    #bookmarksDAO.deleteUser(1)

    #user = ("gaga", "gaga@atu.ie", "password")
    #bookmarkDAO.register(user)

    #data10 = ("www.aliens.org", "the truth is out there", "outerspace 101", "fox_mulder")
    #bookmarkDAO.createBookmark(data10)