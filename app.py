from flask import Flask,redirect,send_from_directory,request
import uuid
dic = {}
app = Flask(__name__)

@app.route('/')
def hello_name():
   return app.send_static_file('index.html')
@app.route('/<keys>')
def open(keys):
	try:
		return redirect(f'{dic[keys]}')
	except KeyError:
		return 'No Key Found'

@app.route('/short/',methods = ['POST', 'GET'])
def random():
	if(request.method == 'POST'):
		key = str(uuid.uuid4())[0:5]
		dic[key] = request.get_data().decode("utf-8")
		yourhostname = ''
		return f'{yourhostname}/{key}'
	if(request.method == 'GET'):
		return 'Ughh Wrong Place :P Uh Can Use this as Api , Use Post request To This Endpoint'




app.run()
