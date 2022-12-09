import mysql.connector
import dbconfig as cfg


class BookmarksDAO:
    connection= ""
    cursor = ""
    host = ""
    user = ""
    password = ""
    database = ""
    
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
         
    
    def create(self, values):
        pass
        '''
        cursor = self.getCursor()
        sql="insert into user (username, email, password) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
'''

    def getAll(self):
        pass 
    '''
        cursor = self.getCursor()
        sql="select * from user"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result
'''
    def findByID(self, id):
        pass
    '''
        cursor = self.getCursor()
        sql="select * from user where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result
'''
    def update(self, values):
        pass 
    '''
        cursor = self.getCursor()
        sql="update user set username= %s, email=%s, password=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        '''

    def delete(self, id):
        pass
    '''
        cursor = self.getCursor()
        sql="delete from user where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        #print("delete done")

'''


       

    def convertToDictionary(self, result):
        pass
    '''
        colnames=['id','title','author', "price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
       '''


    def createUserTable(self):
        pass
    '''
        cursor = self.getcursor()
        sql="CREATE TABLE User (user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username NOT NULL VARCHAR(50), email NOT VARCHAR(120), password VARCHAR(15))"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()
'''


    def createBookmarksTable(self):
        pass
        '''
        cursor = self.getcursor()
        sql="CREATE TABLE Bookmark (bookmark_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, url NOT NULL VARCHAR(500), description VARCHAR(200), category VARCHAR(30), user_id INT, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES User(user_id))"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()

        '''


    # Function to create the database   
    def createdatase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        
        self.cursor = self.connection.cursor()

        sql = "CREATE DATABASE IF NOT EXISTS datarep"

        #sql= "create database" + self.database
        self.cursor.execute(sql)
        print('created db')

        self.connection.commit()
        self.closeAll()
        

bookmarksDAO = BookmarksDAO()

if __name__ == "__main__":

    #Creating database
    bookmarksDAO.createdatase()
    #bookmarksDAO.createtable()

    print("code is working :)")