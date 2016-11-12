import pymysql as dbase
import hashlib

class UserHandler():
    """handler for table user management in database"""
    def __init__(self):
        self.database = dbase.connect(user = 'admin', host = 'localhost', database = 'amangaproject')
        self.cursor = self.database.cursor()
        
    def commit(self):
        """committer function"""
        self.database.commit()
                
    def execute(self, command):
        """command for execute sql query"""
        self.cursor.execute(command)
        
    def checkUser(self,u_id):
        """Return boolean if user id existed or not. this is for user existence checker"""
        command = 'SELECT * FROM user WHERE u_id = "%s"' %(u_id)
        self.execute(command)
        self.fetchId = self.cursor.fetchone()
        if self.fetchId:
            return True
        else:
            return False
        
        
    def getU_id(self, username, password):
        """Returning user id in integer"""
        passwd = password
        converted = bytes(passwd, 'utf-32')
        SHA512protector = hashlib.sha512(converted).hexdigest()
        command = 'SELECT u_id FROM user WHERE username = "%s" AND password = "%s"' %(username, SHA512protector)
        self.execute(command)
        self.resultRaw = self.cursor.fetchone()
        if self.resultRaw:
            self.result = int(''.join(map(str, self.resultRaw)))
            return self.result
        else:
            nodata = int(0)
            return nodata
            
    def insertUser(self, username, password, email, user_image, level, status, join_date):
        """create user and inserting user info to database if not exists"""
        converted = bytes(password, 'utf-32')
        SHA512protector = hashlib.sha512(converted).hexdigest()

        self.GID = self.getU_id(username, password)
        self.checkIfAvailable = self.checkUser(self.GID)
        
        if self.checkIfAvailable == False:
            command = 'INSERT INTO user(username, password, email, prof_img, user_level, user_status, join_date) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' %(username, SHA512protector, email, user_image, level, status, join_date)
            self.execute(command)
            self.commit()
            return True
            
        elif self.checkIfAvailable == True:
            return False
            
    def suspendUser(self, username, password):
        """Admin Function for suspending account"""
        self.targetForSuspend = self.getU_id(username, password)
        command = 'DELETE FROM user WHERE u_id = "%s" LIMIT 1' %(self.targetForSuspend)
        self.execute(command)
        self.commit()
        self.exitDatabase()
        
    def updateUserInfoAdminLevel(self, username, password, email, prof_img, user_level, join_date, userId):
        """Updating user info"""
        converted = bytes(password, 'utf-32')
        SHA512protector = hashlib.sha512(converted).hexdigest()
        
        command = 'UPDATE user SET username = "%s", password = "%s", email = "%s", prof_img = "%s", user_level = "%s", user_status = 0, join_date = "%s" WHERE u_id = "%s" LIMIT 1' %(username, SHA512protector, email, prof_img, user_level, join_date, userId)
        self.execute(command)
        self.commit()
        self.exitDatabase()
        
    def userLevel(self, U_id):
        """Sometime this function will be used"""
        command = 'SELECT user_level FROM user where u_id = "%s"' %(U_id)
        self.execute(command)
        self.resultRaw = self.cursor.fetchone()
        self.result = int(''.join(map(str, self.resultRaw)))
        return self.result

    def userStatusOn(self, U_id):
        command = 'UPDATE user SET user_status = 1 WHERE u_id = %s' %(U_id)
        self.execute(command)
        self.commit()
        self.exitDatabase()

    def userStatusOff(self, U_id):
        command = 'UPDATE user SET user_status = 0 WHERE u_id = %s' %(U_id)
        self.execute(command)
        self.commit()
        self.exitDatabase()

    def getAdminList(self):
        command = 'SELECT * FROM user'
        self.execute(command)
        self.result = self.cursor.fetchall()
        return self.result

    def checkOnOffAdmin(self, U_id):
        command = 'SELECT user_status FROM user WHERE u_id = %s' %(U_id)
        self.execute(command)
        self.resultRaw = self.cursor.fetchone()
        self.result = int(''.join(map(str, self.resultRaw)))
        return self.result

    def exitDatabase(self):
        """closing database connection"""
        self.database.close()


class contentHandler():
    def __init__(self):
        self.database2Connection = dbase.connect(user = 'admin', host = 'localhost', database = 'amangaproject')
        self.cursor = self.database2Connection.cursor()