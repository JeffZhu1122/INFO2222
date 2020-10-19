<!DOCTYPE html>
% include('top.tpl')
<div class="content">
    <div class="container details">
        <div id="main" style="width:100%;">
            <h1 class="title">Computing Help</h1>
            <input class="flat" type="button" value="Back" onclick="javascript:window.location.href='/resources'"/>
            <h3> Computing helps </h3>
            

                    <br/>
                    <br/>
                    <br/>
                    <br/>

                    <div style="width:15%;float:left;">
                    % for u in computing:
                        <!-- <a href="/computing/{{u}}"><h2>{{u}}</h2></a> -->
                        <div>
                            <input class="flat" type="button" data="/computing-help/{{u}}" id="doc" onclick="click1(this)" value="{{u.split(".")[0]}}"/>
                        </div>
                        <br/>

                    % end

                    </div>
                    <!-- <div id="desdiv" style="width:85%;float:left;"><span>Click the unit of study at left, the information will show up here!<iframe id="myFrameId" name="myFrameName" scrolling="yes" frameborder="0" width="800px" height="1000px"></iframe></span></div> -->
                    
                    <div id="desdiv" style="width:85%;float:left;"><span>Click the button on the left, you can access the repository of relavent programming languages!<iframe id="myFrameId" name="myFrameName" scrolling="no" frameborder="0" width="1000px" height="300px"></iframe></span></div>
                    <hr/>
        </div>
    </div>
</div>
% include('bottom.tpl')
<script>
function click1(e) {
    var id=e.getAttribute("data");
    document.getElementById('desdiv').innerHTML = '<iframe src='+id+' scrolling="no" frameborder="0" width="1000px" height="300px"></iframe>';
}
</script>
