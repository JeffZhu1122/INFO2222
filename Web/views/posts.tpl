<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>PeerHub Post Center</title>
    <script src='/js/jquery.js'></script>
    <script src='/js/chat.js'></script>
    <link rel="stylesheet" type="text/css" href="/css/pure.css">
    <link rel="stylesheet" type="text/css" href="/css/grid.css">
    <link rel="stylesheet" type="text/css" href="/css/main.css">
    <link rel="stylesheet" type="text/css" href="/css/chat.css" />
</head>
<body>
    <div class="body-container">
        
        % include('top.tpl')
        <div id='chat'>
            <div style="padding: 0 60px;width:20%;float:left;">
                <form action='#' >
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>

                    <label for='nick'>Title:</label><input type='text' name='title' placeholder="Title ..."/>
                    <br>
                    <br>
                    <label for='nick'>Message:
                    <br>
                    <textarea cols="50" rows="10" name='text' placeholder="Post ..."></textarea> 
                    <input class="flat" type='submit' value='send'/>


                </form>
            </div>
            <br>

            <div align="center" >Welcome to PeerHub Post Center</div>

            <div class='window' style='width:70%;float:left;overflow:auto; height:550px;'>
                <hr width="50%"/>
                <div style="height: 0px"></div>
                
                <br>
            </div>

            
            <br/>
        </div>

        <div style='display: none'>

            <div id='tpl_message' class='message inner' >
                <br>
                &nbsp;&nbsp;&nbsp;Title: <span class='title'></span>
                <br>
                &nbsp;&nbsp;&nbsp;Author: <span class='nick'></span>
                <hr/>
                &nbsp;&nbsp;&nbsp;Post: <span class='text'></span>
                <br>
                <!-- <br>
                <br>
                <br>
                <hr/>
                    <div style="font-size: 15px; width:30%;float:left;margin-bottom: -40px;">&nbsp;&nbsp;&nbsp;<span class='comm'></span></div>
                    <div style="width:70%;float:right;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="commend" placeholder="Comment here!" /><input class='flat'type="submit" value="Submit" /></div>
                <br>
                 <br> -->
            </div>
            <div id='tpl_timestamp' class='timestamp'></div>
            

        </div>

    </div>
    
    % include('bottom.tpl')
</body>
</html>
