from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize
from pysv.policy.browser.interfaces import IBanner
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewlet

import random


class BannerViewlet(ViewletBase):
    """ Smart Teasers with scrollable. text and link
    """
    render = ViewPageTemplateFile('banner.pt')

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def random_banner(self):
        bp = self.context
        if self.context.portal_type not in ['Folder', ] \
           and not IPloneSiteRoot.providedBy(self.context):
            bp = aq_parent(self.context)

        path = '/'.join(bp.getPhysicalPath())
        banner = self.portal_catalog(
            portal_type='Teaser',
            path=dict(query=path),
            review_state='published',
        )
        self.scroll = len(banner) > 1
        banner = list(banner)
        random.shuffle(banner)
        return banner
