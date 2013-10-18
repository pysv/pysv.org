from Acquisition import aq_inner
from Acquisition import aq_parent

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.memoize.instance import memoize
from plone.app.layout.viewlets.common import ViewletBase

from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewlet

from pysv.policy.browser.interfaces import IBanner

import random

class BannerViewlet(ViewletBase):
    """ Smart Teasers with scrollable. text and link
    """
    render = ViewPageTemplateFile('banner.pt')

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def random_banner(self):
        if self.context.portal_type in ['Folder',] or IPloneSiteRoot.providedBy(self.context):
            bp = self.context
        else:
            bp = aq_parent(self.context)

        path = '/'.join(bp.getPhysicalPath())
        banner = self.portal_catalog(portal_type = 'Teaser',
                                           path = dict(query=path),
                                           review_state  = 'published',
                                           )
        self.scroll = len(banner) > 1

        banner = list(banner)
        random.shuffle(banner)
        return banner