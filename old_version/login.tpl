% include('top.tpl')
    <div class="content">
        <h1 class="title">Log in</h1>

        <form class="login" method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" autofocus required>
            <input type="password" name="password" placeholder="Password" required>
            <button class="flat" type="submit">Log in</button>
            <input class="flat" type="button" value="Register" onclick="javascript:window.location.href='http://info.jeffscode.com/register'"/>
        </form>
    </div>
% include('bottom.tpl')