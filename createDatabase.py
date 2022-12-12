# Script to create the database and tables


import mysql.connector
import dbconfig as cfg


# Add your own details here to connect to the database and get a cursor
class DataRepDAO:
    connection= ""
    cursor = ""
    host = ""
    user = ""
    password = ""
    database = ""
    
    # Details from my config file
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    # Connecting to database
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    # Close connection
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
        self.connection.commit()
        print('database created')
        self.closeAll()
        

    
    # Create the users table
    def createUsersTable(self):
        cursor = self.getcursor()
        sql= "CREATE TABLE users (user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20) NOT NULL, email VARCHAR(150) NOT NULL, password VARCHAR(15) NOT NULL, UNIQUE (username, email))"
        cursor.execute(sql)
        self.connection.commit()
        print('bookmarks table created')
        self.closeAll()


    
    # Create the bookmarks table
    def createBookmarksTable(self):
        cursor = self.getcursor()
        sql= "CREATE TABLE bookmarks (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, url VARCHAR(500) NOT NULL, description VARCHAR(200), category VARCHAR(30), created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, user_id INT, UNIQUE (url), FOREIGN KEY(user_id) REFERENCES users(user_id))"
        cursor.execute(sql)
        self.connection.commit()
        print('bookmarks table created')
        self.closeAll()


# data access object
datarepDAO = DataRepDAO()

if __name__ == "__main__":

    #Creating database
    datarepDAO.createdatase()
    #print("database created")

    # Create database tables
    datarepDAO.createUsersTable()
    datarepDAO.createBookmarksTable()
    #print("tables created")

    #print("code is working :)")