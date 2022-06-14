from .interfaces import IContentWellPortletManager
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.manager import ColumnPortletManagerRenderer
from zope.component import adapts
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserView
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ContentWellPortletRenderer(ColumnPortletManagerRenderer):
    """A renderer for the content-well portlets"""

    adapts(Interface, IDefaultBrowserLayer, IBrowserView, IContentWellPortletManager)
    template = ViewPageTemplateFile("templates/renderer.pt")
