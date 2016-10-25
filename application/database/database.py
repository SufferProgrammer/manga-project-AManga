import  sqlite3 as dbase
import hashlib
import os

class UserHandler():
    """handler for table user management in database"""
    def __init__(self):
        self.TemporaryDbPath = os.path.dirname(os.path.abspath(__file__))
        self.dbPath = os.path.join(self.TemporaryDbPath, 'database/database.db')
        self.database = dbase.connect(self.dbPath)
        self.cursor = self.database.cursor()
        
    def commit(self):
        """committer function"""
        self.database.commit()
        
    def exit(self):
        """closing database connection"""
        self.database.close()
        
    def exec(self, command):
        """command for execute sql query"""
        self.cursor.execute(command)
        
    def insertUser(self, username, password, email, user_image, level, status, join_date):
        """inserting user status to database"""
        converted = bytes(password, 'utf-32')
        SHA512protector = hashlib.sha512(converted).hexdigest()
        command = 'INSERT INTO user(username, password, email, user_image, u_level, u_status, u_join_date) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' %(username, SHA512protector, email, user_image, level, status, join_date)
        self.exec(command)
        self.commit()