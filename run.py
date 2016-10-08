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
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/build')
def buildup():
    return 'Under Building'

if __name__=='__main__':
    app.run()