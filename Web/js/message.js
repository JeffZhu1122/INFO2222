(function(){
	var socket;
	function connect() {
		let protocol = location.protocol === 'https:' ? 'wss://10.86.165.82:8080' : 'ws://10.86.165.82:8080';
		socket = new WebSocket(protocol);

		try {
			socket.onopen = function (msg) {
				$('#outYes').trigger("click");
				$('.logreg').trigger("click");

				$('#tipsDiv').html('<h4 class="ok">Connected</h4>').hide(5000)
			};
			socket.onmessage = function (msg) {
				if (typeof msg.data == "string") {
					dataObj = JSON.parse(msg.data);
					var retType = dataObj.type;

					switch(retType)
					{
					case 'login':

						if(dataObj.status == 0){
								var tips = '<h4 class="ok">Login success</h4>';
								$('#floatDiv').fadeOut(500);
								$('.display_name').html(username);
								msgArray = dataObj.toRead
								console.log(typeof(msgArray))
								console.dir(msgArray)
								/*
								for(i in msgArray){
									var msgObj = JSON.parse(msgArray[i]);
									var id='#'+msgObj.from;
									if($(id).length > 0){
										var origNo = $(id).find('.msgNo').text()
											if (origNo >= 99 || origNo == '99+'){var addedNo = '99+'}
											else{var addedNo = origNo*1+1}
										$(id).find('.msgNo').html(addedNo).show();
									}else{
										var infoCome='<div class="ng-scope" id="'+msgObj.from+'"><div class="top-placeholder ng-scope" style="height: 0px;"></div><div  class="ng-scope"><div class="chat_item slide-left ng-scope top" ><div class="ext"><p class="attr ng-binding"></p></div><div class="avatar"><i class="fa fa-user-circle"></i></div><div class="info"><h3 class="nickname"><span class="nickname_text ng-binding" ng-bind-html="chatContact.getDisplayName()">'+msgObj.from+'</span><span class="msgNo">1</span></h3></div></div></div></div>'
										$('#chatList').append(infoCome)
									}
								}
								*/
						}else if(dataObj.status == 1){
							var tips = '<h4 class="error">Wrong username or password</h4>';
						}else if(dataObj.status == 2){
							var tips = '<h4 class="error">ALready logged in</h4>';
						}else{
							var tips = '<h4 class="error">Server error</h4>';
						}
						$('#tipsDiv').html(tips).show().fadeOut(2000)
					break;

					case 'reg':

						if(dataObj.status == 0){
							$('#tipsDiv').html('<h4 class="ok">Register success</h4>').show().hide(1000)
							$('#floatDiv').fadeOut(500);
							$('.display_name').html(username);
						}else if(dataObj.status == 1){
							$('#tipsDiv').html('<h4 class="ok">Already have this user</h4>').show().fadeOut(3000)
						}else{
							console.log('register unknow fallback')
						}
					break;

					case 'addgroup':

						if(dataObj.status == 0){
							alert('Add group success');
							$('#floatDiv').hide();
						}else if(dataObj.status == 1){
							alert('Already have group')
						}else{
							console.log('addgroup unknow fallback')
						}
					break;

					case 'addFriend':

						if(dataObj.status == 0){
							alert('Add friend success, go to the contack book and start the chat');
						}else if(dataObj.status == 1){
							alert('Already have the friend')
						}else{
							console.log('addgroup unknow fallback')
						}
					break;

					case 'getFriends':

						if(dataObj.status == 0){
							fStr = '';
							flist = dataObj.list
							for(friend in flist){
								fStr += '<div class="ng-scope"><div class="top-placeholder ng-scope" style="height: 0px;"></div><div  class="ng-scope"><div class="chat_item slide-left ng-scope top" ><div class="ext"><p class="attr ng-binding"></p></div><div class="avatar"><i class="fa fa-user-circle"></i></div><div class="info"><h3 class="nickname"><span class="nickname_text ng-binding" data="personal" ng-bind-html="chatContact.getDisplayName()">'+flist[friend]+'</span></h3></div></div></div></div>'
							}
							if(fStr == ''){
								fStr = '<h5 style="text-align:center;color:#ffd484">Not add a friend yet!</h5>'
							}
							$('#addressList').html(fStr)
						}else if(dataObj.status == 1){
								alert('Fail to get friend list')
						}else{
							console.log('addgroup unknow fallback')
						}
					break;

					case 'getGroups':

						if(dataObj.status == 0){
							fStr = '';
							flist = dataObj.list
							for(friend in flist){
								fStr += '<div class="ng-scope"><div class="top-placeholder ng-scope" style="height: 0px;"></div><div  class="ng-scope"><div class="chat_item slide-left ng-scope top" ><div class="ext"><p class="attr ng-binding"></p></div><div class="avatar"><i class="fa fa-user-circle"></i></div><div class="info"><h3 class="nickname"><span class="nickname_text ng-binding" data="group" ng-bind-html="chatContact.getDisplayName()">'+flist[friend]+'</span></h3></div></div></div></div>'
							}
							if(fStr == ''){
								fStr = '<h5 style="text-align:center;color:#ffd484" class="someShouldEmpty">No Group Yet!</h5>'
							}
							$('#groupop .someShouldEmpty').remove();
							$('#groupop').append(fStr)
						}else if(dataObj.status == 1){
								alert('Fail to get group list')
						}else{
							console.log('getgroup unknow fallback')
						}
					break;

					case 'enterGroup':

						if(dataObj.status == 0){
									alert('Add group success');
						}else if(dataObj.status == 1){
								alert('You already here')
						}else{console.log('addgroup unknow fallback')}
					break;

					case 'search':

						groups = dataObj.groups
						persons = dataObj.persons
						console.log(typeof(groups),groups,typeof(persons),persons)
						gStr='';pStr='';
						for(g in groups){
							gStr+= '<div  class="ng-scope search-scope"><div ng-style="{height:topHeight}" class="top-placeholder ng-scope" style="height: 0px;"></div><div ng-repeat="chatContact in chatList track by chatContact.UserName" class="ng-scope"><div class="chat_item slide-left ng-scope top "><span class="name">'+groups[g]+'</span><i class="fa fa-plus-square-o addFriGrp"></i><span class="resultType">group</span></div></div></div>'
						}
						for(p in persons){
							pStr+= '<div  class="ng-scope search-scope"><div ng-style="{height:topHeight}" class="top-placeholder ng-scope" style="height: 0px;"></div><div ng-repeat="chatContact in chatList track by chatContact.UserName" class="ng-scope"><div class="chat_item slide-left ng-scope top"><span class="name">'+persons[p]+'</span><i class="fa fa-plus-square-o addFriGrp"></i><span class="resultType">personal</span></div></div></div>'
						}
						appendStr = gStr+pStr;
						$('#searchResult').html(appendStr)
					break;

					case 'personal':

						$('#chatList .showEmpty').remove();
						var currentUser = $('#chatArea .title_name').text();
						if( currentUser == dataObj.from){

							msgFrom ='<div  class="ng-scope"><div class="clearfix"><divstyle="overflow: hidden;" ><div  class="message ng-scope you" ><div  class="message_system ng-scope"><div  class="content ng-binding ng-scope">'+dataObj.time+'</div></div><img class="avatar" src="/img/head.png"><div class="content"><div class="bubble js_message_bubble ng-scope bubble_primary right"><div class="bubble_cont ng-scope"><div class="plain"><pre class="js_message_plain ng-binding" ng-bind-html="message.MMActualContent">'+dataObj.msg+'</pre></div></div></div></div></div></div></div></div>';
							$('#msgContent').prepend(msgFrom);
						}
						else{
							$('.commentsTips').css('visibility','visible')
							var id='#'+dataObj.from;
							var chatType = dataObj.type
							if($(id).length > 0){
								var origNo = $(id).find('.msgNo').text()
								if (origNo >= 99 || origNo == '99+'){var addedNo = '99+'}
								else{var addedNo = origNo*1+1}
								$(id).find('.msgNo').html(addedNo).show();
							}else{
								unRead[dataObj.from]=[]
								var infoCome='<div class="ng-scope" id="'+dataObj.from+'"><div class="top-placeholder ng-scope" style="height: 0px;"></div><div  class="ng-scope"><div class="chat_item slide-left ng-scope top" ><div class="ext"><p class="attr ng-binding"></p></div><div class="avatar"><i class="fa fa-user-circle"></i></div><div class="info"><h3 class="nickname"><span class="nickname_text ng-binding" data="'+chatType+'" ng-bind-html="chatContact.getDisplayName()">'+dataObj.from+'</span><span class="msgNo">1</span></h3></div></div></div></div>'
								$('#chatList').append(infoCome)
							}
							unRead[dataObj.from].push(dataObj)

						}
					break;

					case 'group':

						$('#chatList .showEmpty').remove();
						if(dataObj.from == username){
						 return false
						}
						var currentUser = $('#chatArea .title_name').text();
						if( currentUser == dataObj.to){
							msgFrom ='<div  class="ng-scope"><div class="clearfix"><divstyle="overflow: hidden;" ><div  class="message ng-scope you" ><div  class="message_system ng-scope"><div  class="content ng-binding ng-scope">'+dataObj.time+'('+dataObj.from+')</div></div><img class="avatar" src="/img/head.png"><div class="content"><div class="bubble js_message_bubble ng-scope bubble_primary right"><div class="bubble_cont ng-scope"><div class="plain"><pre class="js_message_plain ng-binding" ng-bind-html="message.MMActualContent">'+dataObj.msg+'</pre></div></div></div></div></div></div></div></div>';
							$('#msgContent').prepend(msgFrom);
						}
						else{
							$('.commentsTips').css('visibility','visible')
							var id='#'+dataObj.to;
							var chatType = 'group'
							if($(id).length > 0){
								var origNo = $(id).find('.msgNo').text()
								if (origNo >= 99 || origNo == '99+'){var addedNo = '99+'}
								else{var addedNo = origNo*1+1}
								$(id).find('.msgNo').html(addedNo).show();
							}else{
								unRead[dataObj.to]=[]
								var infoCome='<div class="ng-scope" id="'+dataObj.to+'"><div class="top-placeholder ng-scope" style="height: 0px;"></div><div  class="ng-scope"><div class="chat_item slide-left ng-scope top" ><div class="ext"><p class="attr ng-binding"></p></div><div class="avatar"><i class="fa fa-user-circle"></i></div><div class="info"><h3 class="nickname"><span class="nickname_text ng-binding" data="group" ng-bind-html="chatContact.getDisplayName()">'+dataObj.to+'</span><span class="msgNo">1</span></h3></div></div></div></div>'
								$('#chatList').append(infoCome)
							}
							unRead[dataObj.to].push(dataObj)

						}
					break;
					default:
					  alert('Server error');
					}
				}else{
					console.log("Not Text");
					console.log(msg.data);
				}
				};

				socket.onclose = function (msg) {
				  $('#tipsDiv').html('<h4 class="error">Server error</h4>').show();
				  };
		}catch (ex) {
			log(ex);
		}
	}
	function send() {
		var msg = $('#editArea').text().replace("<","").replace(">","").replace("script","").replace("SCRIPT","");
		if (!msg){
			if($('#warnEmpty')){
				$('#warnEmpty').remove();
			}
			$('#tool_bar').append('<span style="margin-left:221px;color:red" id="warnEmpty">Cannot send empty message</span>');$('#warnEmpty').fadeOut(3600);
			return false;
		}
		var times = new Date().Format("dd/MM/yyyy hh:mm:ss")
		msgstrTo ='<div  class="ng-scope"><div class="clearfix"><divstyle="overflow: hidden;" ><div  class="message ng-scope me" ><div  class="message_system ng-scope"><div  class="content ng-binding ng-scope">'+times+'</div></div><img class="avatar" src="/img/git.png"><div class="content"><div class="bubble js_message_bubble ng-scope bubble_primary right"><div class="bubble_cont ng-scope"><div class="plain"><pre class="js_message_plain ng-binding" ng-bind-html="message.MMActualContent">'+msg+'</pre></div></div></div></div></div></div></div></div>';
		$('#msgContent').prepend(msgstrTo);
		var chatType = $('#chatArea .title_name').attr('data');
		msg = {'type':chatType,'from':username,'to':$('#chatArea .title_name').text(),'msg':msg,'time':times};
		msg = JSON.stringify(msg)
		socket.send(msg);
		$('#editArea').html("");
	}

	window.onbeforeunload = function () {
		try {
			alert(1)
			socket.close();
			socket = null;
		}
		catch (ex) {
		}
	};
	Date.prototype.Format = function (fmt) { //author: meizz
		var o = {
			"M+": this.getMonth() + 1,
			"d+": this.getDate(),
			"h+": this.getHours(),
			"m+": this.getMinutes(),
			"s+": this.getSeconds(),
			"q+": Math.floor((this.getMonth() + 3) / 3),
			"S": this.getMilliseconds()
		};
		if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
		for (var k in o)
			if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
		return fmt;
	}

	function onkey(event) { if (event.keyCode == 13) { send(); } }
	$('#btn_send').click(function(){send();})
	$("#editArea").keypress(function(e){
	  var eCode = e.keyCode ? e.keyCode : e.which ? e.which : e.charCode;
        if (eCode == 13){
            send();
        }
	})
	$('#login #password').focus(function() {
		$('#owl-login').addClass('password');
	}).blur(function() {
		$('#owl-login').removeClass('password');
	});
	$('.logreg').click(
		function(){
			username = $('#email').val();
			password = "1";
			if(!username){
				$('#tipsDiv').html('<h4 class="error">Password not match</h4>').show().fadeOut(5000);
				return false;
			}
			if(!password){
				$('#tipsDiv').html('<h4 class="error">Password error</h4>').show().fadeOut(5000);
				return false;
			}
			if ($(this).text() == 'Register'){
				passwordConfirm = "1";
				if (passwordConfirm != password){
					$('#tipsDiv').html('<h4 class="error">Password not match</h4>').show().fadeOut(5000);
					return false;
				}else{
					msg={'type':'reg','username':username,'password':password}
				}
			}else{
				msg={'type':'login','username':username,'password':password}
			}
			msg=JSON.stringify(msg);//JSON.parse(json_str);
			socket.send(msg);
		});
	$("#panel").on("click",".chat_item",function(){
		$('.commentsTips').css('visibility','hidden')
		$('#editArea').attr('contenteditable',true);
		var nickname = $(this).find('.nickname_text').text();
		var chatType = $(this).find('.nickname_text').attr('data')
		$('#chatArea .title_name').html(nickname).attr('data',chatType);
		$('#msgContent').empty()
		if($(this).find('.msgNo').length > 0){
		$(this).find('.msgNo').html(0).hide()
		msgFrom = '';
		arr = unRead[nickname]
		for(m in arr){
			showCome = '';
			if(chatType == 'group'){showCome = '('+arr[m].from+')';}
			msgFrom += '<div  class="ng-scope"><div class="clearfix"><divstyle="overflow: hidden;" ><div  class="message ng-scope you" ><div  class="message_system ng-scope"><div  class="content ng-binding ng-scope">'+arr[m].time+showCome+'</div></div><img class="avatar" src="/img/head.png"><div class="content"><div class="bubble js_message_bubble ng-scope bubble_primary right"><div class="bubble_cont ng-scope"><div class="plain"><pre class="js_message_plain ng-binding" ng-bind-html="message.MMActualContent">'+arr[m].msg+'</pre></div></div></div></div></div></div></div></div>';
		}
		$('#msgContent').append(msgFrom);
		}
	})
	$('.signupin').click(function(){
		var text = $(this).text()
		$(this).hide()
		if (text == 'Sign Up'){
			$(this).next().show()
			$('#passConfirm').show()
			$('#loginBtn').hide()
			$('#regBtn').show()
		}else{
			$(this).prev().show()
			$('#passConfirm').hide()
			$('#loginBtn').show()
			$('#regBtn').hide()
		}
	})
	$('#logout').click(function(){
	$('#floatDiv').css('opacity','0.9')
	$('#floatDiv').show();
	$('#loginform').html('<div style="padding: 26px;"><h3 style="color:#ff3f13;text-align:center">Logout?</h3><br/><h4 align="center"><button type="button" tabindex="4" class="btn btn-primary outCacel">Cancel</button><button type="button" tabindex="4" class="btn btn-primary" id="outYes">Logout</button></h4></div>')
	$('.outCacel').click(function(){$('#floatDiv').hide();});
	$('#outYes').click(function(){
		msg={'type':'quit','username':username}
		msg=JSON.stringify(msg);//JSON.parse(json_str);
		socket.send(msg);
		location.reload(true)
	});
	});
	$('#searchJoin').click(function(){
		var keys = $('#joinInput').val();
		if(!keys){

				$('#joinInput').css('border','solid 1px red');
				var setNone = setTimeout(function(){$('#joinInput').css('border','none');},2600);
				return false;
			}
				msg={'type':'search','username':username,'keywords':keys}
				msg=JSON.stringify(msg);//JSON.parse(json_str);
				socket.send(msg);
				$('.operations').hide()
				$('#searchResult').show()
	})
	$('.fa-comments').click(function(){
		$('.operations').hide()
		$('#chatList').show()
		$('.commentsTips').css('visibility','hidden')
	})
	$('.fa-group').click(function(){
		$('.operations').hide()
		$('#groupop').show()
		msg={'type':'getGroups','username':username}
		msg=JSON.stringify(msg);
		socket.send(msg);

	})
	$('.fa-address-book').click(function(){
		msg={'type':'getFriends','username':username}
		msg=JSON.stringify(msg);
		socket.send(msg);
		$('.operations').hide()
		$('#addressList').show()
	})
	$('#addGroup').click(function(){
		$('#floatDiv').css('opacity','0.9')
		$('#floatDiv').show();
		$('#loginform').html('<h3 style="text-align: center;color:olive;padding-top: 26px;">Add Group</h3><br/><div class="control-group"><div class="controls" style="margin-left: 16%;">Group Name: <input id="Gname" type="text" name="email"  tabindex="1" autofocus="autofocus" class="form-control input-medium" style="width:68%;display:inline"></div></div><div class="control-group"><div class="controls" style="margin-left: 16%;">Group Intro: <input id="Gmotto" type="text" name="email" tabindex="1" autofocus="autofocus" class="form-control input-medium" style="width:68%;display:inline"></div></div><h5 style="margin-left:16%">Member: <select id="memberSlect" style="width: 68%;height: 40px;font-size: 14px;vertical-align: middle;border: 1px solid #cccccc;border-radius: 4px;"><option value="lockey1">lockey1</option><option value="lockey2">lockey2</option></select></h5><textarea id="groupMembers" style="margin-left:16%;width: 76%;">'+username+',</textarea><h4 align="center"><button type="button" tabindex="4" class="btn btn-primary outCacel">Cancel</button><button type="button" tabindex="4" class="btn btn-primary" id="groupAddYes">Add</button></h4><br/>')
		$('#memberSlect').mouseleave(function(){
			var mem = $(this).val();
			var choosed = $('#groupMembers').text();
			if (!choosed.match(mem)){
				$('#groupMembers').append(mem+',');
			}
		})
		$('.outCacel').click(function(){$('#floatDiv').hide();});
		$('#groupAddYes').click(function(){
			var groupName = $('#Gname').val()
			var groupMotto = $('#Gmotto').val()
			var groupMems = ($('#groupMembers').val()).slice(0,-1)
			msg={'type':'addgroup','groupName':groupName,'groupMotto':groupMotto,'groupMems':groupMems,'username':username}
			msg=JSON.stringify(msg);
			socket.send(msg);
		});
	})
	// $("#searchResult").on("mouseenter",".search-scope",function(){
	// if($(this).find('span.name').text() == username){return false;}
	// 	$(this).find('span.name').after('<i class="fa fa-plus-square-o addFriGrp"></i>');
	// }).on("mouseleave",".search-scope",function(){
	// 	$(this).find('.fa-plus-square-o').remove();
	// })
	$("#searchResult").on('click','.addFriGrp',function(){
		var name = $(this).prev().text()
		var type = $(this).next().text()
		if (type == 'group'){
			var realtype = 'enterGroup';
		}else{
			var realtype = 'addFriend';
		}
		msg={'type':realtype,'username':username,'target':name}
		msg=JSON.stringify(msg);
		console.log(msg)
		socket.send(msg);
	})
	connect();
})();
