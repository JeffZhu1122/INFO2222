<!DOCTYPE html>
% include('top.tpl')
<div class="content">
    <div >
        % if user!=None:
            <h1 class="title"> Welcome, {{ user }}</h1>
        % end
        <br/>
        <br/>
        
        <br/>
        <br/>

                

                <div align="center">
                	<br/>
                	<br/>
                	<br/>
                	<br/>
                	<br/><br/>
                	<div><h1 style="margin: 0 300px 0 0" >Peerhub.</h1></div>
                	<div><h1>Your reliable support system.</h1></div>
                	<div><h1 style="margin: -50px 370px 0 0">____</h1></div>
                	<br/><br/><br/>
                	<div><h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; > Hello World  <label id="blink">l</label></h1></div>

                        
                </div>
                <br/>

    </div>
</div>


<!-- <div class="footer" align="center" >
	<table class="styled1">
        <tbody>
            <tr>
                <td align="center" style="border-left: 0px solid #eee;">
                	<div class="marker" ></div>
                    <p>
                        USERS
                    </p>
                </td>
                <td align="center">
                	<div class="marker" ></div>
                    <p>
                        DISCUSSIONS
                    </p>
                </td>
                <td align="center">
                	<div class="marker" ></div>
                    <p>
                        SOURCES
                    </p>
                </td>
                <td align="center" style="border-right: 0px solid #eee;">
                	<div class="marker" ></div>
                    <p>
                        MESSAGES
                    </p>
                </td>

            </tr>
        </tbody>
    </table>

</div> -->


% include('bottom.tpl')
<script language="javascript">
        function changeColor(){
            if (document.getElementById("blink").style.color=="white"){
            	document.getElementById("blink").style.color="black";
            }else{
            	document.getElementById("blink").style.color="white";
            }
            
        }
        setInterval("changeColor()",300);
</script>

<style type="text/css">
	.marker {      

 width: 8px;      

 height: 8px;      

 border: 3px solid black;      

 border-radius: 100px;        

     } 

        .footer{position:absolute;bottom:10px;width:100%;height:150px;}
    </style>