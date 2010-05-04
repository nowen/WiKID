from pywClient import pywClient
import sys

print 'Creating connection...'

host = '127.0.0.1'
port = 8388
pkey = 'localhost.p12'
passPhrase = 'changeme'
correct = 'n'

while correct != 'y':
	host = raw_input('Please enter host: ')
	port = int(raw_input('Please enter port: '))
	pkey = raw_input('Please enter the p12 cert filename: ')
	passPhrase = raw_input('Please enter the passPhrase: ')
	correct = raw_input('Is this correct[y/n]: ')
	
w = pywClient(host=host,port=port,pkey=pkey,passPhrase=passPhrase)
print 'Connection created...'

# User Registration Section
print 'User Registration'
correct = 'n'
while correct != 'y':
	user = raw_input('Please enter user: ')
	regcode = raw_input('Please enter registration code: ')
	servercode = '127000000001'
	temp = raw_input('Please enter server code[127000000001]: ')
	if temp != '':
		servercode = temp
	print 'Regsitering user with this information'
	print 'user:', user
	print 'regcode:', regcode
	print 'servercode:', servercode
	correct = raw_input('Is this correct[y/n]: ')
res = w.registerUsername(uname=user, regcode=regcode, servercode=servercode)
if res==0:
	print 'Success'
else:
	print 'Failure. Result:', res
	
#User Registration Section finished

#User login - Check Credentials
print
print 'User Login'
correct = 'n'
while correct != 'y':
	user = raw_input('Please enter user: ')
	passcode = raw_input('Please enter passcode: ')
	servercode = '127000000001'
	temp = raw_input('Please enter server code[127000000001]: ')
	if temp != '':
		servercode = temp

	print 'Logging in with this information'
	print 'user:', user
	print 'passcode:', passcode
	print 'servercode:', servercode
	correct = raw_input('Is this correct[y/n]: ')
	
res = w.CheckCredentials(user=user, passcode=passcode, servercode=servercode)
if res == True:
	print 'Success'
else:
	print 'Failure.'

# User login section finished

#Offline Authentication section started
print
print 'Offline User Verification'
correct = 'n'
while correct != 'y':
	user = raw_input('Please enter user: ')
	import random
#	challenge = raw_input('Please enter challenge: ')
	challenge = str(int(random.random()*pow(10,8)))
	print 'challenge:', challenge
	response = raw_input('Please enter response: ')
	servercode = '127000000001'
	temp = raw_input('Please enter server code[127000000001]: ')
	if temp != '':
		servercode = temp

	print 'Offline Verifying using this information'
	print 'user:', user
	print 'challenge:', challenge
	print 'response:', response
	print 'servercode:', servercode
	correct = raw_input('Is this correct[y/n]: ')

res = w.CheckCredentials(user=user,challenge=challenge,response=response,servercode=servercode)
if res == True:
	print 'Success'
else:
	print 'Failure'

#Offline Authentication section finished

#Addition of devices to existing user ids
print
print 'Adding devices to existing user id'
correct = 'n'
while correct != 'y':
	uname = raw_input('Please enter user: ')
	regcode = raw_input('Please enter registration code: ')
	servercode = '127000000001'
	temp = raw_input('Please enter server code[127000000001]: ')
	if temp != '':
		servercode = temp
	passcode = raw_input('Please enter pass code: ')

	print 'Addition of devices with continue with this information'
	print 'user:', user
	print 'regcode:', regcode
	print 'servercode:', servercode
	print 'passcode:', passcode
	correct = raw_input('Is this correct[y/n]: ')

res = w.registerUsername(uname=uname, regcode=regcode, servercode=servercode, passcode=passcode)
if res == 0:
	print 'Success'
else:
	print 'Failure with returned value:', res

#Addition of devices section finished


