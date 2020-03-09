import smtplib  
from email.mime.text import MIMEText
from email.utils import formataddr
import pymysql
import configparser

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

def check_login(username,password):
	conn = database_connect()
	if(conn is None):
		return None
	cur = conn.cursor()
	try:
		sql ='''SELECT *
				FROM app_user
				WHERE user_name=%s AND user_passwd=%s;'''

		r = dictfetchone(cur,sql,(username,password,))
		cur.close()                    
		conn.close()
		return r
	except Exception as e:
		print(e)
	cur.close()                     
	conn.close()                   
	return None

def is_superuser(username):
    conn = database_connect()
    if(conn is None):
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

def add_user(username,password,email,phone,date):
	conn = database_connect()
	if(conn is None):
		return None
	cur = conn.cursor()
	try:
		sql='''INSERT INTO app_user(
		user_name,user_passwd,user_email,user_phone,submission_date)
		VALUES(%s,%s,%s,%s,%s);
		'''
		cur.execute(sql, (username,password,email,phone,date,))
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
    if(conn is None):
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
    if (conn is None):
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

def change_password(userid,password):
    conn = database_connect()
    if (conn is None):
        return None
    cur = conn.cursor()
    try:
        sql = """UPDATE app_user SET user_passwd=%s where user_id=%s;"""
        r = cur.execute(sql,(password,userid,))
        cur.close()                     
        conn.commit()                  
        return r
    except Exception as e:
        print(e)
    cur.close()                   
    conn.close()                   
    return None
