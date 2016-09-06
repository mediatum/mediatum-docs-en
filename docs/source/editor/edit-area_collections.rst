Collections (available only for administrator accounts)
-------------------------------------------------------

1. Creating a collection

In general, the collection itself is created by the administrator. If
you have permission you can edit at collection level. A description of
editing functions on collection levels follows.

#. Select top level of your media server (e.g.
   "mediaTUM-Gesamtbestand").
#. Create new collection by means of the *General administrative
   functions* panel.



.. figure:: images/create_coll.jpg
   :width: 600 px

   Create collection


2. Editing name and default display format of a collection

#. Select from menu *Edit metadata* and then again *Edit metadata*
#. Now you can edit the collection's name.
#. Select default display of short view. You can choose between three
   options for the short view style:

   -  thumbnail (preview and short display text; several objects next to
      each other)
   -  list (preview and short display; one object per line)
   -  text (no preview, just text; one object per line)

#. Select default display of full view. You can choose between two
   options for the full view style:

   -  full standard (displays text description and thumbnail of the
      object)
   -  full text (displays only text description of the object, no
      thumbnail)

#. You can decide wheather a collection or directory is displayed
   straight after it was created or only when it holds objects.

.. figure:: images/edit-collectionsettings.jpg
   :width: 635 px

   Edit collection settings

These settings can be made only at collection
level. That means a setting on directory level will be overwritten by
the setting that is made at collection level above. **Remark:** Every
user can change the default setting in the normal Website view by
choosing the preferred way of display for the session via the buttons on
the right hand side.

#. Text display
#. Thumbnail display
#. List display

.. figure:: images/display-setting.jpg
   :width: 865 px

   Change display settings

This setting is sometimes remembered by the system
when coming back. That means that the content is not displayed like the
default setting but like your local preference.

3. Add logo to collection

#. Select from menu *Edit metadata* and *Edit logo*.
#. Upload a logo: Search your computer for the logo by clicking
   *Durchsuchen* and pick the specific logo image. Then click on the
   *Create/Upload* button.
#. The logo will be displayed on the top.
#. If available or needed, enter the URL in the field *Link behind logo*
   and click on the *Save Changes* button. You can delete the URL by
   clicking the *Reset* button.
#. You can test the URL by clicking the |image3| symbol (the linked site
   opens in a new tab of your browser).

.. figure:: images/edit-logo.jpg
   :width: 552 px

   Edit logo


4. Set a default sorting for a collection

**Functional description:** It is possible to define a default sorting
of the displayed data sets in your collection. You can pick a field that
becomes your sorting criteria, e.g. year or author. Therefore certain
fields of your metadata scheme have to be defined as sort fields first.
This can only be done by an Administrator in the actual metadata scheme
(Administration area).

#. Click on your collection in the left browsing menu for which you want
   to create the default sorting.
#. Select *Edit metadata* and *Sort files* from the top menu. By default
   the automatic sorting is turned off.
#. Click on the arrow pointing down to get the list of available sort
   fields (if the one you want to choose is not listed - it has not yet
   been defined as a sort field in the metadata scheme). Choose the
   field you want to be the default sorting criteria of your collection
   (e.g. Year, Author, ...).
#. Click OK to save settings.

5. Create search masks: define search fields for advanced search

**Functional description:** By default the normal search interface
provides one field that runs a search over all metadata fields and the
information given there. If you want to offer an advanced search you can
also add certain fields for searching, e.g. for author or year by
defining a search mask. This function also gives you the opportunity to
create fields that search through more than one field, e.g. you could
combine author and editor to a field called 'Person'. But this will only
work if the data types of the fields are suitable for this (see
description later for more information). There are two ways to create
search masks:

-  Define new search mask.
-  Create search mask from parent.

**Define new Search mask** The fields you want to provide for an
advanced search have to be defined as search fields in the metadata
scheme. This has to be done in the *Administration area* before you can
start defining certain search fields or putting fields together.

#. Choose the collection, you want to create the search mask for, by
   clicking on it.
#. Select *Edit metadata* and *Search mask* from the top menu.
#. If no search mask is defined yet, the search mask from the parent
   node will be inherited.
#. If no search masks are displayed or there is none that could have
   been inherited, choose *define new* from menu.
#. A list of fields from the first metadata scheme you are using in your
   collection comes up. These fields are all defined search fields from
   this scheme. They are automatically loaded to become fields for the
   new advanced search and are available immediately. To remove one or
   more fields from the search mask, click on the plus sign in front of
   the field and delete it from the search mask by clicking on the red x
   symbol. This will delete the field only from the search mask; it
   still exists in the metadata scheme and all masks where it was
   defined. You can also rename the field. In the brackets behind the
   field name, the name of the metadata scheme and the chosen field name
   are displayed.

**Result:** The *Advanced search* for the collection is automatically
available next to the standard search in the web view. 

.. figure:: images/advanced-search.jpg
   :width: 302 px

   Advanced search

Click on *Advanced Search* and
as default three search fields come up. (If needded you can have more
fields displayed by clicking on *More Searchfields*. 

.. figure:: images/searchfields.jpg
   :width: 291 px

   Search fields

The fields all hold a list of the
defined search fields. You can choose a field (e.g. author) and combine
it with another one (e.g. year) to get more specific search results.


.. figure:: images/searchfields2.jpg
   :width: 291 px

   Search fields

**Add fields from
other metadata schemes** **Functional description:** If you have more
than one metadata scheme in use, the fields you want to offer may be
part of another metadata scheme and not the one that was loaded first in
your search mask.

#. Go to search mask definition via *Edit metadata* and *Search mask*.
#. Choose *append new* at bottom of list.
#. Click on the plus in front of the new search field. Now you can edit
   the name of the search field. This term will be displayed in the
   advanced search for this field.
#. Click on the arrow on the first empty field and choose a metadata
   scheme that holds the first specific field you want to add.
#. Now you can choose the specific field from the list offered in the
   next field.
#. Click on *add* to define the field in the list. You can add as many
   fields from all the metadata schemes that you are using as you wish.

**Result:** The added search mask field will appear in the advanced
search. 

.. figure:: images/advanced-search2.jpg
   :width: 293 px

   Advanced search

**Combine
fields from different schemes to one search field** **Example:** Combine
fields abstract and title to one search field.

#. Add first a field as described above.
#. To add more fields from the same or another metadata scheme, just
   repeat the described procedure by adding another field to the search
   field.

The defined fields will be listed as shown: 

.. figure:: images/combined-searchfield.jpg
   :width: 468 px

   Combine search fields

**Remark:** Be
careful with combination of fields. Two index fields with the same name
from different schemes can not be combined as well as you should not
combine different field types (e.g. text field and index field). This
function is best used for combination of two text fields. To delete a
field from a search mask field just click on the red x sign next to the
field. You can also delete the whole search mask field by clicking on
the red x sign next to its name. **Create Search mask from parent**
**Functional description:** If a collection holds collections on sub
levels as well, the search mask from the upper level collection can be
automatically transferred to the collection on the next level using
inheritance. It is assumed that the collection on upper level holds a
search mask definition.

-  Select collection on lower level.
-  Select *Edit metadata* and *Search mask* from the top menu.
-  By default, the search mask is set on *none*.
-  Just choose *from parent* in pull down menu and the the search mask
   from the upper (parent) collection will be adapted for the selected
   collection.

The inherited search mask will not be displayed on the lower level; it
is only shown and can be edited on the collection level where it was
originally defined.


.. |image3|  image:: images/Extlink.png
