<!DOCTYPE html>
% include('top.tpl')
<div class="content">
    <div class="container details">
        <h1 class="title"> All Users</h1>
        <div>
            <table class="styled">

                <thead>
                    <tr>
                        <td>user ID</td>
                        <td>User Name</td>
                        <td>User Email</td>
                        <td>User Register Date</td>
                        <td>Is Super User</td>
                    </tr>
                </thead>
                <tbody>
                    % for instance in allusers:
                        <tr>
                            <td style="text-align: center">{{ instance['user_id'] }}</td>
                            <td>{{instance['user_name']}}</td>
                            <td>{{instance['user_email']}}</td>
                            
                            <td>{{instance['submission_date']}}</td>
                            <td>{{instance['is_super']}}</td>
                            % if instance['user_id']!=0:
                                <td onclick="td_click()"><button class="clickable-tr flat" data-href="/user-manage/delete/{{ instance['user_id'] }}">delete</button></td>
                            % end
                        </tr>
                    % end
                </tbody>

            </table>

        </div>
    </div>
</div>
% include('bottom.tpl')
<script src="js/clickable.js"></script>
<script language="javascript">

function td_click(){
event.cancelBubble=true;
}

</script>