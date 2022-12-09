# Create the database and tables


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
         

     # Function to create the database   
    def createdatase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        
        self.cursor = self.connection.cursor()

        

        sql= "CREATE DATABASE IF NOT EXISTS " + self.database
        self.cursor.execute(sql)
        print('created db')

        self.connection.commit()
        self.closeAll()
        

bookmarksDAO = BookmarksDAO()

if __name__ == "__main__":

    #Creating database
    #bookmarksDAO.createdatase()

    # Create database tables
    #bookmarksDAO.createUsersTable()
    #bookmarksDAO.createBookmarksTable()
    

    print("code is working :)")