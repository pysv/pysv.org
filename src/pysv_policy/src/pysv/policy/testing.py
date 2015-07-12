from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import applyProfile
from plone.testing import z2

from zope.configuration import xmlconfig


class PysvPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import pysv.policy
        xmlconfig.file('configure.zcml',
                       pysv.policy,
                       context=configurationContext)
        z2.installProduct(app, 'pysv.policy')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pysv.policy:default')

PYSV_POLICY_FIXTURE = PysvPolicy()
PYSV_POLICY_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PYSV_POLICY_FIXTURE, ),
                       name="PysvPolicy:Integration")
