from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from DateTime.DateTime import DateTime
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.memoize.instance import memoize
from plonede.content.interfaces import ITeaser


class FrontpageView(BrowserView):

    def _teasers(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        path = '/'.join(context.getPhysicalPath())
        results = catalog(
            portal_type='Teaser',
            review_state='published',
            sort_on='id',
            path=path
        )
        return results

    def _events(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(
            portal_type='Event',
            review_state='published',
            end={'query': DateTime(), 'range': 'min'},
            sort_on='start'
        )[:5]
        return results

    def teasers(self):
        result = self._teasers()
        teaser = []
        for t in result:
            obj = t.getObject()
            teaser.append(obj)

        return teaser

    def events(self):
        return self._events()
