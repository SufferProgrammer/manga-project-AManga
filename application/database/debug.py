from application.database.database import UserHandler
import datetime
import time

yeah = UserHandler()

date = datetime.datetime.now()
dateToday = date.strftime('%Y-%m-%d')
username = 'owner'
password = 'keluargabasr3434'
email = 'oniioniichan@gmail.com'
image = ''
u_level = 0
u_status = 0
u_join_date = dateToday

# user = 'piji'
# passwd = 'rahmat hidayat piji pirma'
# mail = 'onii@mail.mail'
# img = 'just/imaginary/path'
# level = 1
# date = jdate

#
test = yeah.insertUser(username, password, email, image, u_level, u_status, u_join_date)

if test:
    print('okay desu... :3')
else:
    print('outo desu... x_x')

# uid = yeah.suspendUser(username, password, email)
# print(uid)
# result = test.checkUser(username, password, email)
# print(result)

# test = yeah.getU_id(username, password, email)
# update = yeah.updateUserInfoAdminLevel(user, passwd, mail, img, level, date, test)

testing = yeah.showUser()
for res in testing:
    print(res)
    
    
# 4a4245de9a620177c567d5fe2490c36dc1d824f5f4a564676fb6b34dfe66005deab74a553763c51b334344fdf723a49772e45241967364705562c02c22274173
# 4a4245de9a620177c567d5fe2490c36dc1d824f5f4a564676fb6b34dfe66005deab74a553763c51b334344fdf723a49772e45241967364705562c02c22274173