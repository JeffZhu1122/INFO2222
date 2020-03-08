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
	if (params is None):
		print(sqltext)
	else:
		print("we HAVE PARAMS!")
		print_sql_string(sqltext,params)
	
	cursor.execute(sqltext,params)
	cols = [a[0] for a in cursor.description]
	print(cols)
	returnres = cursor.fetchall()
	for row in returnres:
		result.append({a:b for a,b in zip(cols, row)})
	return result

def dictfetchone(cursor,sqltext,params=None):
	result = []
	cursor.execute(sqltext,params)
	cols = [a[0] for a in cursor.description]
	returnres = cursor.fetchone()
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
				WHERE user_name=%s AND user_passwd=%s'''

		r = dictfetchone(cur,sql,(username,password,))
		cur.close()                     # Close the cursor
		conn.close()
		return r
	except Exception as e:
		print(e)
	cur.close()                     # Close the cursor
	conn.close()                    # Close the connection to the db
	return None

def is_superuser(username):
    conn = database_connect()
    if(conn is None):
        return None
    cur = conn.cursor()
    try:
        sql = """SELECT is_super
                 FROM app_user
                 WHERE user_name=%s """
        cur.execute(sql, (username,))
        r = cur.fetchone()              # Fetch the first row
        cur.close()                     # Close the cursor
        conn.close()                    # Close the connection to the db
        return r
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    cur.close()                     # Close the cursor
    conn.close()                    # Close the connection to the db
    return None

def add_user(username,password,email,phone,issuper,date):
	conn = database_connect()
	if(conn is None):
		return None
	cur = conn.cursor()
	
	try:
		sql='''INSERT INTO app_user(
		user_name,user_passwd,user_email,user_phone,submission_date,is_super)
		VALUES(%s,%s,%s,%s,%s,%s);
		'''
		cur.execute(sql, (username,password,email,phone,date,issuper,))
		r = cur.fetchone()
		conn.commit()
		cur.close()                     # Close the cursor
		conn.close()
		return r
	except Exception as e:
		print(e)
	
	cur.close()                     # Close the cursor
	conn.close()                    # Close the connection to the db
	return None

# def mail(my_user,username):
#     ret=True
#     try:
#         my_sender='admin@admin.com'
#         msg=MIMEText('''Dear{}：\nSuccessful!'''.format(username),'plain','utf-8')
#         msg['From']=formataddr(["sng admin",my_sender])   
#         msg['To']=formataddr([my_user,my_user])   
#         msg['Subject']='Successful'
#         server=smtplib.SMTP("52.65.238.130",25)  
#         server.login("admin","admin")    
#         server.sendmail(my_sender,my_user,str(msg))   
#         server.quit()   
#     except Exception:  
#         ret=False