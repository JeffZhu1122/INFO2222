<!DOCTYPE html>

<html>
    <head>

        <title>PeerHub</title>
        <link rel="stylesheet" type="text/css" href="/css/pure.css">
        <link rel="stylesheet" type="text/css" href="/css/grid.css">
        <link rel="stylesheet" type="text/css" href="/css/main.css">
        <script src='/js/jquery.js'></script>
    </head>
    <body>
        <div class="body-container">
            <header class="page-header">
                <div class="container">

                    <div class="title">
                        <a href="/">
                            <img style="width:80px; height:80px;" src="../img/homepage.png" alt="home page">
                        </a>
                    </div>
                    <ul class="page-nav nav">

                        % if user==None:
                            <li><a href="/login"><h6>Login</h6></a></li>
                            <li><a href="/register"><h6>Register</h6></a></li>
                        % end

                        % if user!=None:
                        <li><a href="/posts"><img style="width:60px; height:50px;" src="../img/discussion.png" alt="Discussion"></a></li>
                            <li><a href="/resources"><img style="width:50px; height:40px;" src="../img/resources.png" alt="Resources"></a></li>
                            <li><a href="/message"><img style="width:50px; height:50px;" src="../img/message.png" alt="Message"></a></li>
                            % if issuper:
                                <li><a href="/user-manage"><img style="width:50px; height:50px;" src="../img/umanage.png" alt="Manage User"></a></li>
                            % end
                                <li ><a href="/profile"><img style="width:50px; height:50px;" src="../img/profile.png" alt="Profile"></a></li>
                                <li><a href="/logout"><img style="width:50px; height:50px;" src="../img/logout1.png" alt="Logout"></a></li>

                        % end
                    </ul>
                </div>
            </header>
