from Database import dbhandler

test = dbhandler.DatabaseUserManager()

uname = 'piji'
password = 'piji'
email = 'pij@pij.com'
lvl = 1
sts = 0

# test.createUser(uname, password, email, lvl, sts)

uname2 = 'pijip'
passwd = 'piji2'
email2 = 'pasdasd@asd.asd'
# lvl2 = 1
# sts2 = 0
# test.createUser(uname2, passwd, email2, lvl2, sts2)

result = test.getUID(uname2, passwd)
# print(result)

test.deleteUser(result)