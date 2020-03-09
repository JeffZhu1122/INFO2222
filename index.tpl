% include('top.tpl')
<div class="content">
    <div class="container details">
        <h1 class="title"> Welcome, {{ user['user_name'] }}</h1>
             <form action="/changpasswd" method="post">
              New Password: <input type="password" name="password" value="" /><button class="flat" type="submit">Change password</button><br />
            </form>
            <h3> User Information </h3>
                <div>
                        User Name: {{user['user_name']}}
                </div>
                <br/>
                <div>
                        E-mail: {{user['user_email']}}
                </div>
                <br/>
                <div>
                        phone: {{user['user_phone']}}
                </div>
                <br/>
                <div>
                        Is Super: {{ user['is_super'] }}
                </div>
                <br/>
            	<div>
                        Register Date: {{ user['submission_date'] }}
                </div>
                <br/>
                
                <input class="flat" type="button" value="IM Chat" onclick="javascript:window.location.href='http://info.jeffscode.com/chat'"/>
                % if user["is_super"]=="True":
                <input class="flat" type="button" value="Manage User" onclick="javascript:window.location.href='http://info.jeffscode.com/umanage'"/>
                % end
                <input class="flat" type="button" value="Logout" onclick="javascript:window.location.href='http://info.jeffscode.com/logout'"/>
        </form>

        <hr/>
    </div>
</div>
% include('bottom.tpl')
