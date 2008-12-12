Overview
============

* This product enables you to put portlets in places other than right and left columns, specifically:
  * above the main heading (h1) of the page
  * at the base of the page, above the footer
  In each area, you can add up to three columns of portlets. 

* You should use CSS (in the custom folder in portal_skins, or in your own theme product)  to configure how these portlets should appear relative to each other and to the content.

To install the product
======================
* See docs/INSTALL.TXT for instructions


To add portlets above the content
=================================
1. Log into your Plone site as a Manager (or someone else with the "Portlets: Manage portlets" permission)
2. Go to the place in your site where you want portlets. For example:
   * If you want portlets on your home page only, go to http://yourSiteURL/front-page
   * If you want portlets on your entire site, go to http://yourSiteURL
3. Bring up a management page by either
   (a) Clicking the "add, edit or remove portlets link"**; or
   (b) Adding /@@manage-portletsabovecontent to the end of the URL and hitting "return"
 4. You should see a management page entitled "Manage Portlets Above Content"
   This gives you the option to add portlets in one or more of three columns: A, B and C
   You can add as many portlets in each column as you like
   Other commands (reordering, hiding, blocking portlets) are the same as for the right and left columns

** Note: if you are in a folder that has a default page, this will take you to a screen where you can add portlets to that page.
If you want to add portlets to all the pages in the folder, make sure you are on the folder rather than the default page (e.g. by clicking the "contents" tab) before clicking the link

To add portlets below the content
=================================
Follow the above instructions, but instead of clicking the "add, edit or remove portlets above content" link or adding /@@manage-portletsabovecontent to the URL:
 (a) Click the "add, edit or remove portlets below the content" link; or
 (b) Add /@@manage-portletsbelowcontent to the end of the URL


Technical details
===================

* The product adds two new viewlets; within each of these are three portlet managers (specified in portlets.xml)
  For details of exactly which viewlet managers these viewlets slot into:
   * see configure.zcml in Products/ContentWellPortlets/browser
   * or install the product, go to your Plone site and add /@@manage-viewlets to the URL

* The browserlayer.xml file adds crucial functionality; it cannot be replaced with a layer declaration in configure.zcml

* For styling: 
   * Viewlets are contained within a div that has a CSS id
   * Each portlet manager within the viewlet is in a div with CSS class; these can be used for styling

Below is some sample CSS that may work to generate different layouts (although it's up to you to test that is indeed the case in the browsers that matter to your users)
Simply copy and paste the css for the type of layout you are looking for into your theme product's stylesheet, or into portal_skins/ploneCustom.css in the ZMI. 
If you experience issues with one of the portlet areas (usually the farthest right) dropping down below the other(s), try setting margin:0 and padding:0 on the .portletsAboveContentA, .portletAboveContentB, etc. classes.

    /* ----  Three Column Above Layout  ---*/
    .portletsAboveContentA, .portletsAboveContentB, .portletsAboveContentC { float:left; }
    .portletsAboveContentA, .portletsAboveContentC { width:33%; }
    .portletsAboveContentB { width:34%; }
    .portletsAboveContentA .portletWrapper, .portletsAboveContentB .portletWrapper, .portletsAboveContentC .portletWrapper { padding-right:1em; }

    /* ----  Two Column Above Layout (assumes usage of content wells A & B) ---*/
    .portletsAboveContentA, .portletsAboveContentB { float:left; width:50%; }
    .portletsAboveContentA .portletWrapper, .portletsAboveContentB .portletWrapper { padding-right:1em; }


    /* ----  Two Column Below Layout (assumes usage of content wells A & B) ---*/
    .portletsBelowContentA, .portletsBelowContentB, { float:left; width:50%; }
    .portletsBelowContentA .portletWrapper, .portletsBelowContentB .portletWrapper, { padding-right:1em; }
 

    /* ----  Three Column Below Layout ----- */
    .portletsBelowContentA, .portletsBelowContentB, .portletsBelowContentC { float:left; }
    .portletsBelowContentA, .portletsBelowContentC { width:33%; }
    .portletsBelowContentB { width:34%; }
    .portletsBelowContentA .portletWrapper, .portletsBelowContentB .portletWrapper, .portletsBelowContentC .portletWrapper { padding-right:1em; }
  

Bug reporting
=============
Check https://weblion.psu.edu/trac/weblion/query?milestone=ContentWellPortlets+2.0
If you don't see your issue filed there already, go ahead and add a new ticket (component = ContentWellPortlets)
