from application.database.database import UserHandler
import time

jdate = time.strftime('%x')
test = UserHandler()
username = 'piji'
password = 'piji'
email = 'piji@pi.pi'
u_level = 1
u_status = 0
u_join_date = jdate

test.insertUser(username, password, email, u_level, u_status, u_join_date)

if test:
    print('okay desu... :3')
else:
    print('outo desu... x_x')