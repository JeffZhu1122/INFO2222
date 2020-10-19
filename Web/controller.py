from bottle import *
import model
# import gevent.monkey
import collections
import datetime
from time import time
# from gevent import sleep
import os
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
password_check="http://"+config['WAF']['hostname']+":"+config['WAF']['port']+config['WAF']['route']+"/password/"
email_check="http://"+config['WAF']['hostname']+":"+config['WAF']['port']+config['WAF']['route']+"/email/"
string_check="http://"+config['WAF']['hostname']+":"+config['WAF']['port']+config['WAF']['route']+"/detect/"


skey="InF02222_k3Y_y0U_nEv3R_Kn0w"
######## Post Config ########

messages = collections.deque()

MESSAGE_TIMEOUT = 10
FLOOD_MESSAGES = 5
FETCH_FREQ = 1000
js = '''

'''
# gevent.monkey.patch_all()
MAX_UPLOADED = 100

######## Posts Class ########

class Message(object):
	def __init__(self, nick, text,title):
		self.time = time()
		self.nick = nick
		self.text = text
		self.title = title

	def json(self):
		return {'title': self.title,'text': self.text, 'nick': self.nick, 'time': self.time}

###### Posts ######
@get('/posts/api/info')
def on_info():
	return {
		'server_name': 'Bottle Test Chat',
		'server_time': time(),
		'refresh_interval': 1000
	}

@post('/posts/api/send_message')
def on_message():
	text = request.forms.get('text', '')
	title = request.forms.get('title', '')
	nick = request.forms.get('nick', '')
	if ':' in nick:
		nick, token = nick.split(':', 1)
	else:
		token = ''
	nick = nick.strip()
	if not text: return {'error': 'No text.'}
	if not title: return {'error': 'No title.'}
	timeout = time()-MESSAGE_TIMEOUT
	while messages and messages[0].time < timeout:
		messages.popleft()
	if len([m for m in messages if m.nick == nick]) > FLOOD_MESSAGES:
		return {'error': 'Messages arrive too fast.'}
	username = request.get_cookie("session",secret=skey)
	messages.append(Message(username, text,title))
	return {'status': 'OK'}

@get('/posts/api/fetch')
def on_fetch():
	since = float(request.params.get('since', 0))
	updates = [m.json() for m in messages if m.time > since]
	return { 'messages': updates[:10] }
######## Loader ########


# @route('/css/<path>')
# def css(path):
# 	return static_file(path, root='css')

# @route('/fonts/<path>')
# def css(path):
# 	return static_file(path, root='fonts')

# @route('/js/<path>')
# def js(path):
# 	return static_file(path, root='js')

# @route('/img/<path>')
# def js(path):
# 	return static_file(path, root='img')

# @route('/units/<path>')
# def js(path):
# 	return static_file(path, root='units')

# @route('/uploads/<path1>/<path2>')
# def js(path1, path2):
# 	return static_file(path2, root='uploads/'+path1)

# @route('/other_pdf/<path>')
# def js(path):
# 	return static_file(path, root='other_pdf')

# @route('/units-pdf/<path>')
# def js(path):
# 	return static_file(path, root='units-pdf')

# @route('/career/<path>')
# def js(path):
# 	return static_file(path, root='career')

# @route('/career-pdf/<path>')
# def js(path):
# 	return static_file(path, root='career-pdf')

######## Website pages ########

@route('/')
def index():
	username = request.get_cookie("session",secret=skey)
	if username:
		return redirect('/home')
	return template('index',user=None)

@route('/home')
def home():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	issuper=model.is_superuser(username)[0]==1
	return template('home',user=username,issuper=issuper)

@route('/profile')
def profile():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	info=model.get_user_info(username)
	issuper=info[5]==1
	return template('profile',user=username,info=info,issuper=issuper)

@route('/login',method=['POST', 'GET'])
def login():
	if(request.method == 'POST'):
		username=request.forms.get('username')
		username_valid=requests.post(string_check+username).text
		if username_valid!="True":
			return "not successful login"
		password=request.forms.get('password')
		login_return_data = model.check_login(username,password)
		if not login_return_data:
			return redirect('/login')
		response.set_cookie("session", username, secret=skey)
		return redirect('/home')
	elif(request.method == 'GET'):
		return template('login',user=None)

@route('/logout')
def logout():
	response.delete_cookie("session")
	return redirect('/')

@route('/register', method=['POST', 'GET'])
def register():
	username = request.get_cookie("session",secret=skey)
	if username:
		return redirect('/home')
	if(request.method == 'POST'):
		username=request.forms.get('username')
		username_valid=requests.post(string_check+username).text
		if username_valid!="True":
			return "not successful registration"
		password=request.forms.get('password')
		password_valid=requests.post(password_check+password).text
		if password_valid!="True":
			return "not successful registration"
		pass_check=request.forms.get('pass_check')
		email=request.forms.get('email')
		email_valid=requests.post(email_check+email).text
		if email_valid!="True":
			return "not successful registration"
		register_return_data = model.add_user(username,password,pass_check,email,datetime.datetime.now().strftime("%Y-%m-%d"))
		if register_return_data==-1:
			return "not successful registration"
		return redirect('/login')
	elif(request.method == 'GET'):
		return template('register',user=None)

@route('/posts')
def posts():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	issuper=model.is_superuser(username)[0]==1
	return template('posts',user=username,issuper=issuper)

@route('/message')
def message():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	issuper=model.is_superuser(username)[0]==1
	return template('message',user=username,issuper=issuper)

@route('/user-manage')
@route('/user-manage/delete/<user_id>')
def umanage(user_id="0"):
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	if user_id!="0":
		if model.is_superuser(username)[0]==1:
			model.delete_user(user_id)
			return redirect('/user-manage')
	else:
		if model.is_superuser(username)[0]==1:
			allusers=model.get_alluser()
			return template('umanage',allusers=allusers,user=username,issuper=1)
		return redirect('/home')

@route('/change_passwd',method=['POST'])
def change_passwd():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	password=request.forms.get('password')
	password_valid=requests.post(password_check+password).text
	if password_valid!="True":
		return "not successful registration"
	result = model.change_password(username, password)
	print(result)

	return redirect('/logout')
	#return redirect('/logout')

@route('/change_email',method=['POST'])
def change_email():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	email=request.forms.get('email')
	email_valid=requests.post(email_check+email).text
	if email_valid!="True":
		return "not successful registration"
	model.change_email(username,email)
	return redirect('/profile')

@route('/upload/<path>', method = ['POST'])
def upload(path):
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	if int(model.get_user_info(username)[6]) < MAX_UPLOADED:
		model.upload(username)
	else:
		return 'Sorry, you\'ve already uploaded too much stuff.'
	upload = request.files.get('myfile')
	dir = os.path.abspath('uploads/'+path+'/')
	if not os.path.exists(dir):
		os.mkdir(dir)
	upload.save(dir)
	return redirect('/computing-help/'+path+'.html')

@route('/units')
def units():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	unit=os.listdir("units")
	unit.sort()
	issuper=model.is_superuser(username)[0]==1
	return template('units',user=username,unit=unit,issuper=issuper)

@route('/career')
def career():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	career=os.listdir("career")
	career.sort()
	issuper=model.is_superuser(username)[0]==1
	return template('career',user=username,career=career,issuper=issuper)


@route('/resources')
def resources():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	issuper=model.is_superuser(username)[0]==1
	return template('resources',user=username,issuper=issuper)

@route('/computing-help')
def computing():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	computing=os.listdir("computing")
	computing.sort()
	issuper=model.is_superuser(username)[0]==1
	return template('computing',user=username,computing=computing,issuper=issuper)

@route('/academic-honesty-policy')
def policy():
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	issuper=model.is_superuser(username)[0]==1
	return template('policy',user=username,issuper=issuper)

@route('/computing-help/<path>.html')
def page(path):
	username = request.get_cookie("session",secret=skey)
	if not username:
		return redirect('/login')
	upload = request.files.get('myfile')
	dir = os.path.abspath('uploads/'+path+'/')
	if not os.path.exists(dir):
		os.mkdir(dir)
	uploads = os.listdir('uploads/'+path+'/')
	issuper=model.is_superuser(username)[0]==1
	return template('computing/'+path+'.html', user=username, uploads=uploads,issuper=issuper)

@error(404)
def error404(error):
    return 'You should not be here! Nothing here, sorry......'
