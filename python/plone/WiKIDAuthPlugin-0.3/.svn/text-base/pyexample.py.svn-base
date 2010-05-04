from pywClient import pywClient
import sys

print 'Creating connection...'

host = '10.100.0.10'
port = 8388
pkey = 'support.p12'
passPhrase = 'wikidone'
correct = 'n'

while correct != 'y':
	host = raw_input('Please enter host: ')
	port = int(raw_input('Please enter port: '))
	pkey = raw_input('Please enter the p12 cert filename: ')
	passPhrase = raw_input('Please enter the passPhrase: ')
        caCert = raw_input('Please enter the CACertStore: ')
	correct = raw_input('Is this correct[y/n]: ')
	
w = pywClient(host=host,port=port,pkey=pkey,passPhrase=passPhrase,caCert=caCert)
print 'Connection created...'

# User Registration Section
print 'User Registration'
correct = 'n'
while correct != 'y':
	user = raw_input('Please enter user: ')
	regcode = raw_input('Please enter registration code: ')
	domaincode = '127000000001'
	temp = raw_input('Please enter server code[127000000001]: ')
	if temp != '':
		domaincode = temp
	print 'Regsitering user with this information'
	print 'user:', user
	print 'regcode:', regcode
	print 'domaincode:', domaincode
	correct = raw_input('Is this correct[y/n]: ')
res = w.registerUsername(uname=user, regcode=regcode, domaincode=domaincode)
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
	domaincode = '127000000001'
	temp = raw_input('Please enter server code[127000000001]: ')
	if temp != '':
		domaincode = temp

	print 'Logging in with this information'
	print 'user:', user
	print 'passcode:', passcode
	print 'domaincode:', domaincode
	correct = raw_input('Is this correct[y/n]: ')
	
res = w.checkCredentials(user=user, domaincode=domaincode, passcode=passcode)
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
	domaincode = '127000000001'
	temp = raw_input('Please enter server code[127000000001]: ')
	if temp != '':
		domaincode = temp

	print 'Offline Verifying using this information'
	print 'user:', user
	print 'challenge:', challenge
	print 'response:', response
	print 'domaincode:', domaincode
	correct = raw_input('Is this correct[y/n]: ')

res = w.checkCredentials(user=user,challenge=challenge,response=response,domaincode=domaincode)
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
	domaincode = '127000000001'
	temp = raw_input('Please enter server code[127000000001]: ')
	if temp != '':
		domaincode = temp
	passcode = raw_input('Please enter pass code: ')

	print 'Addition of devices with continue with this information'
	print 'user:', user
	print 'regcode:', regcode
	print 'domaincode:', domaincode
	print 'passcode:', passcode
	correct = raw_input('Is this correct[y/n]: ')

res = w.registerUsername(uname=uname, regcode=regcode, domaincode=domaincode, passcode=passcode)
if res == 0:
	print 'Success'
else:
	print 'Failure with returned value:', res

#Addition of devices section finished


