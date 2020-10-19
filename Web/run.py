import model
import view
import controller
import sys
from beaker.middleware import SessionMiddleware
from bottle import *

session_opts = {
    'session.type':'file',
    'session.cookei_expires':3600,
    'session.data_dir':'/tmp/sessions',
    'sessioni.auto':True
}


if __name__ == "__main__":
    app = default_app()
    app = SessionMiddleware(app, session_opts)
    host = 'localhost'
    port = 8182
    debug = True
    reloader = True

    run(app=app, host=host, port=port, debug=debug, reloader=reloader)

else:
    application = default_app()
    # application = SessionMiddleware(application, session_opts)
