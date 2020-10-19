<!DOCTYPE html>
% include('top.tpl')
<div class="content">
    <div class="container details">
        <div id="main" style="width:100%;">
            <h1 class="title"> Resources</h1><br/>

            <input class="flat" type="button" value="Back" onclick="javascript:window.location.href='/resources'"/>
            <br/>
            <br/>
            <h3> All Units Resources </h3>
            <br/>
                    <br/>
                    <br/>
            

    <div id="menu" style="width:15%; float:left;">
        <h1 onClick="javascript:ShowMenu(this,'NO0')"> + 1000 Units</h1>
           <ul id="NO0" class="no">
            % for u in unit:
                % if u[4]=="1":
                    <li><input class="flat" type="button" data="/units/{{u}}" id="doc" onclick="click1(this)" value="{{u.split(".")[0]}}"/></li>
                % end
            % end
           </ul>
        <h1 onClick="javascript:ShowMenu(this,'NO1')"> + 2000 Units</h1>
            <ul id="NO1" class="no">
            % for u in unit:
                % if u[4]=="2":
                    <li><input class="flat" type="button" data="/units/{{u}}" id="doc" onclick="click1(this)" value="{{u.split(".")[0]}}"/></li>
                % end
            % end
            </ul>
        <h1 onClick="javascript:ShowMenu(this,'NO2')"> + 3000 Units</h1>
            <ul id="NO2" class="no">
            % for u in unit:
                % if u[4]=="3":
                    <li><input class="flat" type="button" data="/units/{{u}}" id="doc" onclick="click1(this)" value="{{u.split(".")[0]}}"/></li>
                % end
            % end
            </ul>
        <h1 onClick="javascript:ShowMenu(this,'NO3')"> + 4000 Units</h1>
            <ul id="NO3" class="no">
            % for u in unit:
                % if u[4]=="4":
                    <li><input class="flat" type="button" data="/units/{{u}}" id="doc" onclick="click1(this)" value="{{u.split(".")[0]}}"/></li>
                % end
            % end
            </ul>
    </div>

                    % if user!=None and issuper:
                        <div id="desdiv2" style="width:85%;float:left;"><span></span></div>
                     % end
                    <div id="desdiv1" style="width:85%;float:left;"><span></span></div>
                    <div id="desdiv" style="width:85%;float:left;"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Click the unit of study at left, the information will show up here!<iframe id="myFrameId" name="myFrameName" scrolling="no" frameborder="0" width="1000px" height="900px"></iframe></span></div>


        <hr/>
        </div>
    </div>
</div>
% include('bottom.tpl')
<script>
function click1(e) {
    var id=e.getAttribute("data");
    document.getElementById('desdiv1').innerHTML = '<a href="/units-pdf/'+id.substring(7,15)+'.pdf"'+'><h2>&nbsp;&nbsp;&nbsp;UOS Outline</h2></a>';
    document.getElementById('desdiv').innerHTML = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<iframe src='+id+' scrolling="no" frameborder="0" width="1000px" height="900px"></iframe>';
}
</script>
<style>
*,body,ul,li,h1,h2 {
    vertical-align: center;

    padding: 0;
    list-style: none;
}
 
 
#menu {
    width: 200px;
    margin: auto;
}
 
#menu h1 {
    cursor: pointer;
    color: #FFF;
    font-size: 16px;
    padding: 5px 0 5px 10px;
    border: #C60 1px solid;
    margin-top: 1px;
    background-color: #F93;
}
 
#menu h2 {
    cursor: pointer;
    color: #777;
    font-size: 12px;
    padding: 5px 0 5px 10px;
    border: #E7E7E7 1px solid;
    border-top-color: #FFF;
    background-color: #F4F4F4;
}
 
#menu ul {
    padding-left: 15px;
    height: auto;
    border: #E7E7E7 1px solid;
    border-top: none;
    overflow: auto;
}
 
#menu ul li {

    padding: 5px 0 5px 10px;
}
 
.no {
    display: none;
}
    </style>
    <script language="JavaScript">
        function ShowMenu(obj, noid) {
            var block = document.getElementById(noid);
            var n = noid.substr(noid.length - 1);
            if (noid.length == 8) {
                var ul = document.getElementById(noid.substring(0, 3)).getElementsByTagName("ul");
                var h2 = document.getElementById(noid.substring(0, 3)).getElementsByTagName("h2");
                for (var i = 0; i < h2.length; i++) {
                    h2[i].innerHTML = h2[i].innerHTML.replace("-", "+");
                    h2[i].style.color = "";
                }
                obj.style.color = "#FF0000";
                for (var i = 0; i < ul.length; i++) {
                    if (i != n) {
                        ul[i].className = "no";
                    }
                }
            } else {
                var span = document.getElementById("menu").getElementsByTagName("span");
                var h1 = document.getElementById("menu").getElementsByTagName("h1");
                for (var i = 0; i < h1.length; i++) {
                    h1[i].innerHTML = h1[i].innerHTML.replace("-", "+");
                    h1[i].style.color = "";
                }
                obj.style.color = "#0000FF";
                for (var i = 0; i < span.length; i++) {
                    if (i != n) {
                        span[i].className = "no";
                    }
                }
            }
            if (block.className == "no") {
                block.className = "";
                obj.innerHTML = obj.innerHTML.replace("+", "-");
            } else {
                block.className = "no";
                obj.style.color = "";
            }
        }
    </script>

