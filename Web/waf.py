from bottle import run, request, post, get
import re
import string
import time

# Important globals
host = "localhost"
port = "8081"

# Debug mode to check whether or not attacks are working
debug = False


@post('/waf/detect/<string_in:path>')
def detect_attack(string_in):
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$", "(", ")","@", "%","!"]
    if not debug:
        for letter in string_in:
            if letter in dirty_stuff:
                data=time.strftime("%d-%m-%y %H:%M:%S", time.localtime()) 
                log=open("attack_log.txt","a+")
                log.write(data+"      content: "+string_in+"\n")
                return 'False'
        return 'True'
    return 'False'

@post('/waf/email/<email:path>')
def verify_email(email):
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$", "(", ")", "%","!"]
    if '@' in email:
        for letter in email:
            if letter in dirty_stuff:
                return 'False'
        return "True"
    else:
        return "Not an email address"

@post('/waf/password/<password:path>')
def verify_password(password):
    if 8<=len(password) and len(password)<=16:
        int_count = 0
        for c in password:
            if c.isdigit():
                int_count+=1
                break
        if int_count==0:
            return "Password must contain at least one digit"
    if not any(c in string.ascii_uppercase for c in password):
        return "Password must contain at least one uppercase character"
    return 'True'

# Debug toggle
@post('/waf/debug')
def enable_debugger():
    global debug
    if debug:
        debug = False
    else:
        debug = True

# Run the server
run(host=host, port=port)