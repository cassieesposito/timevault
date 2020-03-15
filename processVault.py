#!/usr/bin/python

from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from datetime import datetime
import tvlib

def main():
	db=tvlib.connect() #connects to database using MySQLdb
	cur = db.cursor()

	#Return todays date in MySQL readable format, use the same date throughout the process.
	now=datetime.now().strftime("%Y-%m-%d")

	#Get all e-mails with a send date before today
	tvlib.cur.execute("SELECT * FROM `emailQueue` WHERE sendTime <= '{0}'".format(now))
	response = tvlib.cur.fetchall()

	for row in response:
		sendEmail(tvlib.rowToDict(row))

	#Delete all e-mails with a send date before today, whether or not they were sent.
	#tvlib.cur.execute("DELETE FROM `emailQueue` WHERE sendTime <= %s", now)
	tvlib.cur.execute("DELETE FROM `emailQueue` WHERE sendTime <= '{0}'".format(now))

	tvlib.db.commit()
	tvlib.db.close()



def sendEmail(message):
	if message['confirmed']:
		toSend = MIMEText(message['body'])
		toSend["From"] = message['from']
		toSend["To"] = message['to']
		toSend["Subject"] = message['subject']
		p = Popen(["/usr/bin/sendmail", "-t"], stdin=PIPE)
		p.communicate(toSend.as_string())


main()
