from zope.interface import Interface
from plone.portlets.interfaces import IPortletManager
from plone.app.portlets.interfaces import IColumn

class IContentWellPortlets(Interface):
    """
    A layer specific to this product. Is registered using browserlayer.xml
    """
    
class IPortletsAboveContent(IPortletManager, IColumn):
	 """
	 For the portlet manager above the content area.
	 The IColumn bit means that we can add all the portlets available to 
	 the right-hand and left-hand column portlet managers
	 """

class IPortletsBelowContent(IPortletManager, IColumn):
	 """
	 For the portlet manager below the content area.
	 The IColumn bit means that we can add all the portlets available to 
	 the right-hand and left-hand column portlet managers
	 """

