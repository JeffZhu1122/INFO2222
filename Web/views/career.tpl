<!DOCTYPE html>
% include('top.tpl')
<div class="content">
    <div class="container details">
        <div id="main" style="width:100%;">
            <h1 class="title"> Career</h1>
                <input class="flat" type="button" value="Back" onclick="javascript:window.location.href='/resources'"/>   
            <h3> All Career Informations </h3>
            
                    <br/>
                    <br/>
                    <br/>
                    <div style="width:30%;float:left;"> 
                    % for u in career:

                        
                    <div>
                        <input class="flat" type="button" data="/career/{{u}}" id="doc" onclick="click1(this)" value='{{u.split(".")[0].replace("_"," ")}}'/>
                    </div>

                    <br/>
                    % end
                    </div>
                    <div id="desdiv1" style="width:70%;float:left;"><span></span></div>
                    <div id="desdiv" style="width:70%;float:left;"><span>Click the Job at left, the information will show up here!<iframe id="myFrameId" name="myFrameName" scrolling="yes" frameborder="0" width="800px" height="1000px"></iframe></span></div>

        <hr/>
        </div>
    </div>
</div>
% include('bottom.tpl')
<script>
function click1(e) {
    var id=e.getAttribute("data");
    document.getElementById('desdiv1').innerHTML = '<a href="/career-pdf/'+id.split(".")[0].split("/")[2]+'.pdf"'+'>View the full document</a>';
    document.getElementById('desdiv').innerHTML = '<iframe src='+id+' scrolling="yes" frameborder="0" width="800px" height="1000px"></iframe>';
}
</script>