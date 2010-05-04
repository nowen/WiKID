=====================================================================
About WiKIDAuthPlugin

WiKIDAuthPlugin is a Plone PAS plugin that once installed in the user 
folder will enable WiKID two-factor authentication for your Plone site.

This is a bare-bones proof-of-concept release.  You currently need to 
change the following WiKID settings on lines 72-77 of WiKIDAuthPlugin.py:

    domaincode = '127000000001'
    host = '127.0.0.1'
    port = 8388
    caCert = '/opt/Plone-3.0.6/zinstance/Products/WiKIDAuthPlugin/WiKID-ca.pem'
    pkey = '/opt/Plone-3.0.6/zinstance/Products/WiKIDAuthPlugin/plone.p12'
    passPhrase = 'passphrase'

to reflect your WiKID setup.

This plugin will work with both the open source Community and 
Enterprise Editions of the WiKID Strong Authentication Server Version 3.0 or 
higher.  

To learn more about two-factor authentication from WiKID please visit:
    http://www.wikidsystems.com

Requires pyOpenSSl:
To install pyopenssl for the unifiedinstaller version, download the pyopenssl source, 
cd to the source directory and run setup.py using the bundled python:

/opt/Plone-3.0.6/Python-2.4.4/bin/python setup.py install 

This product is based on the GMailAuthPlugin.  

=====================================================================
About wClient-Python
=====================================================================

wClient-Python is a class for communicating with the WiKID Strong
Authentication System.

	http://www.wikidsystems.net/product-info-downloads/network-clients

It is available under the GNU Lesser General Public License.

The pyexample.py file is a command line tool to test WiKID functionality.  

*** NOTE *** 
This package is only compatible with version 3.0 or later of the 
WiKID Server.  There is an earlier version available on SourceForge
if you are still running the v2 Server.  So why not take this 
opportunity to upgrade?  :)  That's also available on SF.....

=====================================================================
About WiKID
=====================================================================

Hate passwords?

WiKID is a dual-source two-factor authentication system. It consists of: 
a PIN, stored in the user's head; a small, lightweight client that 
encapsulates the private/public keys; and a server that stores 
the public keys of the client's and the user's PIN. When the user 
wants to login to a service, they start the client and enter their 
PIN, which is encrypted and sent to the server. If the PIN is 
correct, the account active and the encryption valid, the user is 
sent a one-time passcode to use instead of a static password.

You can think of WiKID as 'certificates on steroids'. It is more 
secure than certificates because the required PIN is only stored on 
the server, so it is not susceptible to offline passive attacks. It 
is easier because user enrollment is automated and you don't have to 
deal with a full certiticate infrastructure. You can also compare 
WiKID to hardware tokens: it is much easier to implement, more 
extensible, yet just as secure. Stealing either the token or the PIN 
does you no good. You must steal both, just like a hardware token. 

More information about WiKID may be found online at

    http://sourceforge.net/projects/wikid-twofactor
    http://www.wikidsystems.com/

=====================================================================
Copyright @COPYRIGHT@
@VENDOR_URL@
