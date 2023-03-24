import sqlite3

class DataBase:
    
    def __init__(self):
        self.connection = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("""CREATE TABLE users(id int, first_name TEXT, last_name TEXT, fullname TEXT, phone_number TEXT, address TEXT)""")
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
        
    
    def addUser(self, id, firstname, lastname, fname, number, address):
        sql = "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(sql, (id,firstname,lastname, fname, number, address))
        self.connection.commit()


    def get_info(self, id):
        sql = "SELECT * FROM users WHERE id=?"
        self.cursor.execute(sql, [(id)])
        data = self.cursor.fetchall()
        return data
    
    def updateFname(self, id, name):
        sql = "UPDATE users SET fullname = ? WHERE id = ?"
        self.cursor.execute(sql, (name, id))
        self.connection.commit()

    def updatePhone(self, id, number):
        sql = "UPDATE users SET phone_number = ? WHERE id = ?"
        self.cursor.execute(sql, (number, id))
        self.connection.commit()

    def updateAddress(self, id, address):
        sql = "UPDATE users SET address = ? WHERE id = ?"
        self.cursor.execute(sql, (address, id))
        self.connection.commit()

    



