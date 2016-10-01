import MySQLdb

class DatabaseUserManager():
    """this class is used to user management, I've been desaining this class for handling user management (tested)"""
    def __init__(self):
        self.database = MySQLdb.connect(host='pii-chan.tk', user='developer', db='fromphone')
        self.cursor = self.database.cursor()
    
    def commit(self):
        self.database.commit()

    def Query(self, command):
        self.cursor.execute(command)
        
    def getUID(self, uname, passwd):
        '''get user id with this function (tested)'''
        command = 'SELECT id FROM user WHERE username="%s" AND password="%s"' % (uname, passwd)
        self.Query(command)
        result = self.cursor.fetchone()
        return result
        
    def createUser(self, uname, passwd, email, ulvl, usts):
        '''create user in this function (tested)'''
        command = 'INSERT INTO user(username, password, email, user_level, user_status) VALUES("%s", "%s", "%s", "%s", "%s")' %(uname, passwd, email, ulvl, usts)
        self.Query(command)
        self.commit()
        
    def deleteUser(self, value):
        '''delete user in this function (tested)'''
        command = 'DELETE FROM user WHERE id="%s"' %(value)
        self.Query(command)
        self.commit()
        
    def adminUpdateUser(self, id, uname, passwd, email, ulvl, usts):
        '''admin level update user status in here, this function only for admin or user with higher level (untested yet)'''
        self.Query('UPDATE user SET username=%s, password=%s, user_level= %s, user_status=%s WHERE id=%s') %(uname, passwd, email, ulvl, usts, id)
        self.commit()
        
    def memberUpdateUser(self, id, uname, passwd, email):
        '''and in here is user level update user status, if you want user can update their info,
        this you must give this function. Dont ever give them admunUpdateUser level status (untested yet)'''
        self.Query('UPDATE user SET userame=%s, password=%s, email=%s WHERE id=%s') %(uname, passwd, email, id)
        self.commit()
        
        