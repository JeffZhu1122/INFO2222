<!DOCTYPE html>
% include('top.tpl')
<div class="content">
    <div class="container details">
        <h1 class="title"> Profile</h1>

        <br/>
            <form action="/change_email" method="post">
             New Email: <input type="input" name="email" value="" /><button class="flat" type="submit">Change email</button><br />
           </form>
           <br/>
             <form action="/change_passwd" method="post">
              New Password: <input type="password" name="password" value="" /><button class="flat" type="submit">Change password</button><br />
            </form>

            
            <h3> User Information </h3>
                <div>
                        User Name: {{info[1]}}
                </div>
                <br/>
                <div>
                        E-mail: {{info[4]}}
                </div>
                <br/>
                <div>
                        % if info[5]==1:
                            Is Super: True
                        % else:
                            Is Super: False
                        % end
                </div>
                <br/>
            	<div>
                        Register Date: {{info[7]}}
                </div>
                <br/>
                <div>
                        Uploaded Items: {{info[6]}}
                </div>
                <br/>

        <input class="flat" type="button" value="Logout" onclick="javascript:window.location.href='/logout'"/>
        <br/>



    </div>
</div>
% include('bottom.tpl')
