# Following page 72 of Professional Plone Development by Martin Aspeli

from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_ContentWellPortlets():
    """
    The @onsetup decorator means this will not execute until the 
    Plone site testing layer has been set up
    """
    
    # Load the ZCML configuration
    fiveconfigure.debug_mode = True
    import Products.ContentWellPortlets
    zcml.load_config('configure.zcml', Products.ContentWellPortlets)
    fiveconfigure.debug_mode = False
    
    # Make the product available. 
    # Note: ztc.installPackage('Products.ContentWellPortlets') yielded "Installing Products.ContentWellPortlets ... NOT FOUND" 
    # Therefore did it this way instead
    from OFS.Application import install_package
    app = ztc.app()
    install_package(app, Products.ContentWellPortlets, Products.ContentWellPortlets.initialize)

# Call the (deferred) function
setup_ContentWellPortlets()
    
# Let Plone test case set up this product
ptc.setupPloneSite(products=['Products.ContentWellPortlets'])
    
class ContentWellPortletsTestCase(ptc.PloneTestCase):
    """Use this base class for all the tests in the package. Put common setup code in here"""
