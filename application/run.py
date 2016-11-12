from werkzeug import secure_filename
from database import database
from flask import *
import datetime
import os


upload_path = os.path.dirname(os.path.abspath(__file__))


UPLOAD_FOLDER_USRIMAGE = os.path.join(upload_path, 'static/upload/image/user')
UPLOAD_FOLDER_PRIVIMAGE = os.path.join(upload_path, 'static/upload/image/prev')
UPLOAD_FOLDER_MANGA = os.path.join(upload_path, 'static/upload/image/user')
UPLOAD_FOLDER_VIDIO = os.path.join(upload_path, 'static/upload/vidio')

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg', 'mkv', 'mp3', 'rar', 'zip', '7zip', 'gz'])

app.secret_key = 'C538C57254494DE44733713D282AAF028851B92B5A5730D12B126312FB975237824AABDB972298F6F7D19F86694E81A3F8DAE62707374A31CA4D9F326B21B1D7'

app.config['UPLOAD_FOLDER_PRIVIMAGE'] = UPLOAD_FOLDER_PRIVIMAGE
app.config['UPLOAD_FOLDER_USRIMAGE'] = UPLOAD_FOLDER_USRIMAGE
app.config['UPLOAD_FOLDER_MANGA'] = UPLOAD_FOLDER_MANGA
app.config['UPLOAD_FOLDER_VIDIO'] = UPLOAD_FOLDER_VIDIO

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.before_request
def sessionPerma():
    Session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(hours=96)

#---------- API HANDLER AREA ----------------#

@app.route('/api/<api_key>')
def responseAPI(api_key):
    apiAuthKey = ('5C3D8FB361F9F868E5252A76D9484')
    if api_key == apiAuthKey:
        return jsonify({'Response': [{
            'Response Status': 'OK',
            'Response Code' : 200
        }]
        }), 200
    else:
        return jsonify({'Response' : [{
            'Response Status' : 'Forbidden',
            'Response Code' : 403
        }]
        }), 403

#---------- API HANDLER AREA ----------------#
#---------- ERROR HANDLER AREA ----------------#
    
@app.errorhandler(404)
def errorpage(e):
    page = 'Nani ?'
    return render_template('error.html', page = page), 404

@app.errorhandler(403)
def forbiddenpage(e):
    page = 'Stoooppuu !!'
    return render_template('dame.html', page = page), 403

#---------- ERROR HANDLER AREA ----------------#
#---------- COMMON HANDLER AREA ----------------#

@app.route('/join', methods = ['GET', 'POST'])
def join():
    page = 'Register New Admin'
    image = 'images/web/dev8.jpg'
    if request.method == 'POST':
        level = 2
        status = 0
        date = datetime.datetime.now()
        dateToday = date.strftime('%Y-%m-%d')
        username = request.form.get('username')
        password = request.form.get('password')
        passwordConfirm = request.form.get('confirm')
        email = request.form.get('email')
        profImgPath = request.form.get('fileImgName')
        imgPath = 'static/image/user/%s' %(profImgPath)
        dbMgr = database.UserHandler()
        imageSave = request.files['image']

        if passwordConfirm == password:
            if image and allowed_file(imageSave.filename):
                fileimage = secure_filename(imageSave.filename)
                pathSaveFile = os.path.join(app.config['UPLOAD_FOLDER_USRIMAGE'], fileimage)
                result = dbMgr.insertUser(username, password, email, imgPath, level, status, dateToday)
                if result == True:
                    imageSave.save(pathSaveFile)
                    stat = True
                    return render_template('join.html', page=page, status = stat, image = image)

                elif result == False:
                    stat = request.args.get('status', result)
                    return render_template('join.html', page=page, status = stat, image = image)
        elif password != passwordConfirm:
            stat = 'passAuthFail'
            return render_template('join.html', page=page, status=stat, image=image)
    return render_template('join.html', page = page, image = image)
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    image = 'images/web/dev2.jpg'
    if request.method == 'GET':
        whatToSearch = request.args.get('s')
        if whatToSearch == '':
            return redirect(url_for('index'))
        elif whatToSearch != None:
            page = 'Search'
            return render_template('search.html', result = whatToSearch, page = page, image = image)
        else:
            return redirect(url_for('index'))

@app.route('/')
def index():
    page = 'Index'
    image = 'images/web/dev1.jpg'
    stat = request.args.get('reg_status')
    return render_template('index.html', page = page, image = image, stat=stat)

@app.route('/anime')
def anime():
    page = 'Anime Session'
    image = 'images/web/dev5.jpg'
    return render_template('anime.html', page = page, image = image)

@app.route('/manga')
def manga():
    page = 'Manga Session'
    image = 'images/web/parallax2.jpg'
    return render_template('manga.html', page = page, image = image)

@app.route('/anime/latest')
def animlatest():
    page = 'Latest Anime'
    image = 'images/web/parallax.jpg'
    'Put something to make anime list is in sequence from latest update (this will go to database query)'
    return render_template('anime.html', page = page, image = image)

@app.route('/manga/latest')
def manglatest():
    page = 'Latest Manga'
    image = 'images/web/parallax.jpg'
    'Put something to make manga list is in sequence from latest update (this will go to database query)'
    return render_template('anime.html', page = page, image = image)

@app.route('/news')
def news():
    page = 'News Info'
    image = 'images/web/dev2.jpg'
    return render_template('news.html', page = page, image = image)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    page = 'Login'
    image = 'images/web/dev7.png'
    if request.method == 'POST':
        usernameOrEmail = request.form.get('UoE')
        password = request.form.get('pwd')
        login = database.UserHandler()
        result = login.getU_id(usernameOrEmail, password)
        if result != 0:
            databaseU_levelExamine = database.UserHandler()
            levelExamineResult = databaseU_levelExamine.userLevel(result)
            if levelExamineResult == 0:
                checkUserStatus = database.UserHandler()
                checkLogInStatus = session.get('username')
                if checkUserStatus.checkOnOffAdmin(result) == 0:
                    if checkLogInStatus == None:
                        session['username'] = usernameOrEmail
                        session['password'] = password
                        setOnStatus = database.UserHandler()
                        setOnStatus.userStatusOn(result)
                        return redirect(url_for('owner'))
                    elif checkLogInStatus != None:
                        return redirect(url_for('owner'))
                elif checkUserStatus.checkOnOffAdmin(result) == 1:
                    status = 'On'
                    return render_template('login.html', page=page, image=image, status=status)
            elif levelExamineResult == 2:
                checkUserStatus = database.UserHandler()
                checkLogInStatus = session.get('username')
                if checkUserStatus.checkOnOffAdmin(result) == 0:
                    if checkLogInStatus == None:
                        session['username'] = usernameOrEmail
                        session['password'] = password
                        setOnStatus = database.UserHandler()
                        setOnStatus.userStatusOn(result)
                        return redirect(url_for('admin'))
                    elif checkLogInStatus != None:
                        return redirect(url_for('admin'))
                elif checkUserStatus.checkOnOffAdmin(result) == 1:
                    status = 'On'
                    return render_template('login.html', page=page, image=image, status=status)
        else:
            status = int(0)
            return render_template('login.html', page=page, image=image, status = status)
    return render_template('login.html', page = page, image = image)

@app.route('/admin_dashboard')
def admin():
    if session.get('username') != None and session.get('password') != None:
        userLogin = session.get('username')
        password = session.get('password')
        checkStat = database.UserHandler()
        userId = checkStat.getU_id(userLogin, password)
        if checkStat.userLevel(userId) == 2:
            page = ('Osu %s') % userLogin
            return render_template('admin.html', page = page)
        elif checkStat.userLevel(userId) == 0:
            return redirect(url_for('owner'))
    else:
        abort(403)

@app.route('/mighty_owners')
def owner():
    if session.get('username') != None:
        page = 'Onii-chan Okaeiri :3'
        user = session.get('username')
        return render_template('owner.html', page = page, user = user)
    else:
        abort(403)

@app.route('/admin/list')
def adminlist():
    page = 'Admin list'
    image = 'images/web/dev4.jpg'
    adminList = database.UserHandler()
    examine = adminList.getAdminList()

    return render_template('adminlist.html', page = page, image = image, result = examine)

@app.route('/logout')
def logout():
    username = session.get('username')
    password = session.get('password')
    statusSetAndCheck = database.UserHandler()
    userTarget = statusSetAndCheck.getU_id(username, password)
    statusSetAndCheck.userStatusOff(userTarget)
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)