Workflows
---------

1. Introduction

A workflow in mediatum consists of workflow steps like uploading files,
sending email, editing metadata, et cetera. At the end of a workflow
step the workflow may continue to the next step, branch to one of two
directions, or stop when the end of the workflow has been reached.

2. Create a new workflow

You can start the creation of a new workflow by clicking on the golden
box icon. [caption id="attachment\_1162" align="alignnone"
width="853"]\ |Create new workflow| Create new workflow[/caption]
[caption id="attachment\_1169" align="alignnone" width="502"]\ |Create
new workflow| Create new workflow[/caption] **Procedure:**

#. Enter workflow name.
#. Choose the usergroup with write access for this workflow.

**Remark:** The default selection does not limit the write access. When
creating an usergroup you can attribute editor and workflow rights.
Workflow rights will give the users in that usergroup the right to start
and process workflows.

#. You may give a short description.

The following overview shows the basic workflow handling in the fashion
similar to usergroups, users, metadata types, et cetera: [caption
id="attachment\_1172" align="alignnone" width="754"]\ |Existing
worklfows| Existing workflows[/caption] **Editing functions:**

-  Delete workflow by clicking on the red x sign
-  Edit of workflow methadata by clicking on |image3|
-  Export the workflow as xml file |image4|
-  Show diagram. Display the workflow steps as flow diagram by selecting
   the reading-glass sign.
-  Display and edit workflow steps by |image5|

3. Create workflow steps

When you click on the icon |image6| to edit and create workflow steps
you will arrive at a new administration view with a golden box to create
new workflowsteps. [caption id="attachment\_1184" align="alignnone"
width="570"]\ |Create workflow step| Create worklfow step[/caption]
**Procedure:**

#. Enter a name for the workflow step.
#. Decide if you want to mark this step as adminstep. If so, this step
   will be displayed in the workflow status pages in an accentuated
   manner to indicate that it needs special attention.
#. Select the Node type of this workflow step. Currently (as of January
   2012) the following node types for workflow steps are implemented:
   wait, upload node, ACL protection, send email, metadata editor,
   delete entry, edit node, start node, workflowstep-end, publish.
   **Remark:** The fields shown in the above screenshot will be shown
   for every node. Depending on your choise of the node type additional
   fields for the entry of email addresses, metadata masks, etc. will be
   visible.
#. You may add an explanatory Comment to the definition of this step.

The user can be given two options for workflow steps to follow at the
end of this step in the form of buttons. We call those options *True*
and *False*.

#. Enter a Label for the *True* operation. This text will appear on the
   button and may inform the users about the step that will be started
   after a click on this button.
#. Choose a node for *True*. You can select from the nodes for the
   workflow steps you have already created. You may leave this open and
   come back to set this value once you have defined the corresponding
   worklow step.
#. Choose a Label for the *False* operation and a node for *False*.

4. Workflow steps. Overview.

4.1 Start node

**Purpose:** This is the starting point of the workflow. In addition to
the data necessary for every workflow node, one or more metadata types
can be specified in the field *Node types to create (;-separated schema
list):*. A metadata schema has to be entered in the format Datatype/ID.
**For example:** If you have defined metadata types with
``ID=mdtDocument01`` for (pdf) documents and ``ID=mdtImage01`` for
images and if you want to create an object of one of those types at the
start of the workflow, specify
``document/mdtDocument01;image/mdtImage01``. In the field *Text in front
of selection* you can place an additional information or usage
explanations for the user. **Remark:** The rule {user workflow} is added
to the read access of the node of the object. Have a look at the
description for the node type publish on how to remove this rule.

4.2 Edit node

**Purpose:** Show an editor mask to edit metadata for the node created
at the workflow start. You will have to specify the name of an existing
edit mask in field *Editor mask* for the metadata type to be processed.
Normally at least a standard editor mask named editmask should have been
created for all metadata types.

4.3 Metadata editor

**Purpose:** Displays the metadata in one or more masks. This allows the
user to check the metadata already entered. **Additional information for
this node type:** *Text before data:* Text to be displayed before the
first mask shown. Here the user may be asked to check the following
data. *Text after data:* Text to be displayed after the last mask shown:
The user may be informed about the workflow steps. For example, the
displayed data can be accepted or edited in another workflow step.
*Masks to display:* You will have to specify one or more masks to be
diplayed.

4.4 Upload node

**Purpose:** Show an upload form allowing the user to upload a file for
the object currently processed in the workflow. **Additional information
for this node type:** *Text before upload form:* Here the user may be
asked to upload a file. *Text after upload form:* After the user
uploaded the file, a list of links to the copy of the file in the
mediatum data folder, created thumbnail pictures, or the extracted
fulltext, is shown. The user may be asked to check their quality before
proceeding to the next workflow step.

4.5 Send e-mail

**Purpose:** Send email. **Additional information for this node type:**
*Email address* of the *sender*. *Email address* of the *recipient*.
*Subject* of the mail. *Text* of the body. Html markup may be also used
in the mail. *Details editable?*\ (Yes/No): Yes: The email details will
be displayed for editing before being sent. No: The email will be sent
immediately as specified without being displayed. ** *Condition*:
Additionally a preceding condition for sendung the email can be defined.
The mail is only sent if this condition is true. One of the following
criteria can be set as condition:

-  att:[attrname]=[value] -- attrname can be any attribute assigned to
   the workflow node, e.g. author\_fullname
-  schema=[valuelist] (;-separated) -- tests whether the schema of the
   workflow node is matched by one in the given list
-  type=[valuelist] (;-separated)
-  hasfile -- only tests whether there is any file attached to the
   workflow node

*Send PDF form as attachment (checkbox)*: If a PDF has been appended to
the current node (for example by a workflow step of type "Add PDF pages"
the checked state of this checkbox will cause the PDF to be attached to
the mail.

4.6 Delete entry

**Purpose:** Delete the object created during the start of the workflow.

4.7 ACL protection

**Purpose:** A random key is generated. The generated key is added as
*key* to the metadata of the object being processed in the workflow.
This key can be used in protected links (for example, sent in emails to
persons outside your organization) to protect the access to the object.
If you have generated a key using this workflow step, you can insert a
protected link into an email body by inserting ````. A public link
without key can be inserted by ````\ only if the object has not been
protected.

4.8 Publish

**Purpose:** The access restriction rule {user workflow} applied by the
start node is removed from the read access of the node of the object.

4.9 Wait node

The node types *wait* and *metadata editor* are identical in the current
implementation. See node type *metadata editor* for details.

4.10 Show textpage node

**Purpose:** Display a text page. **Additional information for the
node:** *Text to display:* The text to be displayed may contain html
mark up.

4.11 Classify node

**Purpose:** Decide where in the browsing structure of your web page the
created object should be place. **Additional information for the node:**

-  *ID of destination node*. Enter the ID (or a semicolon separated list
   if IDs) of directories or collections in the browsing structure,
   where the current node shall appear. By clicking on the folder icon a
   tree select element will be shown to help to get at those IDs.
-  *attribute name*. An attribute of the current node can be named here
   to specify the name of a child node of the destination nodes. **For
   example:** if the current node has an attribute named
   'year-published' which holds the value '2008', the current node will
   be added as a child node to the sub-directories/sub-collections of
   the destination nodes with the name '2008'. If a destination node
   does not have such a child '2008', a sub-directory with this name is
   created. In the case that only a substring of the attribute value
   shall be used to determine the sub-containers of the destination
   nodes where to place the current node append
   ``|substring index-of-first-letter-in-substring, index-of-first-letter-after-substring``
   to the attribute name. **For example:** if the current node has an
   attribute named 'date-published' which holds the values in the format
   'yyyy-mm-dd', the year alone can be extracted by entering
   ``date-published|substring 0,4``.
-  *only subnode*. If this check box isn't checked the current node will
   be appended as a child directly to the destination nodes (in addition
   to the sub-containers specified in the input box *attribute name*).
   To avoid this, check the box.

4.12 Checkdoublet node

**Purpose:** Check the nodes in the workflow for doublets of the current
node. If no doublets are found the node is transfered to the workflow
step of the 'True'-operation of the checkdoublet workflow step. If
doublets are found, the user will see the doublets and the current node
in a table. The radio buttons in the first table column allow the
selection of the node with which the user wants to continue the
workflow. When clicking on the 'True'-button the user will be transfered
to the selected node in it's current workflow step. **Additional
information for the node:**

-  ***\ Names of checked attributes (;-separated) ** .* Enter the
   technical attribute names for the node attributes to be checked for
   doublicity. If the Python module *Levenshtein* has been installed,
   the *Levenshtein ratio* will be used to mesure (fuzzy) similarity of
   strings. If the *Levenshtein* module is not found, the strings will
   be checked for an exact match ignoring case. The attribute values for
   these attributes will be shown in the doublet table after the radio
   button and the creation time of the respective node.
-  *Exact Fitting Attribut*. This attribute must exactly match for
   doublets. The value will not be show - if not listed also under the
   checkd attributes. This may be used to restrict the doublet
   candidates - for example: to nodes created by a specific user.
-  *List of attributes to show additionally (;-separated)*. To help the
   users identify the different nodes, additional attributes may be
   listed here. Special case: if the attributes of a mask (for example:
   nodebig) for the node type shall be used, the mask can be named by
   entering exclusively 'mask:nodebig' into this field.
-  *Mask list for labels (;-separated)*. A list of masks where to find
   labels for the attributes. The masks are searched in the given order.
   The first label found is used in the header and footer of the table
   column of the attribute. If no label is found (for example: if no
   mask is specified), the technical attribute name of the attribute
   will be used. (Example of an entry: nodebig;nodesmall;editmask)
-  *E: check this to remove doublets when moving to 'True' option*. If
   this check box is checked the doublets will be removed from the
   workflow when the user clicks the 'True'-option. Only the node with
   the selected radio button will remain in the workflow. If unchecked,
   the doublets will remain in the workflow.

4.13 Ldapauth node

**Purpose:** The user will be asked to enter credentials (username and
password) for authentication against the ldap directory configured in
*mediatum.cfg*. If the authentication succeeds, the current node will be
transfered to the workflow step of the 'True'-operation. In case of a
failure, the node is transfered to the workflow step of the
'False'-operation. If no 'False'-operation is defined, this workflow
step will be shown again with an error message to allow a new trial.
**Additional information for the node:**

-  *attribute for username (default: system.ldapauth\_username.* Here a
   node attribute can be named to store the unique distinguished name
   (DN) of the user as returned by the ldap server if the authentication
   succeeds.

4.14 End node (workflowstep-end)

**Purpose:** This is the end of the workflow. **Additional information
for this node type:**

-  *admin\_wfstep\_endtext*: The text typed in this field will appear
   after the workflow has completed it's work. The default end text is:
   *Ready*.
-  *admin\_wfstep\_endremove*: You can decide if the object created in
   this workflow should be removed from the workflow, after it
   terminated, or keep this object hanging on the workflow.

4.15 Condition node

 

This node is used as a branch only. It can be inserted at any position
in the workflow. In case the defined condition is true the workflow will
continue with the node defined in the field "node for true" of the
condition node. Otherwise it will continue with the node defined in its
field "node for false". The condition node itself is never displayed.
One of the following criteria can be set as condition:

-  att:[attrname]=[value] -- attrname can be any attribute assigned to
   the workflow node, e.g. author\_fullname
-  schema=[valuelist] (;-separated) -- tests whether the schema of the
   workflow node is matched by one in the given list
-  type=[valuelist] (;-separated) -- tests whether the schema of the
   workflow node is matched by one in the given list
-  hasfile:[filename]\|[filetype] -- if a complete filename with
   extension is given it is tested whether there is a file attached that
   matches this filename; if only a file extension is given is tested
   whether there is a file attached whose extension matches this file
   extension. If no parameter is specified it is only tested whether
   there is any file attached to the workflow node

4.16 Defer node

**Purpose:** If you want your object to be published after some
perticular date, or you want just to restirct the write access or
download ability till some date, you should use this node. **Additional
information for the node:**

-  *Attributename.* The name of the object attribute, wich specifies the
   defer-date.
-  *Accessattribute.* Here you can specify which actions should be
   restricted: read, write, or data.

4.17 Addpic2pdf node

**Purpose:** Add pictures (for example logos) to pdf pages. The page
range and the position for the placement may be chosen when the step is
displayed. Point of reference is the bottom left corner or the pages -
which may have different width or height. To aid the positioning a grid
of (approximately) 1 cm squares may be layed over the page. The mouse
and arrow keys may be used to place the picture. After inserting an
image the user will be referred back to this step. She may check the
result through the generation of preview pages or viewing the currently
processed pdf using the link under the preview. Now he can insert more
pictures at more positions or reset to the original or accept the
insertions and proceed to the next workflow step. **Additional
information for the node:**

-  *Text before data*\ Text explaining the procedure may be entered
   here.
-  *Upload logo*\ One or more images may be uploaded. The formats .png,
   .jpg, .gif have been tested. Make sure that the image contains
   information about the resolution (dpi) - otherwise the image may not
   scale correctly in the pdf. Transparencies in images are not
   supported in this version.
-  *URL mapping (separator: \|)*\ In this textarea for each uploaded
   picture a link can be defined. The link will be inserted at the right
   hand side of the picture. Each line should start with a string
   matching the file name uniquely. Then followed by a pipe symbol (\|)
   the url of the link. These url's will be offered to the user in input
   boxes under the pictures. This allows the user to edit or delete the
   link before inserting the picture. If only a link without picture is
   needed, a transparent picture may be used.
-  

4.18 Add PDF Pages

**Purpose:** A pdf form will be prepended to the pdf document passing
through the workflow step - or append it to the node as a file of type
"pdf\_form". The text fields of the form will be filled with the
corresponding attribute values of the document node (correspondence by
equality of field and attribute name). **Additional information for the
node:**

-  *Upload one PDF form here* Here the administrator will upload the pdf
   form.
-  *PDF form fields editable* Check this check box if the fields of the
   form shall be left editable.
-  *append PDF form separately to node* Check this check box if PDF form
   should not be prepended to the document, but appended to the node as
   file of type "pdf\_form".

5. Workflow step overview list and workflow diagram

The following screenshots show an example of a workfow step overview and
a snippet from the corresponding workflow diagram created using the
editing functions discribed above. [caption id="attachment\_1205"
align="alignnone" width="768"]\ |Example workflow| Example
workflow[/caption] **Remark:** The worklow steps are alphabetically
ordered in this list. In the following workflow diagram the nodes are
represented as rectangles with green arrows linking to the node for
*True* and red arrows linking to the node for *False*. This diagram will
be shown after clicking on *open workflow definition* in the top left
corner of the preceding view, or by clicking on the reading-glass sign
in the *Existing workflows* view. [caption id="attachment\_1209"
align="alignnone" width="359"]\ |Workflow diagram| Workflow
diagram[/caption]

6. Starting a workflow

If you are logged in with workflow rights you will see a menu item
*Workflows*. |image10| After selecting the menu item *Workflows*, a list
of the available workflows will be shown. [caption id="attachment\_1214"
align="alignnone" width="583"]\ |Available workflows| Available
workflows[/caption] After clicking on the name of a workflow a status
page for that workflows will be shown. [caption id="attachment\_1216"
align="alignnone" width="721"]\ |Status page of a worklow| Status page
of a workflow[/caption] In the status page the various workflow nodes
are listed with the count of the objects that are currently waiting to
be processed by that workflow step. Workflow steps marked as Admin steps
are highlighted (check data in this example). This might be usefull when
many workflow steps exist and only some of them need the attention or
interference of the administrator. You can start to process an object in
the workflow with a click on the objects count (X) of the start node or
by directing the browser to ``/publish/workflow_name/start_step_name``
(``/publish/test_workflow_02/start`` in this example). At the start the
user will be asked to create a new object associated with the start
node. After doing so the user will be transfered to the node for *True*
of the start node. **Remark:** When clicking on the object count of the
steps other than the start of the workflow, an overview list of the
objects waiting to be processed by that step will be shown. [caption
id="attachment\_1218" align="alignnone" width="730"]\ |Objects to be
processed| Objects to be processed[/caption] In this overview the ID of
the node representing the object is shown together with the creation
time of the object. The name is only shown when the object has been
named. In the other columns a click on the last column will transfer the
object directly to the node for *True* and a click on the second column
from right to the node for *False*. A click on the column *Editor* will
show the object in the editor. This will allow to edit the metadata or
place the object in the browsing structure (use menu item
*Classification/Place in Browsing Structure*). A click on the column
*Step* will open the workflow step in the browser.

Example

Here an example for workflow "Article upload and publishing". A user,
which has a right to upload pdf files, can

-  upload his article
-  enter its title and author's name
-  apply for publication of his article

The publication will be then permitted (or denied) by administrator.
Here the workflow definition: [caption id="attachment\_1330"
align="aligncenter" width="500"]\ |Workflow properties| Workflow
properties[/caption] As you can see the users from the usergroup
``irareGroup`` have a writing right for this workflow. The administrator
has automatically all the rights for all workflows. |image15|\ |image16|
In the diagramm above you can see all the defined workflow steps. The
definition of each step follows below. [caption id="attachment\_1328"
align="aligncenter" width="1010"]\ |Workflow steps| Workflow
steps[/caption] In the definition of the start step the type of node to
be created is defined. This step is visible for users of the group
``irareGroup``. [caption id="attachment\_1326" align="aligncenter"
width="655"]\ |Start step| Start step[/caption] The next step is the
upload step: [caption id="attachment\_1323" align="aligncenter"
width="585"]\ |Upload step| Upload step[/caption] Then we should give
the user the opportunity to enter the author's name and the title of the
article. [caption id="attachment\_1333" align="aligncenter"
width="560"]\ |Edit step| Edit step[/caption] After a user has pushed
the button *Apply for publication* a text page with a short message will
be shown. [caption id="attachment\_1335" align="aligncenter"
width="566"]\ |Text page| Text page[/caption] Notice that the labels of
true and false operations are empty, in order to prevent the publication
by the user itself. For the same reason, we mark the next step as admin
step. [caption id="attachment\_1337" align="aligncenter"
width="595"]\ |First admin step| First admin step[/caption] After the
administrator has permitted the publication, the publish-node will be
executed. [caption id="attachment\_1340" align="aligncenter"
width="564"]\ |Publish| Publish[/caption] After the article was
published, it will be integrated into the browsing structure of
**mediaTUM**. [caption id="attachment\_1342" align="aligncenter"
width="565"]\ |Classify node| Classify node[/caption] Then the workflow
will be finished. [caption id="attachment\_1344" align="aligncenter"
width="571"]\ |End step| End step[/caption] Now the user ``irare`` of
the ``irareGroup`` can upload a document and complete its metadata:
[caption id="attachment\_1348" align="aligncenter" width="488"]\ |An
article was uploaded| An article was uploaded[/caption] After entering
the author's name and title of the article, the user ``irare`` can see
the following page [caption id="attachment\_1350" align="aligncenter"
width="735"]\ |Text displayed to the user| Text displayed to the
user[/caption] In oder to publish the uploaded document, administrator
has to permit the publication. As you can see in the table below, the
document hangs at the first administrator step. [caption
id="attachment\_1353" align="aligncenter" width="694"]\ |Document
attached at the first "administarotr step"| Document attached at the
first "administarotr step"[/caption]

.. |Create new workflow| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/create-workflow.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/create-workflow.jpg
.. |Create new workflow| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/create-new-workflow.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/create-new-workflow.png
.. |Existing worklfows| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/existing-workflows.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/existing-workflows.png
.. |image3| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/Edit.gif
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/Edit.gif
.. |image4| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/export.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/export.png
.. |image5| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/rightarrow.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/rightarrow.png
.. |image6| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/rightarrow1.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/rightarrow1.png
.. |Create workflow step| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/create-workflow-node.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/create-workflow-node.jpg
.. |Example workflow| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example-workflow.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/example-workflow.jpg
.. |Workflow diagram| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow-diagram.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow-diagram.jpg
.. |image10| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/worklfow.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/worklfow.jpg
.. |Available workflows| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/available-workflows.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/available-workflows.jpg
.. |Status page of a worklow| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/status-page.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/status-page.jpg
.. |Objects to be processed| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/objects-to-be-processed.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/objects-to-be-processed.jpg
.. |Workflow properties| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow1.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow1.png
.. |image15| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow-diagram1.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow-diagram1.jpg
.. |image16| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow-diagram2.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow-diagram2.jpg
.. |Workflow steps| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow2.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow2.png
.. |Start step| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/startstep.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/startstep.png
.. |Upload step| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/uploadstep.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/uploadstep.png
.. |Edit step| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/editstep1.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/editstep1.png
.. |Text page| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/textstep.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/textstep.png
.. |First admin step| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/firstadminstep.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/firstadminstep.png
.. |Publish| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/publishstep.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/publishstep.png
.. |Classify node| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/classifystep.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/classifystep.png
.. |End step| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/endstep.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/endstep.png
.. |An article was uploaded| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/edit.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/edit.png
.. |Text displayed to the user| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/text.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/text.png
.. |Document attached at the first "administarotr step"| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow.png
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2012/01/workflow.png
