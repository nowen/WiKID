''' wClient.py
Python Client for wikid '''

from OpenSSL import *
from xml.dom import minidom, Node
import sys, re, select, socket, os, traceback, time

__author__ = "Manish Rai Jain <manishrjain@gmail.com>"

DEBUGGING = True

def DEBUG(s):
	if DEBUGGING == True:
		print s

def verify_cb(conn, cert, errnum, depth, ok):
	# Modify here
	print 'Got certificate: %s' % cert.get_subject()
	return ok

class pywClient:
	
	def __init__(self, filename=None, host=None, port=None, pkey=None, passPhrase=None, caCert=None):
		"This will create a SSL Connection b/w client and server"
		
		DEBUG("DEBUG activated")
		self.filename = filename
		self.host = host
		self.port = port
		self.pkey = pkey
		self.passPhrase = passPhrase
		self.cacert = caCert

		if filename!=None:
			# Parse the properties file here
			print ''

		#ctx = SSL.Context(SSL.TLSv1_METHOD)
		ctx = SSL.Context(SSL.SSLv3_METHOD)
		ctx.set_verify(SSL.VERIFY_PEER, verify_cb)
#		ctx.set_verify(SSL.VERIFY_NONE, verify_cb)
		ctx.load_verify_locations(self.cacert)

		#Get X509 certificate and the private key from the 
		#initial .p12 file provided to network client
		f = open(pkey)
		
		pkcs12Obj = crypto.load_pkcs12(f.read(), passPhrase)
		pkeyObj = pkcs12Obj.get_privatekey()
		x509Obj = pkcs12Obj.get_certificate()
		
		ctx.use_privatekey(pkeyObj)
		ctx.use_certificate(x509Obj)
		
#		ctx.load_verify_locations(ca_cert)
		
		self.sock = SSL.Connection(ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
		self.gotConnection = False
		

	def xmlrequest(self, message=None):
		"Send XML request over the socket and return the XML response."
		DEBUG("XML message:")
		DEBUG(message)
		DEBUG("--------------------------------")
		message = message.replace('\n', '')
		message = message.replace('\r', '')
		message = message + "\n"
		#message = '<?xml version="1.0" encoding="UTF-8"?>\n' + message
		response = self.request(message)
		DEBUG("XML response:")
		DEBUG("--------------------------------")
		DEBUG(response)
		DEBUG("--------------------------------")
		try:
			doc = minidom.parseString(response)
			DEBUG("XML doc:")
			DEBUG(doc)
			DEBUG("--------------------------------")
			node = doc.documentElement
			DEBUG("XML node:")
			DEBUG(node)
			DEBUG("--------------------------------")
		except Exception, error:
			DEBUG("Error: %s" % error)
			sys.exit(1)

		return node

	def request(self, message=None):
		"Send request over the socket and return the response."

		if self.reconnect() != True:
			DEBUG('Unable to connect to the server. Exiting...')
			sys.exit(-1)

		response = ''
		try:
			DEBUG('Sending request: ' + message)
			totalsent = 0
			sent = self.sock.send(message)
			if sent == 0:
				raise RuntimeError, "socket connection broken"
				totalsent = totalsent + sent
# not quite working:
#			DEBUG('Bytes sent: %s ' % totalsent)
#			while True:
#				data = self.sock.recv(100)
#				DEBUG('data chunk: %s ' % data)
#				if not data: break

# SOURCE: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/408859
			self.sock.setblocking(0)
			timeout = 2
			data='';begin=time.time()
			while 1:
				#if you got some data, then break after wait sec
				if response and time.time()-begin>timeout:
					break
				#if you got no data at all, wait a little longer
				elif time.time()-begin>timeout*2:
					break
				try:
					data=self.sock.recv(8192)
					if data:
						response = response + data
						begin=time.time()
					else:
						time.sleep(0.1)
				except:
					pass
			DEBUG('Response received: ' + response)
		except Exception, err:
			DEBUG ("Error connecting: %s" % (err))
			print sys.exc_info()
			self.gotConnection = False

		return response

	def reconnect(self):
		"Reconnect to the server in case connection drops out."
		DEBUG(dir(self))
		if self.gotConnection == False:
			DEBUG("Reconnecting to host ...")
			try:
				self.sock.connect((self.host,self.port))
				DEBUG("Reconnected to host. Trying Handshake...")
				self.sock.do_handshake()
				DEBUG("Handshaking done")
				self.gotConnection = True # self.startConnection()
			except SSL.Error:
				DEBUG('Oops! Reconnection also failed')
				self.gotConnection = False
		
		return self.gotConnection
	
	def ping(self):
		"Send a ping to the server, to make sure it's open"
		message = "<transaction> <type>1</type> <data> <value>TX</value> </data> </transaction>"
		self.xmlrequest(message)

	def showNode(node):
		if node.nodeType == Node.ELEMENT_NODE:
			print 'Element name: %s' % node.nodeName
			for (name, value) in node.attributes.items():
				print '    Attr -- Name: %s  Value: %s' % (name, value)
			if node.attributes.get('ID') is not None:
				print '    ID: %s' % node.attributes.get('ID').value

	def checkCredentials(self, user=None, domaincode=None, passcode=None, challenge=None, response=None):
		return self.verify(user, "base", domaincode, passcode, challenge, response, chap_password='', chap_challenge='', wikid_challenge=None)

	def verify(self, format, user=None, domaincode=None, passcode=None, challenge=None, response=None, 
							chap_password=None, chap_challenge=None, wikid_challenge=None):
		"This helper method verifies credentials using the specified mechanism"

		xml = """<transaction>
	<type format="%s">2</type>
    <data>
        <user-id>%s</user-id>
        <passcode>%s</passcode>
        <domaincode>%s</domaincode>
        <offline-challenge encoding="none">%s</offline-challenge>
        <offline-response encoding="none">%s</offline-response>
        <chap-password encoding="none">%s</chap-password>
        <chap-challenge encoding="none">%s</chap-challenge>
        <result>null</result>
    </data>
</transaction>

""" % (format, user, passcode, domaincode, challenge, response, chap_password, chap_challenge)

		self.validCredentials = False

		try:
			response = self.xmlrequest(xml)
			result = response.getElementsByTagName("result")[0].firstChild.data
			if result == 'VALID':
				self.validCredentials = True
		except SSL.Error:
			self.gotConnection = False
		
		return self.validCredentials
	

	def chapVerify(self, user=None, domaincode=None, chap_password=None, chap_challenge=None, wikid_challenge=None):
		
		if wikidChallenge==None:
			format="chapOff"
		else:
			format="chap"

		return self.verify(user, format, domaincode, passcode, '', '', chap_password, chap_challenge, wikid_challenge)


	def registerUsername(self, uname=None, regcode=None, domaincode=None, passcode=None):
		"This method creates an association between the userid and the device registered by the user."
		
		if passcode != None and len(passcode) > 0:
			DEBUG("Adding new device ...")
			command = "ADDREGUSER"
			type = 4;
			passcodeline = "<passcode>%s</passcode>" % passcode;
			format = "add";
		else:
			DEBUG("Registering user ...")
			command = "REGUSER"
			type = 4;
			passcodeline = "";
			format = "new";

		message = """<transaction>
    <type format="%s">%s</type>
    <data>
    <user-id>%s</user-id>
    <registration-code>%s</registration-code>
    <domaincode>%s</domaincode>
    %s
    <error-code>null</error-code>
    <result>null</result>
    </data>
</transaction>
""" % (format, type, uname, regcode, domaincode, passcodeline)

		try:
			response = self.xmlrequest(message)
			result = response.getElementsByTagName("result")[0].firstChild.data
			DEBUG("result = %s" % result)
			if result == 'SUCCESS' or result == "SUCESS":
				self.connected = True
			else:
				return result
		except SSL.Error:
			self.gotConnection = False
		except:
			DEBUG('Problem in parsing the reply')
			return 2
		DEBUG('Error reading from server')
		return 2
		
	def startConnection(self):
		"Authentication procedure completed. Start off connection with the server now."
		DEBUG("startConnection() ...")
		mesg = "WiKID Python Client v3.0"
		message = """<transaction> <type>1</type> <data> <client-string>%s</client-string> <server-string>null</server-string> <result>null</result> </data> </transaction>
""" % (mesg)
		self.connected = False
		try:
			response = self.xmlrequest(message)
			result = response.getElementsByTagName("result")[0].firstChild.data
			if result == 'ACCEPT':
				self.connected = True
		except SSL.Error:
			self.gotConnection = False
		
		return self.connected
	
	
	def getDomains(self):
		"To be implemented. Has to be tested"
		DEBUG('getDomains: Still to be implemented')

		message = """<transaction> <type>3</type> <data> <domain-list>null</domain-list> </data> </transaction>""" 

		response = self.xmlrequest(message)
		result = response.getElementsByTagName("domain-list")[0]
		print result


if __name__ == "__main__":
	"Testing purposes"

	w = pywClient(host='127.0.0.1', port=8388, pkey='localhost.p12', passPhrase='secret', caCert='WiKID-ca.pem')
	w.startConnection()
	if w.checkCredentials(user='username', domaincode='127000000001', passcode='passhphrase'):
		print 'Cool Valid user'
	else:
		print 'No lah! No Entry!'
	print w.registerUsername(uname='uname', regcode='register', domaincode='haha')
