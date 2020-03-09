from route import *
from beaker.middleware import SessionMiddleware


session_opts = {
    'session.type':'file',                   # 以文件的方式保存session
    'session.cookei_expires':3600,       # session过期时间为3600秒
    'session.data_dir':'/tmp/sessions',  # session存放路径
    'sessioni.auto':True
}

app = default_app()
app = SessionMiddleware(app, session_opts)

if __name__ == '__main__':
	run(app=app,host='localhost', port=8080,debug=True, reloader = True)