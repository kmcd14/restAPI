import mysql.connector
import dbconfig as cfg
#from usersDAO import users 


class BookmarksDAO:
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
         

    # Create a user     
    def createBookmark(self, values):
        
       cursor = self.getcursor()
       sql="insert into bookmarks (url, description, category) values (%s,%s,%s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       print('bookmark created')
       self.closeAll()
       return newid
    


    # Get all bookmarks in the bookmarks table
    def getAllBookmarks(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM bookmarks"
        cursor.execute(sql)
        result = cursor.fetchall()

        allBookmarks = []

        for bookmarks in result:
            resultDict = self.convertToDict(bookmarks)
            allBookmarks.append(resultDict)     

        self.closeAll()
        return allBookmarks


    # Find a bookmark by id
    def getOneBookmark(self, bookmark_id):
        cursor = self.getcursor()
        sql = "SELECT * FROM bookmarks WHERE bookmark_id = %s"
        values = (bookmark_id, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result



    # Get bookmarks by category
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


    # Get bookmarks by month
    def getDate(self, date):
        cursor = self.getcursor()
        sql = "SELECT * FROM bookmarks WHERE created = MONTH( %b)"
        #values = (date, )
        cursor.execute(sql, date)
        result = cursor.fetchall()

        allBookmarks = []

        for bookmarks in result:
            resultDict = self.convertToDict(bookmarks)
            allBookmarks.append(resultDict)     

        self.closeAll()
        return allBookmarks



    # Update bookmark
    def updateBookmark(self, values):
        cursor = self.getcursor()
        sql = "UPDATE bookmarks SET url = %s, description = %s, category = %s WHERE bookmark_id = %s"
        cursor.execute(sql, values)
        
        self.connection.commit()
        print("bookmark updated")
        self.closeAll()
        #return resultDict



    # Delete bookmark for given bookmark_id, returns empty dictionary/JSON
    def deleteBookmark(self, bookmark_id):
        cursor = self.getcursor()
        sql = 'DELETE FROM bookmarks WHERE bookmark_id = %s'
        values = [bookmark_id]
        cursor.execute(sql, values)
        self.connection.commit()
        print("bookmark deleted")
        self.closeAll()
        return {}





    # Convert returned sql query into a dict
    def convertToDict(self, result):
        colnames=['bookmark_id','url', 'description', 'category', 'created', 'user_id']
        allBookmarks = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                allBookmarks[colName] = value
        
        return allBookmarks
    


    
    # Find bookmark by id 
    def findUser(self, id):
        cursor = self.getcursor()
                
        sql = "SELECT * FROM bookmarks WHERE id = %s"
        values = [id]
        cursor.execute(sql,values)
        result = cursor.fetchall()
                    
        return self.convertToDict(result)











        





bookmarksDAO = BookmarksDAO()

if __name__ == "__main__":

    # Create bookmarks table
    bookmarksDAO.createBookmarksTable()

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



    print("code is working")