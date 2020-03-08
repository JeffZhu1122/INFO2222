<html>
    <head>
    <title>Login</title>
    </head>
    <body>
        <p><h2>Login</h2></p>
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        <input type="button" value="Register" onclick="javascript:window.location.href='http://0.0.0.0:8080/register'"/>
    </body>
</html>