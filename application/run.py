from application.database import database
from werkzeug import secure_filename
from flask import *
import os
import time

UPLOAD_FOLDER = 'assets/image/user'
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/API/<api_key>')
def responseAPI(api_key):
    
    apiResponseOk = [{
        'Response Status' : 'OK',
        'Response Code' : 200
    }]
    apiResponseError = [{
        'Response Status' : 'Undefined Error'
    }]
    
    apiAuthKey = ('5C3D8FB361F9F868E5252A76D9484')
    if api_key == apiAuthKey:
        return jsonify({'Response': apiResponseOk}), 200
    else:
        return jsonify({'Response' : apiResponseError}), 403
    
@app.errorhandler(404)
def errorpage(e):
    page = 'Not Found'
    return render_template('error.html', page = page), 404

@app.errorhandler(403)
def forbiddenpage(e):
    return redirect(url_for('index'))

@app.route('/join', methods = ['GET', 'POST'])
def join():
    page = 'Register New Admin'
    if request.method == 'POST':
        level = 2
        status = 0
        date = time.strftime('%x')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        profImgPath = request.form.get('fileImgName')
        imgPath = 'assets/image/user/%s' %(profImgPath)
        image = request.files['image']
        if image and allowed_file(image.filename):
            fileimage = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], fileimage))
            dbMgr = database.UserHandler()
            dbMgr.insertUser(username, password, email, imgPath, level, status, date)
            return redirect(url_for('index'))
    return render_template('join.html', page = page)
    

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
    return render_template('index.html', page = page, image = image)

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

@app.route('/admin/list')
def adminlist():
    page = 'Admin list'
    image = 'images/web/dev4.jpg'
    return render_template('adminlist.html', page = page, image = image)

if __name__=='__main__':
    app.run(debug=True)