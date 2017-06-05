#!/usr/bin/env python3.5
# This script is for checking expiration date of domains and alerting 
# Created by Constantine @ 2017 vi127001 [at] gmail.com

# Global variables
maiserver = "smtp.gmail.com"
maillogin = "someuser@gmail.com"
mailpass = "strongpass"
mailto = ['user1@gmail.com', 'user2@gmail.com']
domains = ['ya.ru','gmail.com']
alertdays = 32 # how many days before alerting

# Import modules
import whois
import datetime
import os
import smtplib


# Email function
def sendEMail(text, maiserver, maillogin, mailpass, mailto, mailtheme):
	for addr in mailto:
		server = smtplib.SMTP(maiserver, 587)
		server.set_debuglevel(1)
		server.ehlo()
		server.starttls()
		server.login(maillogin, mailpass)
		message = "\r\n".join([ \
			"From: "+maillogin, \
			"To: "+addr, \
			"Subject: "+mailtheme, \
			"", \
			"{}".format(text) \
			])
		server.sendmail(maillogin, mailto, message)
		server.quit()


# Domain check function
def checkdomain(www):
	try:
		dn = whois.whois(www)
	except Exception as e:
		print (e)
		os.exit(1)
	return (dn)



#Checking expiration date and alerting (main entrance)
if __name__ == '__main__':
	for x in domains:
		domain = checkdomain(x.rstrip())
		if domain.expiration_date == None:
			pass
		else:
			if type(domain.expiration_date) == list:
				if int((domain.expiration_date[0]-datetime.datetime.now()).days)<alertdays:
					msg = ('The domain '+x+' has been expired at '+ str(domain.expiration_date[0])+' so the domain will expired after '+str((domain.expiration_date[0]-datetime.datetime.now()).days)+' days.')
					print (msg)
					mailtheme = "Alert!!! Domain "+x+" will expired after"+str((domain.expiration_date[0]-datetime.datetime.now()).days)+" days."
					sendEMail(msg, maiserver, maillogin, mailpass, mailto, mailtheme)
				else:
					pass
			else:
				if int((domain.expiration_date-datetime.datetime.now()).days)<alertdays:
					msg = ('The domain '+x+' has been expired at '+ str(domain.expiration_date)+' so the domain will expired after '+str((domain.expiration_date-datetime.datetime.now()).days)+' days.')
					print (msg)
					mailtheme = "Alert!!! Domain "+x+" will expired after"+str((domain.expiration_date-datetime.datetime.now()).days)+" days."
					sendEMail(msg, maiserver, maillogin, mailpass, mailto, mailtheme)
				else:
					pass
else:
	pass


