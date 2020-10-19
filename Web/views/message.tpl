<!DOCTYPE html>

<head>
<meta http-equiv="Content-Type" content="charset=utf-8" />
<title>Message</title>
<link rel="stylesheet" type="text/css" href="/css/font-awesome.min.css"/>
<link rel="stylesheet" type="text/css" href="/css/message.css" />
</head>
<body>
<script>
username = password = null;
unRead={}
</script>
% include('top.tpl')
<div class="main_inner">
	<div class="panel" id="panel">
		<!--BEGIN header-->
		<div class="header">
			<div class="avatar">
				<img class="img" src="/img/git.png">
			</div>
			<div class="info">
				<h3 class="nickname">
					<span class="display_name ng-binding">Nobody</span>
				</h3>

			</div>
		</div>
		<!--END header-->

		<!--BEGIN search-->
		<div class="search_bar" id="search_bar">
			<i class="fa fa-search" id="searchJoin"></i>
			<input class="frm_search ng-isolate-scope ng-pristine ng-valid" value="" type="text" id='joinInput' placeholder="Search">
		</div>
		<!--END search-->

		<!--BEGIN tab-->
		<div class="tab" >
			<div class="tab_item">
				<a class="chat" title="Chat" href="javascript:void(0)" id="chatOp"><i class="fa fa-comments"></i><span class="commentsTips"></span></a>
			</div>
			<div class="tab_item no_extra">
				<a class="chat"  title="Contacts" href="javascript:void(0)"><i class="fa fa-address-book" ></i></a>
			</div>
		</div>
		<!--END tab-->
	<div class="nav_view" style="visibility: visible; width: auto;">
		<div class="scroll-wrapper chat_list scrollbar-dynamic" style="position: relative;">

		  <div jquery-scrollbar="" class="chat_list scrollbar-dynamic scroll-content scroll-scrolly_visible operations" id="chatList" data-username="" style="margin-bottom: 0px; margin-right: 0px; height: 473px;">
			<h5 style="color:#ff5555;text-align:center" class="showEmpty">Empty</h5>
		  </div>

		  <div class="chat_list scrollbar-dynamic scroll-content scroll-scrolly_visible operations" id="searchResult" style="display:none;margin-bottom: 0px; margin-right: 0px; height: 473px;">

		  </div>

		  <div class="chat_list scrollbar-dynamic scroll-content scroll-scrolly_visible operations" id="groupop" style="display:none;margin-bottom: 0px; margin-right: 0px; height: 473px;">
			<h3 align="center" style="    border-top: solid 1px #828180;padding-top: 5px;"><i class='fa fa-plus-square' id="addGroup" style="color: #68ccf3;"></i></h3>

		  </div>

		  <div class="chat_list scrollbar-dynamic scroll-content scroll-scrolly_visible operations" id="addressList" style="display:none;margin-bottom: 0px; margin-right: 0px; height: 473px;">

		  </div>

		</div>
	</div>
	</div>

	<div ui-view="contentView" style="height:100%;" class="ng-scope">
		<div id="chatArea" class="box chat ng-scope">

			<div class="box_hd">
			  <div id="chatRoomMembersWrap"></div>
				<div class="title_wrap">
					<div class="title poi">
						<a class="title_name ng-binding">Welcome to PeerHub Message System!</a>

						<i class="web_wechat_down_icon"></i>
					</div>
				</div>

			</div>

			<div class="scroll-wrapper box_bd chat_bd scrollbar-dynamic">
				<div jquery-scrollbar="" id="msgContent"class="box_bd chat_bd scrollbar-dynamic scroll-content"  style="margin-bottom: 0px; margin-right: 0px; height: 431px;">
				<h4 align="center">Empty</h4>
				</div>

			</div>

			<div class="box_ft ng-scope" >

				<div class="content ng-isolate-scope" >
					<pre id="editArea"  class="flex edit_area ng-isolate-scope ng-pristine ng-valid" contenteditable="false"  ></pre>
					<span class="caret_pos_helper" id="caretPosHelper"></span>
				</div>

				<div class="action">
					<input class="btn btn_send" id="btn_send" href="javascript:void(0);" value="Send" readonly="readonly"/>
				</div>
			</div>
		</div>
	</div>
</div>

<div onload="run()">
	<input style="display:none" id="email" type="text" name="email" placeholder="{{user}}" value="{{user}}" tabindex="1" autofocus="autofocus" class="form-control input-medium">
	<button style="display:none" type="button" tabindex="4" class="btn btn-primary logreg" id="regBtn" >Register</button>
</div>

<script src="/js/messageJQ.js"></script>
<script src="/js/message.js"></script>
% include('bottom.tpl')

</body>
</html>
