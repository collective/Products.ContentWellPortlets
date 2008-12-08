Introduction
============

Adds two new portlet zones: one above the main heading (h1) of the page, and the other at the  base of the page, above the footer

TODO:
The ContentWellPortlets.css and cssregistry.xml files should disappear from later versions of this product 
The CSS is only here as a temporary fudge to hide the "manage portlets" link that leads to the @@manage-portlets view.
That link is called in by a python script: plone.app.portlets.manager.ColumnPortletManagerRenderer
We are parasitizing this script for the time being, so we get the template that it calls 
(which renders the link along with all its other goodness) 
