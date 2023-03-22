import sqlite3

class DataBase:
    
    def __init__(self):
        self.connection = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("""CREATE TABLE users(id int, first_name TEXT, last_name TEXT)""")
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
        
    
    def addUser(self, id, firstname, lastname):
        sql = "INSERT INTO users VALUES (?, ?, ?)"
        self.cursor.execute(sql, (id,firstname,lastname))
        self.connection.commit()


    def get_info(self, id):
        sql = "SELECT * FROM users WHERE id=?"
        self.cursor.execute(sql, [(id)])
        data = self.cursor.fetchall()
        return data



