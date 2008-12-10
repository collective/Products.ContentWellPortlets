# Following page 73 of Professional Plone Development by Martin Aspeli
# Requires that the base.py file exists

import unittest
from Products.ContentWellPortlets.tests.base import ContentWellPortletsTestCase

class TestSetup(ContentWellPortletsTestCase):
    '''
    Check whether product is installed correctly
    '''
    
    def afterSetUp(self):
        pass

    def testCSSregistered(self):
        '''
        Is our stylesheet registered?
        TODO: remove this test once the workaround requiring the stylesheet is fixed
        '''
        self.failUnless('++resource++ContentWellPortlets.styles/ContentWellPortlets.css' in self.portal.portal_css.getResourceIds(), 'Cannot find CSS')
        
    def testInterfaceAvailable(self):
        '''
        Is our product-specific interface available?
        '''
        from plone.browserlayer import utils
        from Products.ContentWellPortlets.browser.interfaces import IContentWellPortlets
        self.failUnless(IContentWellPortlets in utils.registered_layers(), 'Cannot find IContentWellPortlets interface')
    
    def testPortletManagersAbove(self):
        '''
        Are our portlet managers available? Test by inserting a calendar portlet
        '''
        from zope.component import getUtility, getMultiAdapter
        from plone.app.portlets.portlets import calendar
        from plone.portlets.interfaces import IPortletManager
        from plone.portlets.interfaces import IPortletRenderer

        # get the portlet manager we should have created
        manager = getUtility(IPortletManager, name='ContentWellPortlets.AbovePortletManager1',context=self.portal)
        
        # try rendering a portlet with it using getMultiAdapter((context, request, view, manager, assignment), Interface)
        renderer = getMultiAdapter((self.folder, self.folder.REQUEST, self.folder.restrictedTraverse('@@plone'), manager, calendar.Assignment()), IPortletRenderer)
        self.failUnless(isinstance(renderer, calendar.Renderer), 'Cannot render portlet above contents')
        import pdb; pdb.set_trace()
        
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
