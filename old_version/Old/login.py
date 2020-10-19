import sqlite3
from bottle import route, run, template, request, get, post

@route('/login')
def login():
  return '''
    <form action="/login" method="post">
    Username: <input name="username" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
    </form>
  '''

@route('/login', method = 'POST')
def confirm_login():
  username = request.forms.get('username')
  password = request.forms.get('password')

  conn = sqlite3.connect('todo.db')
  c = conn.cursor()

  c.execute("SELECT username, passwd FROM todo WHERE role LIKE 'student'")

  result = str(c.fetchall())
  c.close()

  store = result.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace("'", '').split(', ')
  
  count = 0
  for i in range(len(store)//2):
    if store[count] == username:
      if store[count+1] == password:
        return "<b>Login success</b>"
    count += 2

  print(store)
    #return "<b>Logged in</b>"
  
  return "<b>Login failed</b>"

run(reloader = True)

