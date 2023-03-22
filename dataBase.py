import sqlite3

class DataBase:
    
    def __init__(self):
        self.connection = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("""CREATE TABLE users(id int)""")
            self.connection.commit()
        except:
            print("Already created!!")


    def checkUsernameExist(self, id):
        sql = "SELECT * FROM users WHERE id=?"
        self.cursor.execute(sql, [(id)])
        data = self.cursor.fetchone()
        if data is None:
            return False
        else:
            return True
        
    
    def addUser(self, id):
        sql = "INSERT INTO users VALUES (?)"
        self.cursor.execute(sql, [(id)])
        self.connection.commit()

