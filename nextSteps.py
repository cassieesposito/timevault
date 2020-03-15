#!/usr/bin/python

import cgi
import tvlib
import random
import string
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from datetime import date


def main():
	form = cgi.FieldStorage()
	tvlib.printHeader()

	if validDate(form):
		try:
			key=saveMessage(form)
			sendConfirmationEmail (key)
		except:
			describeError(form, "Did you forget to include your e-mail address, the recipient's e-mail address, or the date?")
		
	
	       
	tvlib.printFooter()
	tvlib.db.commit()
	tvlib.db.close()



def saveMessage (form):
	
	sendTime=form.getvalue("year") + "-" + form.getvalue("month") + "-" + form.getvalue("day") + " 00:00:00" #The date provided by the user at midnight in a MySQL DATETIME format.

	#Create a string of 45 uppercase alphanumeric characters using SystemRandom
	confirmationKey = ''.join(random.SystemRandom().choice(string.ascii_uppercase+string.digits) for _ in range(45))

	#Save e-mail to database for future reference
	cmd = "INSERT INTO `emailQueue` (`sendTime`, `fromName`, `fromEmail`, `toName`, `toEmail`, `subject`, `body`, `confirmationKey`) VALUES (%s, %s,%s, %s, %s, %s, %s, %s)"
	args = (sendTime, form.getvalue("fromName"), form.getvalue("fromEmail"), form.getvalue("toName"), form.getvalue("toEmail"), form.getvalue("subject"), form.getvalue("body"), confirmationKey)
	#args = (sendTime, form.getvalue("fromName"), "move", form.getvalue("toName"), "davi@timevault.org", form.getvalue("subject"), form.getvalue("body"), confirmationKey)
	tvlib.cur.execute(cmd,args)

	return confirmationKey




def validDate (form):
	valid=True

	try:
		if date.today() > date(int(form.getvalue("year")), int(form.getvalue("month")), int(form.getvalue("day"))):
			valid=False
			describeError(form, "We can't send an e-mail to the past for you, that would violate the temporal prime directive!")
			
	except:	
		valid=False
		describeError(form,"You've entered an invalid date")
		
	return valid




def sendConfirmationEmail (key):
	message=tvlib.getMessage(key)
	
	
	body = "You're one step away from sending your e-mail in to the future. All you need to do is click on the link below:\n" \
			 "http://www.timevault.org/confirm.py?key=%s" %key
	
	toSend = MIMEText(body)
	toSend["From"] = "system@EXAMPLE.COM"
	toSend["To"] = message['from']
	toSend["Subject"] = 'E-mail the future with "' + message['subject'] + '"'
	p = Popen(["/usr/bin/sendmail", "-t"], stdin=PIPE)
	p.communicate(toSend.as_string())
	
	print "We've sent you an e-mail with a link to confirm your e-mail address. You'll need to click on it in order " \
	      "to schedule delivery at %s" % message['sendTime']
	
	

def describeError(form=0, error=0):
	print "Oops, there was an error!<br/>"
	if error:
		print "%s<br />" % error
	print 'Go back and try again! If you keep getting this error, try e-mailing <a href="mailto:webmaster@EXAMPLE.COM">webmaster@EXAMPLE.COM</a><br />'
	print "<br />"
	if form:
		print "Just in case you've got one of those terrible browsers that's going to lose your writing when you press the back button, here's a little bit of information about your e-mail:<br />"
		print "Subject: %s<br />" % form.getvalue("subject")
		print "Body: %s<br />" % form.getvalue("body")

main()


