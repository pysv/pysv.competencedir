# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from pysv.competencedir.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of pysv.competencedir into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pysv.competencedir is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('pysv.competencedir'))

    def test_uninstall(self):
        """Test if pysv.competencedir is cleanly uninstalled."""
        self.installer.uninstallProducts(['pysv.competencedir'])
        self.assertFalse(self.installer.isProductInstalled('pysv.competencedir'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IPysvCompetencedirLayer is registered."""
        from pysv.competencedir.interfaces import IPysvCompetencedirLayer
        from plone.browserlayer import utils
        self.failUnless(IPysvCompetencedirLayer in utils.registered_layers())
