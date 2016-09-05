User administration
-------------------

1. Usergroups

The system’s rights management is based on user groups. Therefore, first
step is creating a user group that can hold one or more single user.
After installing the system there is just one user group, the
Administration group.

[caption id="attachment\_754" align="alignnone" width="300"
caption="Usergroups"]\ |Usergroups|\ [/caption]

The following user group operations are available:

-  Create new user groups
-  Edit user groups
-  Delete user groups

1.1 Create new usergroup

[caption id="attachment\_759" align="alignnone" width="300"
caption="Create usergroup"]\ |Create usergroup|\ [/caption]

#. Click on the yellow box symbol in the right upper corner of the user
   group overview.
#. Enter name of user group.
#. You can add descriptive text for the group (optional).
#. Grant permissions for editor and workflow rights (if required)
#. Leave checkbox *create access rule for current user group* checked.
#. MediaTUM is based on different editing modules. That means for a
   usergroup you can exclude certain editing functions. This can be done
   by hiding them. By default all modules are available; you have to
   move one or more modules from the right to the left box to deny
   access in the edit mode for this group. Just double click the name of
   the module or mark it and click on the arrow button between the
   fields.
#. Click on *Save*.

**Result:** New usergroup is listed in overview:

[caption id="attachment\_762" align="alignnone" width="300" caption="New
usergroup"]\ |New usergroup|\ [/caption]

1.2 Edit / delete usergroups

The overview **(1)** shows you all existing user groups, the number of
users in the user group **(2)**, the assigned metadata schemes **(3)**,
if editing rights **(4)** and workflow rights **(5)** are given.

[caption id="attachment\_764" align="alignnone" width="300"
caption="Usergroups overview"]\ |Usergroups overview|\ [/caption]

You can edit usergroups by clicking on the yellow pen symbol **(6)**;
delete user groups by clicking on the red symbol **(7)**. **Remark:** A
usergroup can only be deleted when no users are assigned to this group.

2. Users

[caption id="attachment\_768" align="alignnone" width="300"
caption="Users"]\ |Users|\ [/caption]

To get an overview of all existing users, click on *Users* in submenu
*User administration*. All users are listed with their username and
email address and optional first and/or last name and organsation. You
can also see the usergroups that are assigned to the user.

[caption id="attachment\_771" align="alignnone" width="300"
caption="Users overview"]\ |Users overview|\ [/caption]

The following user operations are available:

#. Create new user: yellow box icon
#. Edit user: document with pen icon
#. Send email to user: envelope icon
#. Delete user: red x icon

2.1 Create new user

Click on yellow box in user overview. The single user edit interface
will come up.

[caption id="attachment\_773" align="alignnone" width="270" caption="Add
user"]\ |Add user|\ [/caption]

**Procedure:**

#. Enter name of new user and email address. This email-address will be
   used for sending the user account details later. Optional you can add
   first and last name of the user.
#. Allocate user to one or more user groups (Multiple selection: press
   CTRL-button while selecting with mouse)
#. If necessary activate checkbox *Password changeable*
#. Save new user

**Result:** User is listed in overview with all assigned usergroups.

[caption id="attachment\_777" align="alignnone" width="300"
caption="Users overview"]\ |Users overview|\ [/caption]

To send the login details to the user via email, click the envelope
symbol **(5)**. Preformatted text will be displayed. This text can be
manually edited before sending. **Remark:** By sending the password you
also reset the password. The lock symbol **(6)** shows the status of the
password. Unlocked means the password has not been sent to the user via
email or has been changed.

2.2 Edit / delete users

To delete a user - click on red x icon in the list beside the user. To
edit the user - click on the edit symbol in the user list.

2.3 Password allocation

**Reset password** To change a user password just send login details via
email (envelope symbol). A new password for this user name will be
generated and sent. The old password is no longer valid. **Special
password configuration** If user wants a particular password (e.g.
"testpassword") where the password is not changeable (checkbox "Password
changeable" not checked), edit already created user by clicking the edit
button in the user overview. Enter the desired password in *new
password* field. Click on the lock symbol |image8| **Remark:** This
function cannot be used when first creating a user account, you first
have to create the account in the common way. Do not send the login
information (user name & password) via the envelope symbol. Instead send
the new login information to the user in a separate email.

.. |Usergroups| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_1-usergroup-300x138.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_1-usergroup.jpg
.. |Create usergroup| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_1_1_createusergroup-300x215.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_1_1_createusergroup.jpg
.. |New usergroup| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_1-usergroup-3-300x115.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_1-usergroup-3.jpg
.. |Usergroups overview| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_1_2-groupoverview-300x73.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_1_2-groupoverview.jpg
.. |Users| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_2-start-300x115.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_2-start.jpg
.. |Users overview| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/users_overview1-300x81.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/users_overview1.jpg
.. |Add user| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_2_1_adduser-270x300.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_2_1_adduser.jpg
.. |Users overview| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_2-email-new2-300x134.jpg
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/3_2-email-new2.jpg
.. |image8| image:: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/Archive.gif
   :target: http://mediatum.sourceforge.net/documentation/wp-content/uploads/2011/12/Archive.gif
