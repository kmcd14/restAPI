import mysql.connector 
import dbconfig as cfg


class BookmarkDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
        
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']


    def getcursor(self): 
        self.connection = mysql.connector.connect(
        host=       self.host,
        user=       self.user,
        password=   self.password,
        database=   self.database,
        )

        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()


 


 




    # method to register bookmark
    # param : JSON : info taken from HTML form - url, username and password
    def register(self, register_data):
        print(register_data)     
        cursor = self.getcursor()
        values = [
            register_data["username"],
            register_data["email"],
            register_data["password"],
        ]

        
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
        cursor.execute(sql,values)
        self.connection.commit()
        print ("JOB DONE")
        self.closeAll()
        return 1
        
        
            
    # method to login 
    # param : JSON : login data (username, password)
    def login(self, login_data):
        cursor = self.getcursor()
        values = [login_data["username"]]       
        sql = "SELECT username, password FROM users WHERE username = %s"
        cursor.execute(sql,values)
        data = cursor.fetchone()
        print(data)
          
        if data[0] == "" and data[1]=="":
            print("Not Found")
            return 0
        else:
            if login_data["password"] == data[1]:
                print("logged in")
                return 1
            else:
                print("Wrong Password")

                return 0
        #self.closeAll()            
        

    # Return user for given userID
    def findUserByID(self, userId):
       #db = self.getConnection()
       cursor = self.getConnection()
       sql = 'select * from users where user_id = %s'
       values = [userId]
       cursor.execute(sql, values)
       result = cursor.fetchone()
       user = self.convertUserToDict(result)
       cursor.close()
       return user







    # method to create bookmark
    # param : JSON : bookmark information (name, description, category)
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
        

    # method to display all bookmarks in HTML table
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
       

    # method to convert to dictionary
    def convert_to_dict(self,result):
        colnames = ["id","url","description","category", "created", "user_id"]
        bookmark= {}

        if result:
            for c, col_name in enumerate(colnames):
                value = result[c]
                bookmark[col_name] = value
        return bookmark

    # method to find bookmark by its id 
    def find_bookmark_by_id(self,id):
        cursor = self.getcursor()
        
        sql = "SELECT * FROM bookmarks WHERE id = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchone()
        #self.closeAll()
        return self.convert_to_dict(result)
        
        

    # method to update bookmark data in MySQL table 
    def update_bookmark(self, bookmark):
        cursor = self.getcursor()
            
        sql = "UPDATE bookmarks SET url = %s, description = %s, category = %s WHERE id = %s"

        #values = ("www.pigsandcats.com", "google images", "research", "4")
        values = [bookmark[0],bookmark[1],bookmark[2], bookmark[3]]  


        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        #return bookmark


    def add(self, id, bookmark):
        cursor = self.getcursor()
        sql = "INSERT INTO bookmarks(bookmarks.url, description, category, username) VALUES ( %s,%s,%s, %s)"
        values = [
            bookmark["url"],
            bookmark["description"],
            bookmark["category"],
            bookmark["user_id"]
            ]  
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return cursor.lastrowid 



        
    
    # method to remove bookmark from database
    def delete_bookmark (self, id):

        cursor = self.getcursor()
        sql = "DELETE FROM bookmarks WHERE id = %s"
        values = (id,)
        cursor.execute(sql,values)
        self.connection.commit()
        self.closeAll()
        return {}
        
        
bookmarkDAO = BookmarkDAO()

if __name__ == "__main__":
    print('ughhhhhhhhhhhhhh')

 # Update user
    data = ("catpig", "AAAAAAAAA", "research", 41)
    bookmarkDAO.update_bookmark(data)

    a = bookmarkDAO.find_bookmark_by_id(41)
    print(a)