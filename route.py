from bottle import *
import database
import gevent.monkey
import collections
import datetime
from time import time
from gevent import sleep

messages = collections.deque()

MESSAGE_TIMEOUT = 10
FLOOD_MESSAGES = 5
FETCH_FREQ = 1000

class Message(object):
	def __init__(self, nick, text):
		self.time = time()
		self.nick = nick
		self.text = text

	def json(self):
		return {'text': self.text, 'nick': self.nick, 'time': self.time}

js = '''

'''
gevent.monkey.patch_all()

	

@route('/css/<path>')  
def css(path):  
	return static_file(path, root='css')

@route('/js/<path>')  
def js(path):  
	return static_file(path, root='js')

@route('/')
def index():
	s = request.environ.get('beaker.session')
	if s==None:
		return redirect('/login')
	if "user" not in s:
		return redirect('/login')
	s = request.environ.get('beaker.session')  
	return template('index',user=s['user'])

@route('/login',method=['POST', 'GET'])
def login():
	if(request.method == 'POST'):
		login_return_data = database.check_login(
			request.forms.get('username'),
			request.forms.get('password')
		)
		if login_return_data is None:
			return redirect('/login')
		s = request.environ.get('beaker.session')  
		s['user'] = login_return_data[0]
		s.save()
		return redirect('/')
	elif(request.method == 'GET'):
		return template('login')
	
@route('/logout')
def logout():
	s = request.environ.get('beaker.session')
	s['user'] = None
	s.save()
	return redirect('login')

@route('/register', method=['POST', 'GET'])
def register():
	if(request.method == 'POST'):
		register_return_data = database.add_user(
			request.forms.get('username'),
			request.forms.get('password'),
			request.forms.get('email'),
			request.forms.get('phone'),
			datetime.datetime.now()
		)
		return redirect('/login',)
	elif(request.method == 'GET'):
		return template('register')
	
@route('/chat')
def logout():
	return template('chat')	

@get('/chat/api/info')
def on_info():
	return {
		'server_name': 'Bottle Test Chat',
		'server_time': time(),
		'refresh_interval': 1000
	}

@post('/chat/api/send_message')
def on_message():
	text = request.forms.get('text', '')
	nick = request.forms.get('nick', '')
	if ':' in nick: 
		nick, token = nick.split(':', 1)
	else:           
		token = ''
	nick = nick.strip()
	if not text: return {'error': 'No text.'}
	timeout = time()-MESSAGE_TIMEOUT
	while messages and messages[0].time < timeout:
		messages.popleft()
	if len([m for m in messages if m.nick == nick]) > FLOOD_MESSAGES:
		return {'error': 'Messages arrive too fast.'}
	s = request.environ.get('beaker.session')  
	messages.append(Message(s['user']["user_name"], text))
	return {'status': 'OK'}

@get('/chat/api/fetch')
def on_fetch():
	since = float(request.params.get('since', 0))
	updates = [m.json() for m in messages if m.time > since]
	return { 'messages': updates[:10] }

@route('/umanage')
@route('/umanage/delete/<user_id>')
def umanage(user_id="0"):
	s = request.environ.get('beaker.session')
	username = s.get('user',None) 
	if not username:
		return redirect('/login')
	if user_id!="0":
		database.delete_user(user_id)
		return redirect('/umanage')
	else:
		if user_details['is_super']=="True":
			allusers=database.get_alluser()
			return template('umanage',allusers=allusers)
		return redirect('/')


@route('/changpasswd',method=['POST'])
def changpasswd():
	s = request.environ.get('beaker.session')
	username = s.get('user',None) 
	if not username:
		return redirect('/login')
	s = request.environ.get('beaker.session')  
	database.change_password(s['user']["user_id"],
			request.forms.get('password'))
	return redirect('/logout')
