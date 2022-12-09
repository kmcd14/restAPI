import mysql.connector
import dbconfig as cfg
class UsersDAO:
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
         
    def create(self, values):
        
       cursor = self.getcursor()
       sql="insert into users (username ,email, password) values (%s,%s,%s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.closeAll()
       return newid
    

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
    
    def createUsersTable(self):
        cursor = self.getcursor()
        sql= "CREATE TABLE users (user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL, email VARCHAR(150) NOT NULL, password VARCHAR(15) NOT NULL, UNIQUE(username,email))"
        unique = "ALTER TABLE users ADD UNIQUE ('username', 'email');"
        cursor.execute(sql)
        #cursor.execute(unique)
        print('users table created')
        self.connection.commit()
        self.closeAll()
        
'''
    def createdatase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql="create database "+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()
       ''' 

userDAO = UsersDAO()

if __name__ == "__main__":

    # Create users table
    #userDAO.createUsersTable()

    data = ("test", "test@test.com", "test1234")
    userDAO.create(data)
    
    print("code is working")