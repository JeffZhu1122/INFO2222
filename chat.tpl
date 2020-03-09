<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Bottle Chat</title>
    <script src='http://code.jquery.com/jquery-1.6.4.min.js'></script>
    <script src='/js/chat.js'></script>
    <link rel="stylesheet" type="text/css" href="/css/pure.css">
    <link rel="stylesheet" type="text/css" href="/css/grid.css">
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <link rel="stylesheet" type="text/css" href="/js/chat.css" />
</head>
<body>
    <div class="body-container">
        <header class="page-header">
            <div class="container">
                <div class="title">
                    <a href="/"><span class="inner"></span></a>
                </div>
                <ul class="page-nav">

                </ul>
            </div>
        </header>
        <div id='chat'>
            <div class='window' style='overflow:auto; width:100%; height:300px;'>
                <div style="height: 1000px"></div>
                <div class='topic'>Welcome to the bottle chat test.</div>
            </div>
            <form action='#'>
                
                <label for='nick'>Message:</label><input type='text' name='text' />
                <input type='submit' value='send'/>

            </form>
            <br/>
            <input class="flat" type="button" value="Back" onclick="javascript:window.location.href='http://info.jeffscode.com/'"/>
        </div>

        <div style='display: none'>
            <div id='tpl_message' class='message'>
                <span class='nick'></span>: <span class='text'></span>

            </div>
            <div id='tpl_timestamp' class='timestamp'>
                
            </div>
        </div>

    </div>
    <footer class="page-footer">
        <div class="container">
            <div class="pure-g">
                <div class="pure-u-1 pure-u-md-1-2">
                    <ul>
                        <li><span>Copyright &copy; 2020 </span></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
    <script src="/js/clickable.js"></script>
</body>
</html>
