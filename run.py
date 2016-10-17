from flask import *

app = Flask(__name__)

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
    page = 'Forbidden'
    return render_template('dame.html', page = page), 403

@app.route('/')
def index():
    page = 'Index'
    return render_template('index.html', page = page)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        whatToSearch = request.args.get('s')
        if whatToSearch == '':
            return redirect(url_for('index'))
        elif whatToSearch != None:
            page = 'Search'
            return render_template('search.html', result = whatToSearch, page = page)
        else:
            return redirect(url_for('index'))

@app.route('/anime')
def anime():
    page = 'Anime Session'
    return render_template('anime.html', page = page)

@app.route('/manga')
def manga():
    page = 'Manga Session'
    return render_template('manga.html', page = page)

@app.route('/build')
def buildup():
    return 'Under Building'

if __name__=='__main__':
    app.run(debug=True)