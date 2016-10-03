from flask import *


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/buildup')
def buildup():
	return "<h1><center>THIS PAGE IS UNDER CONSTRUCTION</center></h1>"
	

if __name__ =='__main__':

	app.run(host = '0.0.0.0', debug = True, port = 80)