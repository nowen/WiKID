"""WiKIDAuthPlugin
Copyright(C), 2008, WiKID Systems, Inc - ALL RIGHTS RESERVED

This software is licensed under the Terms and Conditions contained within the
LICENSE.txt file that accompanied this software.  Any inquiries concerning the
scope or enforceability of the license should be addressed to:

WiKID Systems, Inc
1350 Spring St. Suite 300   
Atlanta, Georgia 30309 USA
p. +1 866-244-1876 
www.wikidsystems.com
info@wikidsystems.com
"""

from AccessControl.Permissions import add_user_folders
from Products.PluggableAuthService.PluggableAuthService import registerMultiPlugin
from WiKIDAuthPlugin import WiKIDAuthPlugin, manage_addWiKIDAuthPlugin, manage_addWiKIDAuthPluginForm

def initialize(context):
    """ Initialize the WiKIDAuthPlugin """
    try:
        registerMultiPlugin(WiKIDAuthPlugin.meta_type)

        context.registerClass( WiKIDAuthPlugin
                             , permission=add_user_folders
                             , constructors=( manage_addWiKIDAuthPluginForm
                                            , manage_addWiKIDAuthPlugin
                                            )
                             , icon='www/WiKID.png'
                             , visibility=None
                             )

    except ImportError:
        # If we don't have libgmail installed (and installed
        # correctly) then there is no point in exposing this plugin.
        pass

