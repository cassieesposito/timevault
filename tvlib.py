#!/usr/bin/python

import MySQLdb

### IMPORTANT: THIS MUST BE UPDATED WITH YOUR MYSQL CREDENTIALS ###
db=MySQLdb.connect (host="HOSTNAME",
                       user="USERNAME",
                       passwd="PASSWORD",
                       db="DATABASE")

cur=db.cursor()

#Preprocess a stored e-mail for sending or display                           
def rowToDict(row):
	message = {'submitTime' : row[0]}
	message['sendTime'] = row[1]
	message['from'] = str(row[2]) + " <" + row[3] + ">"
	message['to'] = str(row[4]) + " <" + row[5] + ">"
	message['subject'] = str(row[6])
	message['body'] = "This is an e-mail from the past.\nIt was sent on "
	message['body'] += (row[0].strftime("%A, %B %e, %Y at %l:%M %p UTC."))
	message['body'] += "\n\n" + str(row[7])
	message['key'] = row[8]
	message['confirmed'] = row[9]
	return message

def getMessage(key):
	cur.execute ("SELECT * FROM `emailQueue` WHERE `confirmationKey`=%s",key)
	return rowToDict(cur.fetchone())

#HTTP Response, top part of document template
def printHeader():
	print "Content-type: text/html"
	print
	print "<html>"
	print "<head></head>"
	print "<body>"
	
	
#HTTP Response, bottom part of document template
def printFooter():
	print "</body>"
	print "</html>"