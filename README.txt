Introduction
============

Overview
* Creates two new areas where portlets can be added to your Plone site:
  * above the main heading (h1) of the page
  * at the base of the page, above the footer
  In each area, you can add up to three columns of portlets. 

* You should use CSS (in the custom folder in portal_skins, or in your own theme product) 
  to configure how these portlets should appear relative to each other and to the content.

Technical details
* This product adds two new viewlets; within each of these we call a template that calls a series of portlet managers
  (the portlet managers are specified in portlets.xml)
  See browser/configure.zcml for details of exactly which viewlet managers these viewlets slot into

* For styling: each area has a CSS id, and each column within it has a CSS class; these can be used for styling
  For example, if you want just two columns of portlets above the content, you could style with something like:
  #portlets-above .portletsAboveContentA, #portlets-above .portletsAboveContentB { width:48%; padding-right:2em; float:left }

* The browserlayer.xml file adds crucial functionality; it cannot be replaced with a layer declaration in configure.zcml
  

TODO:
The ContentWellPortlets.css and cssregistry.xml files should disappear from later versions of this product 
The CSS is only here as a temporary fudge to hide the "manage portlets" link that leads to the @@manage-portlets view.
That link is called in by a python script: plone.app.portlets.manager.ColumnPortletManagerRenderer
We are parasitizing this script for the time being, so we get the template that it calls 
(which renders the link along with all its other goodness) 
