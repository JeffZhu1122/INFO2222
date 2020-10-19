<!DOCTYPE html>
% include('top.tpl')
    <div class="content">
        <h1 class="title">Log in</h1>
		<h2 class="title" align="center">Sign into your account</h2>
        <form class="login" method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" autofocus required>
            <input type="password" name="password" placeholder="Password" required>
            <button class="flat" type="submit">Log in</button>
            
        </form>
        <br>
        <form class="login" action="#">
                <h4 align="center">New user? <a href="/register">Register</a>.</h4>
            </form>
    </div>
% include('bottom.tpl')