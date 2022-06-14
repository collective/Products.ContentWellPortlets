Changelog
=========

4.3.1 (2022-06-14)
------------------

- Import fix for plone 5.2
  [gomez]

4.3.0 (2015-07-02)
------------------

- Add upgrade step to update cssregistry.
  [cah190]

- Clear the title from the stylesheet registration, as this prevents this makes
  this css resource an alternative stylesheet and prevents to be rendered in
  browsers.
  [thet]

- Add a z3c.autoinclude.plugin entry point.
  [thet]

- Change CSS rendering mode to "link" to allow merging with other link-rendered
  resources.
  [thet]

- Add a class to portlet managers, indicating how many portlets are in there.
  The form is ``num-portlets-NUMBER``. This can be used to build grid layouts,
  based on available css classes.
  [thet]

- Unify portlet manager templates to one template instead of five.
  [thet]

- Show links to portlet manager management views only in manage portlet view.
  So, you have to visit @@manage-portlets or @@manage-content-type-portlets to
  edit the ContentWellPortlets areas.
  [thet]

- Add contentwellportlets class to all portlet rows.
  [thet]

- Rename all porlet-well_manager classes to portlet-well_manager.
  [thet]

- Don't show ContentWellPortlets on views implementing IPloneControlPanelView.
  Please note, that not all control panels implement this interface.
  [thet]

- Add content type portlets management screens for each ContentWellPortlets
  area. These management screens are accessible from the
  @@manage-content-type-portlets view, which must be called with the content
  type as ``key`` request parameter. Open it from the @@types-controlpanel.
  [thet]

- Remove i18n folder. All translations are in locales folder already.
  [thet]

- Add uninstall profile.
  [thet]


4.2.0 (2013-01-18)
------------------

- Adding PortletsBelowContentTitle based on Maurizio Lupo's code along with
  upgrade step.
  [cah190]

- Replace migration code with ZCML upgrade step.
  [cah190]

- Merged Italian translation from Maurizio Lupo.  Thanks!
  [cah190]


4.1.0 (2011-11-30)
------------------

- Added another portlet manager below the global nav but above portal-columns
  [robzonenet]

- Added upgrade step and improved renderer to fail gracefully when the upgrade
  has not yet been run.
  [cah190]


4.0.1 (2011-11-22)
------------------

- Fixed container link for footer portlets.
  [robzonenet]


4.0 (2011-08-18)
----------------

* Portlet managers' css identifiers are now of the format
  'AbovePortletManager1' instead of the previously used
  'portletsAboveContentA'
  [esteele]

* Use Plone 4's deco.gs to handle layout automatically. Portlet managers will
  now display as 1/[number of portlet managers with visible portlets] wide.
  For example, if three of the six portlet managers have visible portlets,
  each will fill 1/3 of the available area. Themes based on
  plonetheme.sunburst will see the changes. Others will either need to use
  sunburst's columns.css or manually align content using each portlet
  manager's unique id.
  [esteele]

* Depend on 'Products.CMFPlone' instead of 'Plone'. See
  http://dev.plone.org/plone/ticket/10877 for more information.
  [esteele]

3.0 (2011-03-09)
----------------

* Release 3.0 Final
  [esteele]

3.0b2 (2011-02-28)
------------------

* Change the way the footer portlets viewlet is registered so that it plays a
  bit more nicely with themes.
  [esteele]

* Add a class="row" to the footer portlet template to prevent it from bleeding
  into the content area.
  [esteele]

3.0b1 (2011-01-27)
------------------

* Pin to Plone 4.0 or better. Those looking for 3.x compatibility are best
  sticking with ContentWellPortlets 2.0.
  [esteele]

* Added French translation
  [kiorky,numahell]

* Added Spanish translation
  [macagua]

* Added support for i18n
  [macagua]

2.1 (2010-06-21)
----------------

* Move "above" portlets to IAboveContent viewlet manager.
  [esteele]

* Tweak styling of "manage portlets" links, add managePortletsFallback class.
  [esteele]

2.0 (2009-10-12)
----------------

* Adds Footer portlets
* Adds extra portlet managers to each content well portlet area (6 per area:
  above content, below content, and footer) - 18 total
* Included extra example css in README.txt
* Cleaned up manager UI
* Adds warning message when on a default view of a container.

1.1 (2008-12-19)
----------------

* Added our own portlet manager renderer (closes ticket #952)
* Got rid of CSS associated with the previous (fudge) method of rendering we
  were using

1.0.1 (2008-12-17)
------------------

* Fixed an issue with an incomplete egg

1.0 (2008-12-16)
----------------

* Initial release

