from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from zope.component import getMultiAdapter
from urlparse import urlparse

class FrontpageView(BrowserView):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        p_state = getMultiAdapter((context, request), name=u'plone_portal_state')
        portal_url = p_state.portal_url()
        path = p_state.navigation_root_path()
        
        domain = urlparse(portal_url).hostname.split('.')[-1]
        
        domainsdict = {'de':'de','at':'at','ch':'ch'}
        target_id = domainsdict.get(domain, 'default')

        target_brains = portal_catalog(id=target_id, path=dict(query=path), depth=0)

        if len(target_brains) == 1:
            request.response.redirect(target_brains[0].getURL())
            
        else:
            messages = IStatusMessage(self.request)
            messages.addStatusMessage(u"Diese Darstellung leitet je nach aufgerufener Domain auf ein \
                    Element (am sinnvollsten wohl ein Ordner) mit den id's 'de', 'at' oder 'ch' weiter. \
                    Als Fallback auf einen content mit der id 'default'. Wenn es auch das nicht gibt eben \
                    auf die folder_contents", type="info")
            request.response.redirect(portal_url+"/folder_contents")

    