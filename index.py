#!/usr/bin/python

import datetime

print '''Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Welcome to the Time Vault!</title>
<link rel="stylesheet" type="text/css" href="view.css" media="all">
<script type="text/javascript" src="view.js"></script>
<script type="text/javascript" src="calendar.js"></script>
</head>
<body id="main_body" >
	
	<img id="top" src="top.png" alt="">
	<div id="form_container">

		<h1><a>Send E-mail to the Future</a></h1>
		<form id="form" class="appnitro"  method="post" action="nextSteps.py">
			<div class="form_description">
				<h2>Welcome to the Time Vault</h2>
				<p>Where you can send E-mail to the future!</p>
			</div>						
			<div style="overflow:hidden">
				<div class="newLine leftHalf">
					Your Name <br />
					<input id="fromName" name="fromName" type="text" maxlength="255" value="" />
				</div>
				<div class="rightHalf">
					Your E-mail Address <span style="color:red">* (required)</span> <br />
					<input id="fromEmail" name="fromEmail" type="text" maxlength="255" value="" />								
				</div>
				<div class="leftHalf">
					Recipient Name <br />
					<input id="toName" name="toName" type="text" maxlength="255" value="" />				
				</div>
				<div class="rightHalf">
					Recipient E-mail Address <span style="color:red">*</span> <br />
					<input id="toEmail" name="toEmail" type="text" maxlength="255" value="" />												
				</div>
				<div class="row">
					Subject <br />
					<input id="subject" name="subject" type="text" maxlength="255" class="large" value="" />
				</div>
				<div class="row">
					Body<br />
					<textarea id="body" name="body" class="textarea large"></textarea> 			
				</div>
				<div class="row">
					Date to Send E-mail (MM / DD / YYYY) <span style="color:red">*</span><br />
					<span><input id="cal_month" name="month" class="text" size="2" maxlength="2" value="" type="text" /> /</span>
					<span><input id="cal_day" name="day" class="text" size="2" maxlength="2" value="" type="text" /> /</span>
					<span><input id="cal_year" name="year" class="text" size="4" maxlength="4" value="" type="text" /></span>
					<span id="calendar_5"><img id="cal_img" class="datepicker" src="calendar.gif" alt="Pick a date." /></span>
					<script type="text/javascript">
						Calendar.setup({
							inputField	 : "cal_year",
							baseField    : "cal",
							displayArea  : "cal",
							button		 : "cal_img",
							ifFormat	 : "%B %e, %Y",
							onSelect	 : selectDate
						});
					</script>	
				</div>
				<div class="row">'''
print "				This system operates on UTC. This page was loaded on %s." % datetime.datetime.now().strftime("%A, %B %e, %Y at %l:%M %p")
print '''				</div>
				<div class="row">
						<input id="saveForm" class="button" type="submit" name="submit" value="Send E-mail" />
				</div>
	<img id="bottom" src="bottom.png" alt="">
	</body>
</html>
'''
