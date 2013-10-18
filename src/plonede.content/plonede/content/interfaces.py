from zope.interface import Interface
from zope import schema

from zope.container.constraints import contains

from plonede.content import PlonedeMessageFactory as _

class ITeaser(Interface):
    """Teaser
    """
    
    title = schema.TextLine(title=_(u"Title"),
                            required=True)
    
    description = schema.Text(title=_(u"Description"),
                              description=_(u"Short Description of the Body Text."))
    