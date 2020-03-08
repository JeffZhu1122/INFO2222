from bottle import *
import database


user_details = {} 
session = {} 
	
@route('/')
def index():
	if('logged_in' not in session or not session['logged_in']):
		return redirect('/login')
	return "hello "+str(user_details)

@route('/login',method=['POST', 'GET'])
def login():
	
	if(request.method == 'POST'):
        # submitting details
        # The form gives back EmployeeID and Password
		login_return_data = database.check_login(
            request.forms.get('username'),
            request.forms.get('password')
        )

        # If it's null, saying they have incorrect details
		if login_return_data is None:
			return redirect('/login')

		session['logged_in'] = True

        # Store the user details for us to use throughout
		global user_details
		user_details = login_return_data[1]
		return redirect('/',)
	elif(request.method == 'GET'):
		return template('login')
	


@route('/register', method=['POST', 'GET'])
def register():
	if(request.method == 'POST'):
		register_return_data = database.add_user(
			request.forms.get('username'),
			request.forms.get('password'),
			request.forms.get('email'),
			request.forms.get('phone'),
			time.strftime("%Y-%m-%d", time.localtime()) 
        )
		return redirect('/login',)
	elif(request.method == 'GET'):
		return template('register')
	
	


# @route('/deleteuser')
# def deleteuser():
# 	db = pymysql.connect("52.65.238.130","web","C3zr6XLmw3JGZxCh","web")
# 	cursor = db.cursor()
# 	cursor.execute( '''select * from web_user WHERE user_id>=0;''')
# 	userId = len(cursor.fetchall())
# 	username = request.query.username
# 	cursor.execute( '''select * from web_user WHERE user_name="{}";'''.format(username))
# 	email = request.query.email
# 	if len(cursor.fetchall())>0 or "@" not in email:
# 		return json.dumps({"Result":"False"})
# 	password = request.query.password	
# 	phone = request.query.phone
# 	date= time.strftime("%Y-%m-%d", time.localtime()) 
# 	sql='''INSERT INTO web_user(
# 		user_id,user_name,user_passwd,user_email,user_phone,user_fight,submission_date,wallet)
# 		VALUES(
# 		{},"{}","{}","{}","{}",{},'{}',{});
# 		'''.format(userId,username,password,email,phone,0,date,0)
# 	cursor.execute(sql)
# 	db.close()
# 	mail(email,username)
# 	return  json.dumps({"Result":"True"})

# @route('/getmedia')
# def videoUrl():	
# 	db = pymysql.connect("52.65.238.130","web","C3zr6XLmw3JGZxCh","web")
# 	cursor = db.cursor()
# 	cursor.execute( '''select * from web_video WHERE video_id>=0;''')
# 	allVideo=cursor.fetchall() 
# 	allBin=[]
# 	for i in range (len(allVideo)):
# 		allBin.webend({})
# 		allBin[i]["title"]=allVideo[i][1]
# 		allBin[i]["url"]=allVideo[i][2]
# 		allBin[i]["thumbnail_pic_s"]=allVideo[i][3]
# 	return json.dumps({"result":{"data":allBin}})
	

