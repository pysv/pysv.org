from zope.interface import implements
from zope.component import adapts

from Products.Archetypes import atapi

from Products.Archetypes.interfaces import IObjectPostValidation
from Products.Archetypes.utils import DisplayList
from Products.CMFCore.utils import getToolByName

from Products.validation import V_REQUIRED

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.ATContentTypes.content import image

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.permissions import ModifyPortalContent
from archetypes.referencebrowserwidget import ReferenceBrowserWidget

from plonede.content.interfaces import ITeaser
from plonede.content.config import PROJECTNAME

from plonede.content import PlonedeMessageFactory as _


ALLOWED_FONT_COLORS = DisplayList([('black', 'black'), 
                                   ('white', 'white'),
                                   ('blue', 'blue'),
                                   ('darkgrey', 'darkgrey'),
                                   ('lightgrey', 'lightgrey'),
                                   ])

schema = atapi.Schema((

    atapi.ReferenceField('teaserlink',
              required=False,
              searchable=False,
              languageIndependent=True,
              relationship = 'related',
              multiValued = False,
              write_permission = ModifyPortalContent,
              widget = ReferenceBrowserWidget(label = _(u'label_link', default=u"Link to some content"),
                            show_review_state = False,
                            show_indexes = False,
                            force_close_on_insert = True,
                            ),
        ),
    
    atapi.StringField('linktext',
              required=False,
              searchable=False,
              storage = atapi.AnnotationStorage(),
              widget = atapi.StringWidget(
                        description = '',
                        label = _(u'label_link_text', default=u'Text for this Link'),
                        ),
    ),

    atapi.StringField('fontcolor',
              required=False,
              searchable=False,
              storage = atapi.AnnotationStorage(),
              vocabulary = ALLOWED_FONT_COLORS, 
              widget = atapi.SelectionWidget(
                        desciption='',
                        label = _(u'label_font_color', default=u'Select color for header and description')
                        )
              ),
    ),

)

TeaserSchema = image.ATImageSchema.copy() + schema.copy()

TeaserSchema['title'].storage = atapi.AnnotationStorage()
TeaserSchema['description'].storage = atapi.AnnotationStorage()

finalizeATCTSchema(TeaserSchema, folderish=False, moveDiscussion=False)

class Teaser(image.ATImage):
    """Teaser
    """

    implements(ITeaser)

    portal_type = "Teaser"
    _at_rename_after_creation = True

    schema = TeaserSchema
    
    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    linktext =  atapi.ATFieldProperty('linktext')
    teaserlink =  atapi.ATFieldProperty('teaserlink')
    fontcolor = atapi.ATFieldProperty('fontcolor')
    
atapi.registerType(Teaser, PROJECTNAME)    