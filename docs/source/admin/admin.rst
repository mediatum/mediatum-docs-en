Benutzer / -gruppen Verwaltung
==============================


.. figure:: images/AdminNeuStart.png
   :alt: AdminNeuStart.png


Nach dem Login erweitert sich die Menüleiste um:

-  User

 -  User
 -  User Group
 -  Authenticator Info

-  Node

 -  Node
 -  File

-  Setting
-  ACL

 -  Access Rule
 -  Access Ruleset
 -  Access Ruleset To Rule

-  Redis Cli

Ganz rechts ist ein kleines Dreieck in der Menüleist, über das man den
Logout erreicht.

User
----

.. figure:: images/Benutzer.jpg
   :alt: Benutzer.jpg


Zunächst werden die Nutzer aufgelistet und man kann grobe Informationen
in tabellarischer Sicht einsehen. Es ist ein Suchschlitz vorhanden und
es kann nach Spalten auf-/absteigend sortiert werden. Mit Add Filter
kann man die Suche eingrenzen und mit "With Selected" ausgewählte Nutzer
z.B. löschen. Das Löschen funktioniert ebenfalls über die Liste mit dem
Mülleimersymbol.

.. warning::

    **Achtung:** Hat ein Nutzer sich jemals eingeloggt, ist
    das Löschen nicht mehr möglich! In diesem Fall müssen sämtliche
    Gruppen des Nutzers entfernt werden. So wird der Account deaktiviert!

Blau unterlegte Felder lassen sich in der Liste direkt anklicken und
bearbeiten.

In der Übersicht:

-  Das Augensymbol oder Create zeigt einen einzigen Benutzer an:
   |BenutzerAuge|
-  Der Stift oder Edit führt zur Ansicht für die Bearbeitung eines
   Benutzers: |BenutzerStift|
-  In dem Feld "Groups" kann man die Benutzergruppe aus einem
   Dropdownmenü auswählen.
-  Export stellt eine CSV Datei zum Download der Benutzer zur Verfügung.

.. figure:: images/CreateUser.jpg
   :alt: CreateUser.jpg


**Vor der Benutzererstellung soll immer geprüft werden, ob dieser Nutzer
bereits einen Account hat.**

-  **Kurzinfos zu Benutzertyp**
-  Interne Nutzer:
-  internal: default - mit dieser Auswahl wird ein interner Nutzer
   angelegt, das Passwort muss ebenso, wie sämtliche Felder händisch
   eingetragen werden. Es gilt: Informationen einzutragen, die vorhanden
   sind.

+--------------------+--------------------------+-----------------------------------------------------+
| Feldbezeichnung    | Beschreibung             | Interner Nutzer                                     |
+====================+==========================+=====================================================+
| **Home Dir:**      | Gibt ID des              | wird nach erstem Öffnen des Editbereichs angelegt   |
|                    | Homeverzeichnisses an    |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **Authenticator    |Legt die Art des          | internal: default                                   |
| Info:**            |Accounts fest             |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **ID:**            | Gibt ID des Benutzers an.| wird automatisch angelegt                           |
+--------------------+--------------------------+-----------------------------------------------------+
| **Login Name:**    | Kennung zum einloggen.   | händisch eintragen                                  | 
+--------------------+--------------------------+-----------------------------------------------------+
| **Distplay Name:** | Name der nach dem Login  | kann optional ausgefüllt werden.                    |
|                    | angezeigt wird, z.B.     |                                                     |
|                    | Rechercheansichten neben |                                                     |
|                    | "Logut".                 |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **Lastname:**      | Nachname                 | Nach vorhandenen Informationen ausfüllen            |
+--------------------+--------------------------+-----------------------------------------------------+
| **Firstname:**     | Vorname                  | Nach vorhandenen Informationen ausfüllen            |
+--------------------+--------------------------+-----------------------------------------------------+
| **Telephone:**     | Telefonnr.               | Nach vorhandenen Informationen ausfüllen            |
+--------------------+--------------------------+-----------------------------------------------------+
| **Organisation:**  | Organisation / Lehrstuhl | Nach vorhandenen Informationen ausfüllen            |
+--------------------+--------------------------+-----------------------------------------------------+
| **Comment:**       | Zusätzliche Informationen| Kann optional ausgefüllt werden                     |
|                    | zum Nutzer               |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **Email:**         | Email-Adresse            | Nach vorhanden Informationen ausfüllen              |
+--------------------+--------------------------+-----------------------------------------------------+
| **Passwort Hash:** | Passwort wird zum        | Wird automatisch ausgefüllt,  nach dem Anlegen des  |
|                    | abspeichern in Hash      | Nutzers                                             |
|                    | umgewandelt              |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **Salt:**          | Gehört als Ergänzung zum | Wird automatisch ausgefüllt,  nach dem ersten Login |
|                    | Feld "Passwort-Hash"     |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **Last Login:**    | gibt den Zeitpunkt des   | wird automatisch angelegt,  frühestens nach dem     |
|                    | letzten Logins des       | ersten Login                                        |
|                    | Nutzers an               |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **Active:**        | Noch nicht implementiert | siehe links                                         |
+--------------------+--------------------------+-----------------------------------------------------+
| **Cand Edit**      | Noch nicht implementiert | siehe Links                                         |
| **Shoppingbag:**   |                          |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **Can Change       | Nutzer kann selbst       | Aktiviert Zugriff auf die Funktion                  |
| Password:**        | Passwort verändern       |                                                     |
+--------------------+--------------------------+-----------------------------------------------------+
| **Password:**      | Passwort festlegen       | Bei Internen Benutzern muss ein Passwort händisch   |
|                    |                          | angegeben werden.                                   |
+--------------------+--------------------------+-----------------------------------------------------+
| **Created At:**    | Ersstellungsdatum des    | Wird automatisch ausgefüllt,                        |
|                    | Nutzeraccounts           |  nach dem Anlegen des Nutzers                       |
+--------------------+--------------------------+-----------------------------------------------------+
| **Groups:**        | Benutzergruppen, zu denen| Eintragen der ersten Buchstaben, dann erscheint eine| 
|                    | der Nutzer gehören soll  | Liste der verfügbaren Gruppen zur Eintragung        |
|                    |                          | (Mehrfachauswahl).                                  |
+--------------------+--------------------------+-----------------------------------------------------+

User Group
----------

Die Benutzergruppe hat analoge Funktionen wie bei den Nutzern, hier nur
die Unterschiede:

-  Erstellen einer neuen Benutzergruppe |GruppeCreate|

-  **Name:** Dieser Name muss immer vergeben werden und muss eindeutig
   sein.
-  **Description:** Die Beschreibung sollte ein paar Informationen über
   die Gruppe bereitstellen, wie zum Beispiel, der Lehrstuhl, für den
   diese Gruppe erstellt wurde.
-  **Hidden Edit Functions:** Der bisherige "eidentifier" wurde nun
   umbenannt zu "identifier" - Standardmäßig sollen nun folgende
   Funktionen ausgeblendet werden: identifier - bis weiteres in Ticket
   #950 geklärt ist
-  **Is Editor / Workflow Editor / Admin Group:** hier werden jeweils
   die Rechte bei vorhandenem Haken hinzugefügt.
-  **Created At:** Wird automatisch nach erstellen der Gruppe
   ausgefüllt.
-  **Versions:** Ein Dropdown Menü ist verfügbar.
-  **Users:** Benutzer können mit dem Dropown Menü gefunden werden. Das
   eingeben von Zeichen führt zu einer Eingrenzung der Liste.

Menüpunkt Authenticatior Info
-----------------------------

Hier werden die verschiedene Benutzertypen von der Datenbank
aufgelistet.

-  Internal = Interne Benutzer
-  Weitere, falls mediaTUM entsprechend ergänzt wurde


Node, File, Setting
-------------------

Die Menüpunkte Node, File und Setting beinhalten Anzeigen, die die
tieferen Ebenen der Datenbank darstellen. Diese sollen von den Admins
zunächst nicht weiter berücksichtigt werden. Diese Punkte sollen
demnächst ausgeblendet werden.


System-Einstellungen
==============================

Menü Konfiguration
------------------

In der Menü Konfiguration können Sie definieren, welche Optionen im
Edit- und Administrationsbereich verfügbar sind. Die jeweilige
Reihenfolge der Buttons ist ebenfalls individuell veränderbar.


Im ersten Reiter sehen Sie die Konfiguration des Adminbereichs:

.. figure:: images/MenKonf1.jpg
   :alt: MenKonf1.jpg

   

Wählen Sie den 2. Reiter aus, damit der Editbereich angezeigt wird.
Zuerst müssen Sie einen Datentyp aus dem Dropdownmenü auswählen, da die
Ansicht für jeden Datentyp unterschiedlich eingerichtet werden kann.

.. figure:: images/MenKonf2.jpg
   :alt: MenKonf2.jpg


Im nächsten Bild dient der Datentyp Dokument als Beispiel, die Ansicht
ähnelt der Konfiguration des Adminbereichs. 

.. figure:: images/MenKonf3.jpg
   :alt: MenKonf3.jpg
   
Funktionen in beiden Bereichen
------------------------------

-  |Pfeile| Verändern Sie die Reihenfolge der Optionen mithilfe
   dieser Pfeile.
-  |Loeschen| Diese Option wird ausgeblendet.
-  Blenden Sie die Option wieder ein, indem Sie im rechten Dropdownmenü
   auf -Verschieben- klicken und eine Oberkategorie auswählen, zu der
   die Option hinzugefügt werden soll.

Hier das Dropdownmenü:

.. figure:: images/MenKonf4.jpg
   :alt: MenKonf4.jpg





Editor für Admins
==============================

Symbole
-------

+--------------------+------------------------------------+
| **Symbol**         | **Bedeutung**                      |
+====================+====================================+
| |Pfeil|            | Einzelheiten anzeigen              |
+--------------------+------------------------------------+
| |Neu|              | Neues Element erstellen            |
+--------------------+------------------------------------+
| |Maske|            | Anzeigen und Bearbeiten            |
+--------------------+------------------------------------+
| |Lupe|             | Gesamte Übersicht                  |
+--------------------+------------------------------------+
| |Bearbeiten|       | Datensatz bearbeiten               |
+--------------------+------------------------------------+
| |Pfeile|           | Nach oben bzw. unten verschieben   |
+--------------------+------------------------------------+
| |Export|           | Auswahl exportieren                |
+--------------------+------------------------------------+

.. |BenutzerAuge| image:: images/BenutzerAuge.jpg
.. |BenutzerStift| image:: images/BenutzerStift.jpg
.. |GruppeCreate| image:: images/GruppeCreate.jpg


.. |Edit| image:: ../images/Edit.jpg
.. |Pfeile| image:: ../images/Pfeile.jpg
.. |Pfeil| image:: ../images/Pfeil.jpg
.. |Loeschen| image:: ../images/Loeschen.jpg
.. |Lupe| image:: ../images/Lupe.jpg
.. |Neu| image:: ../images/Neu.jpg
.. |Maske| image:: ../images/Maske.jpg
.. |Bearbeiten| image:: ../images/Bearbeiten.jpg
.. |Export| image:: ../images/Export.jpg