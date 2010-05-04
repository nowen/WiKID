"""WiKIDAuthPlugin
Copyright(C), 2008, WiKID Systems, Inc - ALL RIGHTS RESERVED

This software is licensed under the Terms and Conditions contained within the
LICENSE.txt file that accompanied this software.  Any inquiries concerning the
scope or enforceability of the license should be addressed to:

WiKID Systems, Inc.
1350 Spring St.
Suite 300
Atlanta, Ga 30309
info at wikidsystems.com 
866-244-1876
"""

from AccessControl import ClassSecurityInfo

from Globals import InitializeClass
from OFS.Cache import Cacheable

from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements
from Products.PluggableAuthService.interfaces.plugins import IAuthenticationPlugin

from zLOG import LOG
from  pywClient import pywClient
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

manage_addWiKIDAuthPluginForm = PageTemplateFile(
    'www/wikidAdd', globals(), __name__='manage_addWiKIDAuthPluginForm' )

def manage_addWiKIDAuthPlugin(dispatcher, id, title=None, REQUEST=None):
    """ Add a WiKIDAuthPlugin to a Pluggable Auth Service. """

    obj = WiKIDAuthPlugin(id, title)
    dispatcher._setObject(obj.getId(), obj)

    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect(
                                '%s/manage_workspace'
                                '?manage_tabs_message='
                                'WiKIDAuthPlugin+added.'
                            % dispatcher.absolute_url())

class WiKIDAuthPlugin(BasePlugin, Cacheable):

    """ PAS plugin for using WiKID credentials to log in.
    """

    meta_type = 'WiKIDAuthPlugin'

    security = ClassSecurityInfo()

    def __init__(self, id, title=None):
        self._id = self.id = id
        self.title = title
    

    #
    #   IAuthenticationPlugin implementation
    #
    #security.declarePrivate('authenticateCredentials')
    def authenticateCredentials(self, credentials):

        """ See IAuthenticationPlugin.

        o We expect the credentials to be those returned by
          ILoginPasswordExtractionPlugin.
        """
        login = credentials.get( 'login' )
        password = credentials.get( 'password' )
        domaincode = '127000000001'
        host = '127.0.0.1'
        port = 8388
        caCert = '/opt/Plone-3.0.6/zinstance/Products/WiKIDAuthPlugin/WiKID-ca.pem'
        pkey = '/opt/Plone-3.0.6/zinstance/Products/WiKIDAuthPlugin/laptop.p12'
        passPhrase = 'passphrase'
        w = pywClient(host=host, port=port, pkey=pkey, passPhrase=passPhrase, caCert=caCert)

        if login is None or password is None:
           return None
        res = w.checkCredentials(login, domaincode, password)
        if res == True:
            return login, login
        else:
            print None
 
classImplements(WiKIDAuthPlugin, IAuthenticationPlugin)

InitializeClass(WiKIDAuthPlugin)
