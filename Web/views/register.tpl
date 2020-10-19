<!DOCTYPE html>
% include('top.tpl')
<html>
    <head>
    <title>Register</title>
    </head>
    <body>

        <div class="content">
            <h1 class="title">Register</h1>
            <h2 class="title" align="center">Create an account</h2>
            <form class="login" method="POST" action="/register">

                <input type="text" name="username" placeholder="Username" autofocus required>
                <input type="password" name="password" placeholder="Password" required>
                <h5>* Your password needs to be 8 to 16 characters long, and must contain at least one digit and a capital letter.</h5>
                <input type="password" name="pass_check" placeholder="Type the password again" required>
                <input type="text" name="email" placeholder="email" autofocus required>
                <button class="flat" type="submit">Register</button>
            </form>
            <br>
            <form class="login" action="#">
                <h4 align="center">Existing user? <a href="/login">Login</a>.</h4>
            </form>
        </div>
    </body>
</html>
% include('bottom.tpl')
