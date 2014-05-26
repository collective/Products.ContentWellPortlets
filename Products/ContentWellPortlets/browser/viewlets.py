from zope.component import getMultiAdapter, ComponentLookupError
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from plone.portlets.interfaces import IPortletManager
from fractions import Fraction
from plone.app.portlets.browser.interfaces import\
    IManageContentTypePortletsView


class ContentWellPortletsViewlet(ViewletBase):
    name = ""
    manage_view = ""

    def update(self):
        context_state = getMultiAdapter(
            (self.context,
             self.request),
            name=u'plone_context_state')

        if IManageContentTypePortletsView.providedBy(self.view):
            key = self.request.form.get('key')
            self.manageUrl = '%s/%s?key=%s' % (
                context_state.view_url(), self.manage_type_view, key)
        else:
            self.manageUrl = '%s/%s' % (
                context_state.view_url(), self.manage_view)

        # This is the way it's done in plone.app.portlets.manager, so we'll do
        # the same
        mt = getToolByName(self.context, 'portal_membership')
        self.canManagePortlets = mt.checkPermission(
            'Portlets: Manage portlets',
            self.context)

    def showPortlets(self):
        return '@@manage-portlets' not in self.request.get('URL')

    def portletManagers(self):
        managers = []
        try:
            for n in range(1, 7):
                name = 'ContentWellPortlets.%s%s' % (self.name, n)
                mgr = getUtility(
                    IPortletManager,
                    name=name,
                    context=self.context)
                managers.append((mgr, name))
            return managers
        except ComponentLookupError:
            return []

    def portletManagersToShow(self):
        visibleManagers = []
        for mgr, name in self.portletManagers():
            if mgr(self.context, self.request, self).visible:
                visibleManagers.append(name)

        managers = []
        numManagers = len(visibleManagers)
        for counter, name in enumerate(visibleManagers):
            pos = 'position-%s' % str(
                Fraction(counter, numManagers)).replace('/', ':')
            width = 'width-%s' % (
                str(Fraction(1, numManagers)).replace('/', ':')
                if numManagers > 1 else 'full')
            managers.append(
                (name, 'cell %s %s %s' % (name.split('.')[-1], width, pos)))
        return managers


class PortletsInHeaderViewlet(ContentWellPortletsViewlet):
    name = 'InHeaderPortletManager'
    manage_view = '@@manage-portletsinheader'
    manage_type_view = '@@manage-typeportletsinheader'


class PortletsBelowTitleViewlet(ContentWellPortletsViewlet):
    name = 'BelowTitlePortletManager'
    manage_view = '@@manage-portletsbelowtitlecontent'
    manage_type_view = '@@manage-typeportletsbelowtitlecontent'


class PortletsAboveViewlet(ContentWellPortletsViewlet):
    name = 'AbovePortletManager'
    manage_view = '@@manage-portletsabovecontent'
    manage_type_view = '@@manage-typeportletsabovecontent'


class PortletsBelowViewlet(ContentWellPortletsViewlet):
    name = 'BelowPortletManager'
    manage_view = '@@manage-portletsbelowcontent'
    manage_type_view = '@@manage-typeportletsbelowcontent'


class FooterPortletsViewlet(ContentWellPortletsViewlet):
    name = 'FooterPortletManager'
    manage_view = '@@manage-portletsinheader'
    manage_type_view = '@@manage-typeportletsfooter'
