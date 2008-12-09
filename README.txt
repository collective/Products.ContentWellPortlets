Overview
============

* This product enables you to put portlets in places other than right and left columns, specifically:
  * above the main heading (h1) of the page
  * at the base of the page, above the footer
  In each area, you can add up to three columns of portlets. 

* You should use CSS (in the custom folder in portal_skins, or in your own theme product) 
  to configure how these portlets should appear relative to each other and to the content.

To install the product
======================
* See docs/INSTALL.TXT for instructions


To add portlets above the content
=================================
1. Log into your Plone site as a Manager
2. Go to the place in your site where you want portlets. For example:
   * If you want portlets on your home page only, go to http://yourSiteURL/front-page
   * If you want portlets on your entire site, go to http://yourSiteURL
3. Add /@@manage-portletsabovecontent to the end of the URL and hit "return" to bring up a management page
   * On your home page, this would give a URL of http://yourURL/front-page/@@manage-portletsabovecontent
4. You should see a management page entitled "Manage Portlets Above Content"
   This gives you the option to add portlets in one or more of three columns: A, B and C
   You can add as many portlets in each column as you like
   Other commands (reordering, hiding, blocking portlets) are the same as for the right and left columns


To add portlets below the content
=================================
Follow the above instructions, but add /@@manage-portletsbelowcontent to the end of the URL instead of
/@@manage-portletsabovecontent


Technical details
===================

* The product adds two new viewlets; within each of these we call a template 
  that calls portlet managers (specified in portlets.xml)
  For details of exactly which viewlet managers these viewlets slot into:
   * see configure.zcml in Products/ContentWellPortlets/browser
   * or install the product, go to your Plone site and add /@@manage-viewlets to the URL

* For styling: 
   * viewlets are contained within a div that has a CSS id
   * each portlet manager within the viewlet is in a div with CSS class; these can be used for styling
  For example, if you want just two columns of portlets above the content, you could style with something like:
  #portlets-above .portletsAboveContentA, #portlets-above .portletsAboveContentB { width:48%; padding-right:2em; float:left }

* The browserlayer.xml file adds crucial functionality; it cannot be replaced with a layer declaration in configure.zcml
  

TODO:
The ContentWellPortlets.css and cssregistry.xml files should disappear from later versions of this product 
The CSS is only here as a temporary fudge to hide the "manage portlets" link that leads to the @@manage-portlets view.
That link is called in by a python script: plone.app.portlets.manager.ColumnPortletManagerRenderer
We are parasitizing this script for the time being, so we get the template that it calls 
(which renders the link along with all its other goodness) 
