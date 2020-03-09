% include('top.tpl')
<html>
    <head>
    <title>Register</title>
    </head>
    <body>

        <div class="content">
            <h1 class="title">Register</h1>

            <form class="login" method="POST" action="/register">
                <input type="text" name="username" placeholder="Username" autofocus required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="text" name="email" placeholder="email" autofocus required>
                <input type="text" name="phone" placeholder="phone" autofocus required>
                <button class="flat" type="submit">Register</button>
                <input class="flat" type="button" value="Back" onclick="javascript:window.location.href='http://info.jeffscode.com/login'"/>
            </form>
        </div>
    </body>
</html>
% include('bottom.tpl')