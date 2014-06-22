import logging

# ZODB imports
from ZODB.POSException import ConflictError

# Zope imports
from AccessControl import getSecurityManager

# CMFCore imports
from Products.CMFCore import permissions
from plone import api

# Logger output for this module
logger = logging.getLogger(__name__)

INITIAL_LOGIN_LANDING_PAGE = "/mitmachen/willkommen-neu-registriert"


def redirect_to_first_login_landing_page(user):
    # Get access to the site within we are currently processing
    # the HTTP request
    portal = api.portal.get()

    # We need to access the HTTP requesrt object via
    # acquisition as it is not exposed by the event
    request = getattr(portal, "REQUEST", None)
    if not request:
        # HTTP request is not present e.g.
        # when doing unit testing / calling scripts from command line
        return

    # Look for portal relative paths where the items are
    try:
        target = portal.unrestrictedTraverse(INITIAL_LOGIN_LANDING_PAGE)
    except ConflictError:
        # Transaction retries must be
        # always handled specially in exception handlers
        raise
    except Exception, e:
        # Let the login proceed even if the folder has been deleted
        # don't make it impossible to login to the site
        logger.exception(e)
        return False

    # Check if the current user has Editor access
    # in the any items of the folder
    sm = getSecurityManager()

    for obj in target.listFolderContents():
        if sm.checkPermission(permissions.ModifyPortalContent, obj):
            logger.info("Redirecting user %s to %s" % (user, obj))
            request.response.redirect(obj.absolute_url() + "/edit")
            return True

    logger.warn("Redirecting user {0} to inital loginpage failed".format(user))

    # Let the normal login proceed to the page "You are now logged in" etc.
    return False
