Objects
-------

By default, object related authorizations (regarding see, edit and
download options) are the same as those which are assigned to the
"parent" directory (that is the directory which contains the object),
for example, if you are allowed to edit a certain directory, you
normally are also able to edit the objects therein; if you can display a
certain directory, you normally can also see the objects therein.
.. rubric:: 1. Upload of new objects

New objects will be uploaded directly into the subfolder *Uploads* of
your user directory. A direct upload into other folders is not
supported. If you select the folder *Upload* in your user directory all
content of the subfolder *Uploads* will be displayed and you can
initiate a file upload. Supported object types and formats are:

-  image files - gif, tif, jpg, png, bmp
-  document files - pdf
-  video files - flv

You can upload exactly one file per upload. **Remark:** If you want to
upload more than one object file, you may create a zip archive (e.g.
using WinZip) and upload the zip archive; after completion of the upload
process the zip-archive will automatically be unpacked and you can
individually edit the objects. The larger the size of your zip archive
the longer the upload process will take. To upload a file select
*Files*, then *Upload* in the *General administrative functions* panel,
or select the folder *Uploads* in your user directory in the *Folder
administration*.
.. rubric:: 2. Creating metadata sets without attached digital objects.
   Creating bibliographic data sets

This feature enables you to create purely bibliographic data sets in
mediaTUM. If needed, digital objects to these bibliographic data sets
can be attached later. In order to create metadata sets manually proceed
as by upload of objects with one exception: Click the *Upload* button
without previously having selected a file for upload. It is also
possible to create metadata sets by uploading BibTeX files
(filename.bib) **How to do it:**

-  Select *Import bibtex* from files menu of the *General administrative
   functions* panel. If not yet existing, the directory *Imports* is
   automatically created.
-  Click on *Durchsuchen* and choose the BibTeX file you want to upload
   from your (local) system or network (e.g. example.bib).
-  Click on *Create/Upload* button to load file up.

[caption id="attachment\_927" align="alignnone" width="963"
caption="Import bibtex data"]\ |Import bibtex data|\ [/caption]
**Result:** Content of file is automatically turned into a metadata set
without object (bibliographic data set). [caption id="attachment\_930"
align="alignnone" width="795" caption="Bibliographic data
set"]\ |Bibliographic data set|\ [/caption] **Remark:** The bibtex
import function is not a general setting and does not necessarily be
available for your metadata schema. There are different data
types/formats for BibTeX that have to be defined in the metadata schema
that is used. If there are no BibTeX data types defined for the metadata
scheme you are using an error message coming is up. So far, the
following BibTeX formats can be processed by a specific metadata scheme:
book; incollection; mastersthesis; proceedings; inproceedings; diss;
techreport; article; misc If you have questions about this feature,
please contact the administrator.
.. rubric:: 3. Special editing function: specific video thumbnail

By default the automatically created thumbnail shows the first second on
a video. This image might not always be the best promotion for your
video, there might be another scene that would be better for the
thumbnail. You can create a thumbnail of a certain second of the video,
the procedure is described in this section.

#. Upload a video of your choice. The standard thumbnail will be created
   (1st second of video)
#. Watch the video and decide which second you want to make the
   thumbnail.
#. Change into *editing the video object* by clicking on the
   metadescription area right of the thumbnail. Click on *Edit metadata*
   and then on *Administration*.
#. Scroll down to the section *Create new attribute* and insert the
   value *system.thumbframe* in the field *Attribute name*.
#. Insert the second of the video scene you want to have as thumbnail,
   e.g. 15 for second 15.
#. Click on save button
#. Click on *Edit metadata* and then on *Change/add digital object*
#. Scroll down to the bottom of the site to the *Reprocess digital
   object* button. Click on the button and the new thumbnail will be
   created and set for the object.

.. rubric:: 4. Metadata (descriptive metadata)

Descriptive Metadata are data which describe the content of digital
objects. They are useful for resource discovery. Mandatory metadata
fields are tagged by an orange star \* . **Metadata field types:**

-  Fields with unrestricted data entry, text fields, memo fields.

   -  *Data entry / editing*: via keyboard, no restrictions.
   -  *Examples*: Title, abstract, description, non-structured data.

   [caption id="attachment\_936" align="alignnone" width="640"
   caption="Example"]\ |Example|\ [/caption]
-  Index fields

   -  *Data entry / editing*: via keyboard, no restrictions. If needed
      you can utilize field / attribute values already in use in your
      collection (and describe other related objects) by selecting them
      from the field index.
   -  *Examples*: Authors, keywords, descriptors.

   An index field can be identified by the button *Index* behind the
   text field. Entered attributes are saved in a specific index list.
   You can recall the saved values for later for different data sets,
   clicking on that button. [caption id="attachment\_938"
   align="alignnone" width="646"
   caption="Example"]\ |Example|\ [/caption] To see the index entries
   click button *Index*. New window with index entries will be opened.
   Select entry via mouse click to select one entry. Hold Ctrl-key and
   select entries one by one to select more than one entry. [caption
   id="attachment\_941" align="alignnone" width="408" caption="Index
   entries"]\ |Index entries|\ [/caption] To change existing data enter
   new values, select other entries from field index and separate
   different values by semicolon. **Advantages of index fields:**

   -  Field index can be made available in standard web interface to
      support searching and retrieval process.
   -  Quality control of field values: data entry errors can be detected
      easier than in preceeding type fields.
   -  Support of data entry processes by utilizing attribute value
      transfer from index (thus error prevention and improving
      consistency of field values).

-  Drop down lists

   -  *Data entry / editing*: selecting one field value from drop down
      list. List of available values cannot be changed in editor
      interface (list is managed by Administrator).
   -  *Examples*: Fields with a limited number of attribute values.

   [caption id="attachment\_945" align="alignnone" width="609"
   caption="Example"]\ |Example|\ [/caption] **Remark:** The first enty
   of a drop down list will always be set for an object. This can be a
   comfortable way of automatically set values. You can always change to
   another value if required. If that is not needed and you want to keep
   the possibility of not setting any value, an *empty* value can be
   added to the list (see *TUM Standort* field in examples below). The
   empty value can be used for objects that do not hold a value for the
   specific field. [caption id="attachment\_947" align="alignnone"
   width="608" caption="List without empty value"]\ |List without empty
   value|\ [/caption] or [caption id="attachment\_949" align="alignnone"
   width="610" caption="List with an empty value"]\ |List with an empty
   value|\ [/caption]
-  Lists of field values with multiple selection

   -  *Data entry / editing*: selecting one or more entries from list of
      field values; list of available values cannot be changed in editor
      interface. Select entry via mouse click to select one entry. Hold
      Ctrl key and select entries one by one to select more than one
      entry.
   -  *Examples*: fields with a limited number of attribute values.

   [caption id="attachment\_953" align="alignnone" width="606"
   caption="Example"]\ |Example|\ [/caption] If necessary the entries in
   the list of field values can be structured hierarchically (see
   example above). Certain entries can be excluded from the selection
   process; these entries will be displayed in boldface (see "Sciences"
   and "Engineering" in example above). If necessary *empty* entries can
   be generated. Use a semicolon for separation of different field
   values. Use the following schema for editing of personal names: [Last
   name], [First name].

.. rubric:: 5. Publishing objects by using the *Quick publisher* option.

If a directory contains unpublished objects, a message is displayed on
red background. The link in the message enables you to place the marked
objects in a certain directory of your collection as well.

#. Click on the link "Publish these objects"
#. Mark relevant objects
#. Check if an *Actual Destination Directory* is chosen and if it is the
   right one (example has not yet a chosen directory!).
#. Click on the button *Choose publish directory* to define a directory
   or to change it.
#. Choose publish directory in browsing structure by checking the circle
   behind. The directory will be marked.
#. Click on *OK* button. Actual destination directory will be shown.
#. By clicking the *Publish* button the object will be moved to the
   chosen destination directory.

.. rubric:: 6. Technical metadata: Change or add digital object(s).

**Functional description:**

-  Display of digital object and all related files like generated
   thumbnails, full text extraction, etc.
-  Exchange digital objects while keeping existing descriptive metadata.
-  Add additional object to the attachement browser. This is a special
   feature that should be used carefully.

Click on *Change/add digital object* in the *Edit metadata* menu. A list
of all related files and their size will be displayed: [caption
id="attachment\_965" align="alignnone" width="650" caption="Change/add
digital object"]\ |Change/add digital object|\ [/caption] **Exchanging
digital objects while keeping existing descriptive metadata**
**Functional description:** It happens that you upload and edit an
object that later turns out to be not the object you thought it was
(e.g. there are different versions and you did not have the right one or
had another one). In some cases, you might have even sent the link to
the object to other people. This feature gives you the chance to upload
another object to the data set and keep the internal id and metadata (of
course you can edit the metadata as well if necessary). After the
upload, the new file has to be reprocessed to create the correct related
files like thumbnails or full text extractions.

#. Choose setting for *Exchange of digital object*.
#. Click on button *Durchsuchen* and look for file on your system, mark
   it and then click *Open*
#. Click on *Create/Upload* button.
#. Click on *Re-process digital object* button at the end of the page.

**Add digital object** **Functional description:** mediaTUM does not
necessarily require a digital file to create a digital object/data set.
You can also create a bibliographic record which can be handy for items
that you want to list (e.g. copyright protected fulltexts are not
available or allowed to present) or to create a two step workflow: first
create the metadata sets and then add the digital files to these data
sets. With this function you can add the file later to an existing
metadata sets.

#. Choose setting *Add digital object*
#. Click on button *Durchsuchen* and look for file on your system, mark
   it and then click *Open*
#. Click on *Create/Upload* button.
#. Click on *Re-process digital object* button at the end of the page.

**Add new thumbnail** **Functional description:** To represent the data
set of an object the required thumbnails are generated automatically. By
default the following principles are used to choose what will be
displayed on the thumbnails:

-  for a document (pdf): first page of pdf file
-  for an image (e.g. jpg, tif): whole display of the uploaded image
-  for a video(flv): first second of video

**Note on PDF files:** Due to file restrictions it can happen in some
rare cases that you upload a file but the thumbnail could not be
generated (postprocessing error). In this case you can use this function
to create a screenshot of the first page and add it as thumbnail. You
just need an image file, the size will be automatically adjusted during
the process. **Note on videos:** If you don't want the generated
thumbnail of a video (maybe the first second was a black take) you can
also use this function to change the thumbnial to a preferred image.
Another solution is to define a certain second/scene for your video
thumbnail, for a descripion how to do this see above. **How to do it:**

#. Create an image of the item/scene you want to be displayed as
   thumbnial (e.g. screenshot).
#. Go to the section *Add new thumbnail* on the *Change/add digital
   object* page.
#. Click on button *Durchsuchen* and look for the image file on your
   system, mark it and click *Open*.
#. Click on *Create/upload*.

[caption id="attachment\_975" align="alignnone" width="549" caption="Add
new thumbnail"]\ |Add new thumbnail|\ [/caption] The thumbnail will be
automatically added to the object, you do not have to reprocess the
digital object. **Add additional files to the attachement browser**
**Functional description:** The attachement browser is a special feature
that can be used for objects that consist of more than one digital file
but hold only one set of metadata description. Exapmle: an architectural
diploma theses has only one metadata description data set but consists
of various plans, drafts, images. You need a data set of any kind
(document, image, video) to attach one or more files to it. You have two
options to use the attachement browser:

-  Attach more than one additional object to the data set. This will
   create an additional directory where all the attachments are stored.
-  Attach only one additional object to the data set. This option can be
   used if you have exactly one file to attach and you don't need it's
   own directory for that.

To attach more than one additional object:

#. Choose the option *add attachment directory*.
#. Enter a name for the attachement directory in the field *Directory*.
#. Click on *Durchsuchen* and choose the first file on your system that
   you want to attach.
#. Click on *Create/upload* to attach the files.

[caption id="attachment\_979" align="alignnone" width="473"
caption="Attach directory"]\ |Attach directory|\ [/caption] **Result:**
The table *Attachements* is visible and the attachement directory *test*
has been created. It holds the file that was uploaded. [caption
id="attachment\_1018" align="alignnone" width="548" caption="Attachment
directory"]\ |Attachment directory|\ [/caption] **Remark:** the table
*Files* above the attachement browser shows all existing thumbnails and
files that are related to the actual data set. To attach only one
additional object to data set:

#. Choose the option *add attachment*.
#. Click on *Durchsuchen* and choose the first file on your system that
   you want to attach.
#. Click on *Create/Upload* to attach the files.

[caption id="attachment\_1021" align="alignnone" width="562"
caption="Attached file"]\ |Attached file|\ [/caption]
.. rubric:: 7. Technical metadata: Object administration.

**Functional description:** Technical metadata is the term for all
metadata values that are assigned to an object. Not all of them are
necessarily used for display. Apart from the metadata values you entered
this can be:

-  Metadata that comes with an uploaded file such as EXIF, IPTC or PDF
   INFO. These values will be saved with the object to keep all
   information with the object. It is also possible to integrate values
   into the presentation masks/schemes to use them for automatic
   display. Please contact your mediaTUM administrator if you are
   interested in using this feature.
-  Information that was generated from other software, e.g. scanner
   software (size, height, weight, scan date, etc).
-  Internal object information like the used scheme, upload time or
   uploader.

There are a range of special functions for objects that will be listed
and explained in this part. Choose *Edit metadata* and then
*Administration* in the menu and a similar looking page will come up:
[caption id="attachment\_1025" align="alignnone" width="619"
caption="Overview of technical metadata"]\ |Overview of technical
metadata|\ [/caption] **You can see the following sections:**

-  *Node information and special functions for object editing*. In
   general the system updates changes to objects automatically, but
   sometimes it can be useful to start manually the required processes.
-  *Node information*. This section gives an overview of general data.
   To clear the cache for that node click on the button |image15|. This
   feature is needed if the database has been modified but the system
   still holds the previous data in the cache. By using the reload
   button the data is loaded straight from the database and the cache
   for that object is emptied out.
-  *Metadata fields not in use*. Here is all metadata displayed that was
   imported with the object, e.g. EXIF, IPTC or PDF-INFO data. This
   metadata is often attached to images by digital cameras or scanner
   devices and holds specific data like device model, resolution, image
   width and height etc. The attributes and values could be used if
   necessary. To indicate that they are automatically entered and not in
   use their font colour is red.
-  *Metadata that were entered*. This section holds the filled metadata
   fields from the used metadata schema and shows the manually entered
   values. There are displayed the internal IDs of the scheme fields
   that are used behind the names displayed in the edit mask.
-  *Technical metadata that came with object*. This data block contains
   technical metadata that came with the object similar to the ones
   above in font color red. They are separated and in font color black
   because for some EXIF, IPTC or PDFINFO metadata fields a standard
   translation is available. If fields of that kind are imported they
   are displayed with the standard name and shown in this section rather
   than displayed with the raw field name under the red section above.
-  *Attribute editor*. It is also possible to set values for attributes
   straight through the atribute editor.

.. rubric:: 8. Create Identifier

With this function a Hash-ID or an URN can be created. If you can't find
this function in your edit-menu, you can add it in *Administration Area*
in ``System -> Menu configuration -> Edit menu`` if you have
administrator access rights. In order to be able to create urns the
following entries in your ``mediatum.cfg`` are required:
`` [urn] institutionid=91 pubtypes=diss;epub namespace=nbn:de:bvb;nbn:de:4444;nbn:en:1111;publicid;epc``
The values in this snippet have to be replaced by the values of your
company or organisation. The list of the Univorm Resource Names
Namespaces can be referenced
`here <http://www.iana.org/assignments/urn-namespaces/urn-namespaces.xml>`__.
The entries ``pubtype`` and ``namespace`` accept multiple values. In
this case the values have to be separated by semicolon. Once a Hash-ID
or URN has be generated, it won't be changed anymore.
.. rubric:: 9. Preview

To get a preview of an object you have to choose *Layout* and then
*Preview* from the menu. A preview with all metadata fields that hold
values will be displayed with the full view thumbnail. [caption
id="attachment\_1033" align="alignnone" width="738" caption="Object
preview"]\ |Object preview|\ [/caption] To create a printable form of an
object that holds thumbnail and metadata click on one of the printer
symbol on the right. This will create a data sheet in the PDF format
that can either be saved or printed via the print function of the PDF
reader.

.. |Import bibtex data| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/bibtex.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/bibtex.jpg
.. |Bibliographic data set| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/bibtex_2.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/bibtex_2.jpg
.. |Example| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example.jpg
.. |Example| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example2.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example2.jpg
.. |Index entries| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/index-values.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/index-values.jpg
.. |Example| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example3.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example3.jpg
.. |List without empty value| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/tum1.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/tum1.jpg
.. |List with an empty value| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/tum2.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/tum2.jpg
.. |Example| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example41.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example41.jpg
.. |Change/add digital object| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/change.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/change.jpg
.. |Add new thumbnail| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/thumbnail.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/thumbnail.jpg
.. |Attach directory| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/attach-directory.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/attach-directory.jpg
.. |Attachment directory| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/attachment.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/attachment.jpg
.. |Attached file| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/attach-file.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/attach-file.jpg
.. |Overview of technical metadata| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/techmetadata.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/techmetadata.jpg
.. |image15| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/Update_index.gif
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/Update_index.gif
.. |Object preview| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/object-preview.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/object-preview.jpg
