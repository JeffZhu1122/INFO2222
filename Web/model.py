import pymysql
import configparser
import random
from random import Random
import hashlib

def create_salt(length = 8):
	salt = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	len_chars = len(chars) - 1
	random = Random()
	for i in range(length):
		salt += chars[random.randint(0, len_chars)]
	return salt

def md5(password,salt):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	pwd_wo = md5.hexdigest()+salt
	md5.update(pwd_wo.encode('utf-8'))
	pwd=md5.hexdigest()
	return pwd


def print_sql_string(inputstring, params=None):
	if params is not None:
		if params != []:
		   inputstring = inputstring.replace("%s","'%s'")

	print(inputstring % params)

def dictfetchall(cursor,sqltext,params=None):
	result = []

	cursor.execute(sqltext,params)
	cols = [a[0] for a in cursor.description]

	returnres = cursor.fetchall()
	if returnres==None:
		return None
	for row in returnres:
		result.append({a:b for a,b in zip(cols, row)})
	return result

def dictfetchone(cursor,sqltext,params=None):
	result = []
	cursor.execute(sqltext,params)
	cols = [a[0] for a in cursor.description]
	returnres = cursor.fetchone()
	if returnres==None:
		return None
	result.append({a:b for a,b in zip(cols, returnres)})
	return result

def database_connect():
	config = configparser.ConfigParser()
	config.read('config.ini')
	if 'database' not in config['DATABASE']:
		config['DATABASE']['database'] = config['DATABASE']['user']
	connection=None
	try:
		connection = pymysql.connect(config['DATABASE']['host'],config['DATABASE']['user'],config['DATABASE']['password'],config['DATABASE']['database'])
	except Exception as e:
		print(e)
	return connection

########SQL Config Above########

def check_login(username,password):
	conn = database_connect()
	if(conn is None):
		return None
	cur = conn.cursor()
	if '<script>' in username or '<script>' in password:
		return None
	try:
		sql ='''SELECT salt,user_passwd
				FROM app_user
				WHERE user_name=%s;'''

		r = dictfetchone(cur,sql,(username,))
		if r!=None :
			salt=r[0]["salt"]
			test_passwd=md5(password,salt)
			if test_passwd==r[0]["user_passwd"]:
				return True
		cur.close()
		conn.close()
		return False
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None

def is_superuser(username):
	conn = database_connect()
	if conn is None:
		return None
	cur = conn.cursor()
	try:
		sql = """SELECT is_super
				 FROM app_user
				 WHERE user_name=%s;"""
		cur.execute(sql, (username,))
		r = cur.fetchone()
		cur.close()
		conn.close()
		return r
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None

def get_user_info(username):
	conn = database_connect()
	if conn is None:
		return None
	cur = conn.cursor()
	try:
		sql = """SELECT *
				 FROM app_user
				 WHERE user_name=%s;"""
		cur.execute(sql, (username,))
		r = cur.fetchone()
		cur.close()
		conn.close()
		return r
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None

def check_user(username, password, pass_check):
	conn = database_connect()
	if conn is None:
		return None
	cur = conn.cursor()
	try:
		sql='''SELECT * FROM app_user WHERE user_name=%s;'''
		cur.execute(sql, (username,))
		r = cur.fetchone()
		#print(r)
		conn.commit()
		cur.close()
		conn.close()
		if r!=None:
			return False
		elif password!=pass_check:
			return False
		return True
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None

def add_user(username,password,pass_check,email,date):
	conn = database_connect()
	if conn is None:
		return None
	cur = conn.cursor()
	try:
		if (check_user(username, password, pass_check)==False):
			return -1

		else:
			salt=create_salt()
			password=md5(password,salt)
			sql='''INSERT INTO app_user(
			user_name, user_passwd,salt,user_email, submission_date)
			VALUES(%s,%s,%s,%s,%s);
			'''
			cur.execute(sql, (username,password,salt,email,date,))
			r = cur.fetchone()
			conn.commit()
			cur.close()
			conn.close()
			return r
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None

def get_alluser():
	conn = database_connect()
	if conn is None:
		return None
	cur = conn.cursor()
	try:
		sql = """select * from app_user;"""
		r = dictfetchall(cur,sql)
		cur.close()
		conn.close()
		return r
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None

def delete_user(user_id):
	user_id=str(user_id)
	conn = database_connect()
	if conn is None:
		return None
	cur = conn.cursor()
	try:
		sql = '''DELETE FROM app_user where user_id=%s; '''
		cur.execute(sql, (user_id,))
		conn.commit()
		cur.close()
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None

def change_password(username,password):
	try:
		conn = database_connect()
		if conn is None:
			return None
		cur = conn.cursor()
		salt=create_salt()
		password=md5(password,salt)
		sql = """UPDATE app_user SET user_passwd=%s,salt=%s where user_name=%s;"""
		r = cur.execute(sql,(password,salt,username,))
		cur.close()
		conn.commit()

		cur.close()
		conn.close()
	except Exception as e:
		print(e)

	return None

def change_email(username,email):
	conn = database_connect()
	if conn is None:
		return None
	cur = conn.cursor()
	try:
		sql = """UPDATE app_user SET user_email=%s where user_name=%s;"""
		r = cur.execute(sql,(email,username,))
		cur.close()
		conn.commit()
		return r
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None

def upload(username):
	conn = database_connect()
	if conn is None:
		return None
	cur = conn.cursor()
	try:
		sql = """UPDATE app_user SET uploaded=uploaded+1 where user_name=%s;"""
		r = cur.execute(sql,(username,))
		cur.close()
		conn.commit()
		return r
	except Exception as e:
		print(e)
	cur.close()
	conn.close()
	return None
