#!/usr/bin/python

import cgi
import tvlib


def main():
	key=cgi.FieldStorage().getvalue('key')
	tvlib.printHeader()
	tvlib.cur.execute ('UPDATE `emailQueue` SET `confirmed`=1 WHERE `confirmationKey`=%s',key)
	print "confirmed"
	tvlib.printFooter()
	
main()