# -*- coding: iso-8859-1 -*-
"""

pysv_policy test_setuphandlers

@copyright: 2013 ReimarBauer
@license:  GPL

"""

import unittest2 as unittest

from pysv.policy.testing import\
    PYSV_POLICY_INTEGRATION_TESTING

from plone.app.controlpanel.security import SecurityControlPanelAdapter

class TestSetuphandlers(unittest.TestCase):

    layer = PYSV_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']

    def test_setuphandlers(self):
        security = SecurityControlPanelAdapter(self.portal)
        self.assertTrue(security.enable_user_folders)
