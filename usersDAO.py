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
         

    # Create a user     
    def createUser(self, values):
        
       cursor = self.getcursor()
       sql="insert into users (username ,email, password) values (%s,%s,%s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       print('user created')
       self.closeAll()
       return newid
    


    # Get all users in the users table
    def getAllUsers(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()

        allUsers = []

        for users in result:
            resultDict = self.convertToDict(users)
            allUsers.append(resultDict)     

        self.closeAll()
        return allUsers


    # Find a user by their user_id
    def getOneUser(self, user_id):
        cursor = self.getcursor()
        sql = "SELECT * FROM users WHERE user_id = %s"
        values = (user_id, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result



    # Update user
    def updateUser(self, values):
        cursor = self.getcursor()
        sql = "UPDATE users SET username = %s, email = %s, password = %s WHERE user_id = %s"
        cursor.execute(sql, values)
        
        self.connection.commit()
        print("user updated")
        self.closeAll()
        #return resultDict



    # Delete user for given user_id, returns empty dictionary/JSON
    def deleteUser(self, user_id):
        cursor = self.getcursor()
        sql = 'DELETE FROM users WHERE user_id = %s'
        values = [user_id]
        cursor.execute(sql, values)
        self.connection.commit()
        print("user deleted")
        self.closeAll()
        return {}





    # Convert returned sql query into a dict
    def convertToDict(self, result):
        colnames=['user_id','username','email', "password"]
        allUsers = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                allUsers[colName] = value
        
        return allUsers
    


    
    # Find user by user_id 
    def findUser(self, id):
        cursor = self.getcursor()
                
        sql = "SELECT * FROM users WHERE id = %s"
        values = [id]
        cursor.execute(sql,values)
        result = cursor.fetchall()
                    
        return self.convertToDict(result)




    # Create the users table
    def createUsersTable(self):
        cursor = self.getcursor()
        sql= "CREATE TABLE users (user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL, email VARCHAR(150) NOT NULL, password VARCHAR(15) NOT NULL, UNIQUE(username,email))"
        cursor.execute(sql)
        print('users table created')
        self.connection.commit()
        self.closeAll()
        






usersDAO = UsersDAO()

if __name__ == "__main__":

    # Create users table
    #usersDAO.createUsersTable()

    #data = ("test", "test@test.com", "test1234")
    #usersDAO.createUser(data)
    

    #oneUser = userDAO.getOneUser(1)
    #print(oneUser)

    #userCount = usersDAO.getAllUsers(1)
    #print(userCount)

    # Update user
    #data = ("UPDATEtest", "test@test.com", "test1234", 2)
    #usersDAO.updateUser(data)

    # Delete user
    #usersDAO.deleteUser(1)

    print("code is working")