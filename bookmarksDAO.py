# Script to create the data access object and interact with the database

# Import libaries and config file
import mysql.connector 
import dbconfig as cfg



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
        values = [
            account["username"],
            account["email"],
            account["password"],
        ]

        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
        cursor.execute(sql,values)
        self.connection.commit()
        print ("registered")
        self.closeAll()
        return 1
        
        
            
   
    # Function to log a user in
    def login(self, account):
        cursor = self.getcursor()
        values = [account["username"]]       
        sql = "SELECT username, password FROM users WHERE username = %s"
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
    def create_bookmark(self, bookmark):
        cursor = self.getcursor()
        sql = "INSERT INTO bookmarks( bookmarks.url, description, category) VALUES ( %s,%s,%s)"

        values = [
            bookmark["url"],
            bookmark["description"],
            bookmark["category"],
            ]  

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return cursor.lastrowid 
        

    # Function to get all bookmarks
    def get_all(self):
        cursor = self.getcursor()     
        sql = "SELECT * FROM bookmarks"
        cursor.execute(sql)
        result = cursor.fetchall()
        return_arr = []
        
        for r in result:
            result_as_dict = self.convert_to_dict(r)
            return_arr.append(result_as_dict)     
        self.closeAll()
        return return_arr
       

    # Function to convert response to a dict
    def convert_to_dict(self,result):
        colnames = ["id","url","description","category", "created"]
        bookmark= {}

        if result:
            for c, col_name in enumerate(colnames):
                value = result[c]
                bookmark[col_name] = value
        return bookmark



    # Function to get a bookmark by id
    def find_bookmark_by_id(self,id):
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
    def update_bookmark(self, bookmark):
        cursor = self.getcursor() 
        sql = "UPDATE bookmarks SET url = %s, description = %s, category = %s WHERE id = %s"
        #values = ("www.google.com/images", "google images", "research", "4")
        values = [bookmark[0],bookmark[1],bookmark[2], bookmark[3]]  

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        #return bookmark


    # Function to add a bookmark
    def add(self, bookmark):
        cursor = self.getcursor()
        sql = "INSERT INTO bookmarks(url, description, category, username) VALUES ( %s,%s,%s, %s)"
        values = [
            bookmark["url"],
            bookmark["description"],
            bookmark["category"],
            ]  
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return cursor.lastrowid 


    
    # Function to delete a bookmark
    def delete_bookmark (self, id):
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

    # Update user
    #data = ("catpig", "AAAAAAAAA", "research", 41)
    #bookmarkDAO.update_bookmark(data)

    #a = bookmarkDAO.find_bookmark_by_id(41)
    #print(a)

    # Create a bookmark
    #data = ("www.goggle.com", "google homepage", "research")
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