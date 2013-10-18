from zope.i18nmessageid import MessageFactory
from plonede.content import config

from Products.Archetypes import atapi
from Products.CMFCore import utils

PlonedeMessageFactory = MessageFactory('plonede.content')

def initialize(context):
    """ initalizer called wenn used as a Zope 2 product, referenced from
    configure.zcml, ct registration
    """
    
    from content import teaser
    
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit("%s: %s" % (config.PROJECTNAME, atype.portal_type),
            content_types      = (atype,),
            permission         = config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)