Anwender - Dokumentation
========================

.. figure:: images/Recherche.png
   :alt: Recherche.png
   
   

Suche
-----

In dem Eingabefeld links oben kann eine einfache Suche durchgeführt werden. 
Beim Aufruf der Startseite von mediaTUM wird eine Suche im Gesamtbestand durchgeführt. 
Wechselt man in eine Kollektion oder ein Unterverzeichnis, werden nur diese Bestände durchsucht.
Für einzelne Kollektionen kann auch eine erweiterte Suche durchgeführt werden, 
erreichbar über den Link "Erweiterte Suche". Hier kann gezielt nach Inhalten in einzelnen 
Felder gesucht werden: neben der Eingabe von Suchbegriffen ist eine Auswahl aus Index-Listen möglich. 
Welche Felder durchsuchbar sind, wird vom Inhaber der Kollektion festgelegt: :ref:`Suche Einrichten`.



Dokumente in der Vollanzeige
----------------------------

Nach der Auswahl in der Trefferliste wird das Dokument in der Vollansicht angezeigt. 
Angezeigt werden die Metadaten des Dokuments, die im Bibtex-Format exportiert werden können.
Ist ein Volltext vorhanden, kann er über einen Klick auf das Thumbnail aufgerufen werden.

Der Zugriff auf einen Volltext kann über IP-Adressen (z.B. campusweit) oder Benutzergruppen geregelt werden. 
Nicht immer ist ein Volltext vorhanden, u.a. aus urheberrechtlichen Gründen. 


.. _Export von Trefferlisten:

Möglichkeiten zum Export von Trefferlisten
------------------------------------------

Allgemeine Informationen
^^^^^^^^^^^^^^^^^^^^^^^^

Folgender Link ist Ausgangspunkt und muss angepasst werden:
http://mediatum.ub.tum.de/services/export/node/ID/Hierarchie?format=Formatangabe

Im Link muss eingesetzt werden:

-  **ID:** muss mit der ID z.B. 123456 des gewünschten Verzeichnisses
   ausgetauscht werden. Ermitteln Sie eine ID, indem Sie in das
   gewünschte Unterverzeichnis navigieren, dort finden Sie im Link
   "?id=123456".
-  **Hierarchie:** Gemeint ist hier die Ebene innerhalb der des
   Verzeichnisses gesucht werden sollen.
-  Ohne Angabe der Hierarchie wird nur der Knoten selbst ausgegeben.
-  Um das Eltern-Element anzuzeigen setzen Sie **„parents“** ein.
-  Ausgabe von Inhalten des Knotens (ohne Unterverzeichnissen) erhalten
   Sie mit **„children“**
-  **„allchildren“** gibt zusätzlich Inhalte der Unterverzeichnisse aus.
-  **attrspec=all** bzw. **attrspec=none** Alle/Keine Felder anzeigen
-  **& limit=999999**: limit auf beliebige Zahl erhöhen

**Ausführliche Informationen:**

-  Zu erweiterten Suchmöglichkeiten:
   http://wiki.ub.tum.de/mediatum\_dev/index.php5/Mediatume\_dev:Webservice\_REST
-  Zu Publikationslisten, mit mediaTUM als Quelle:
   https://www.typo3.tum.de/index.php?id=61&L=0

Ansichten - CSV, JSON, RSS, XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Es ist möglich mithilfe von bestimmten Links in mediaTUM zu Suchen und
  sich die Trefferliste in einem der verfügbaren Formate (CSV, JSON,
  RSS, XML) anzeigen zu lassen. Folgender Link ist Ausgangspunkt und
  muss angepasst werden:
  http://mediatum.ub.tum.de/services/export/node/ID/Hierarchie?format=Formatangabe
| **Formatangabge:** Die Formatangabe wird einfach mit *csv, json, rss*
  oder *xml* angegeben. Ohne Angabe wird standardmäßig XML ausgegeben.

Download - Excel
^^^^^^^^^^^^^^^^

Ausgangslink:
http://mediatum.ub.tum.de/services/export/node/ID/allchildren?format=csv&sep=;&delimiter=dquote&bom&mimetype=application/vnd.ms-excel
**ID** wird mit dem Knoten des zu durchsuchenden Bereichs ausgetauscht.
Außerdem kann **„allchildren“** ausgetauscht werden, damit nach der
gewünschten Hierarchiestufe gesucht wird (:ref:`Export von Trefferlisten`). Die
Einschränkung der Treffer einer Suchanfrage ist nicht möglich und es
werden immer alle Felder angezeigt.

Suche nach Metadatenschemata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Soll nach einem bestimmten Metadatenschema gesucht werden, muss die
Suche auf das gewünschte Metadatenschema eingegrenzt werden. Im Beispiel
wird nach dem Schema „dt-konferenzbeitrag“ gesucht, es wurde folgender
Befehl hinzugefügt: **?q=schema=dt-konferenzbeitrag** Beispiel:
http://mediatum.ub.tum.de/services/export/node/993185/allchildren/?q=schema=dt-konferenzbeitrag
