Overview
============

* This product enables you to put portlets in places other than right and left columns, specifically:
  * above the main heading (h1) of the page
  * at the base of the page, above the footer
  In each area, you can add up to three columns of portlets. 

* You should use CSS (in the custom folder in portal_skins, or in your own theme product)  to configure how these portlets should appear relative to each other and to the content.

* This may allow you to create distinctive layouts for pages, folders etc without having to write new zope page templates

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

* The browserlayer.xml file enables this product to work with whatever theme product is installed
  It should not be replaced with a layer declaration in configure.zcml

          * For styling: 
             * Viewlets are contained within a div that has a CSS id
             * Each portlet manager within the viewlet is in a div with CSS class; these can be used for styling

          Below is some sample CSS that may work to generate different layouts (although it's up to you to test that is indeed the case in the browsers that matter to your users)
          Simply copy and paste the css for the type of layout you are looking for into your own theme product's stylesheet, or into portal_skins/ploneCustom.css in the ZMI. 
          If you experience issues with one of the portlet areas (usually the farthest right) dropping down below the other(s), try setting margin:0 and padding:0 on the .portletsAboveContentA, .portletAboveContentB, etc. classes. 

          All examples are written for Above Content portlets. For those below content and in the footer simply substitute the proper class identifier. So, .portletsAboveContentA would become .portletsBelowContentA, or .FooterPortletA.

  /* **** CSS for equal-width portlets. Keep in mind there are no margins or paddings set on these examples.  The examples below show for portlets above. portlets below and footer portlets are similar **** */
      	/* --- Six Column Above Layout ---- */
      	    .portletsAboveContentA, .portletsAboveContentB, .portletsAboveContentC,  .portletsAboveContentD,  .portletsAboveContentE,  .portletsAboveContentF {
          		float: left;
          		width: 16.6%;
      		}

      	/* --- Five Column Above Layout ---- */
      	    .portletsAboveContentA, .portletsAboveContentB, .portletsAboveContentC,  .portletsAboveContentD,  .portletsAboveContentE,  {
          		float: left;
          		width: 20%;
      		}

          /* --- Four Column Above Layout ---- */
      		.portletsAboveContentA, .portletsAboveContentB, .portletsAboveContentC,  .portletsAboveContentD   {
          		float: left;
          		width: 25%;
      		}

          /* --- Three Column Above Layout ---- */
      		.portletsAboveContentA, .portletsAboveContentB, .portletsAboveContentC   {
          		float: left;
          		width: 33%;
      		}

          /* --- Two Column Above Layout ---- */
      		.portletsAboveContentA, .portletsAboveContentB   {
          		float: left;
          		width:50%;
      		}


      /* **** Below shows three portlets, one portlet half the width of the page with 2 portlets on the right dividing up the remainder **** */
          	.portletsAboveContentA {
              	float: left;
              	width: 50%;
          	}

          	.portletsAboveContentB, .portletsAboveContentC {
              	float: left;
              	width: 25%;
          	}

      /* **** Below shows 3 portlets, one portlet 40% the width of the page with 2 portlets on the right slightly wider **** */
          	.portletsAboveContentA {
              	float: left;
              	width: 40%;
          	}

          	.portletsAboveContentB, .portletsAboveContentC {
              	float: right;
              	width: 60%;
          	}

      /* **** Below shows 4 portlets, one portlet 40% the width of the page with another portlet 60% and 2 more below that one that are 30% each wide.**** */
          	.portletsAboveContentA {
          	    float: left;
          	    width: 40%;
          	}
          	.portletsAboveContentB {
          	    float: right;
          	    width: 60%;
          	}
          	.portletsAboveContentC, .portletsAboveContentD {
          	    float: right;
          	    width: 30%;
          	}

      /* **** Below shows 4 portlets with varying widths, 2 on the left 15% wide and the third one is 40%, fourth one is 30%  **** */

          	.portletsAboveContentA, .portletsAboveContentB {
              	float: left;
              	width: 15%;
          	}

          	.portletsAboveContentC {
              	float: left;
              	width: 40%;
          	}
          		.portletsAboveContentD {
              	float: left;
              	width: 30%;
          	}
Bug reporting / feature suggestions
=============
Check https://weblion.psu.edu/trac/weblion/query?component=ContentWellPortlets
If you don't see your issue filed there already, go ahead and add a new ticket (component = ContentWellPortlets)
