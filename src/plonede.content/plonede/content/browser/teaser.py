from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from plone.memoize.instance import memoize
from plonede.content.interfaces import ITeaser


class TeaserView(BrowserView):
    __call__ = ViewPageTemplateFile('teaser.pt')
