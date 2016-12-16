Anwender-Dokumentation
======================

Die folgenden Abschnitte beschreiben Funktionalitäten von mediaTUM für die eine Registrierung und Anmeldung des Nutzers nicht notwendig ist.

.. figure:: images/Recherche.png
   :alt: Recherche.png
   

Navigationsbaum
---------------

Auf der linken Seite befindet sich der Navigationsbaum.
Er ist hierarchisch aufgebaut und ermöglicht den gezielten Aufruf einzelner Kollektionen.


Suche
-----

In dem Eingabefeld links oben kann eine einfache Suche durchgeführt werden. 
Beim Ausführen einer Suche auf der mediaTUM Startseite wird eine Suche im Gesamtbestand durchgeführt.
Wechselt man in eine Kollektion oder ein Unterverzeichnis, werden nur diese Bestände durchsucht.
Für einzelne Kollektionen kann auch eine erweiterte Suche durchgeführt werden, erreichbar über den Link "Erweiterte Suche".
Hier kann gezielt nach Inhalten in einzelnen Felder gesucht werden:
neben der Eingabe von Suchbegriffen ist eine Auswahl aus Index-Listen möglich.
Welche Felder durchsuchbar sind, wird vom Inhaber der Kollektion festgelegt: :ref:`Suche Einrichten`.


Dokumente in der Vollanzeige
----------------------------

Nach der Auswahl in der Trefferliste wird das Dokument in der Vollansicht angezeigt. 
Angezeigt werden die Metadaten des Dokuments, die auch im Bibtex-Format exportiert werden können.
Ist ein Volltext vorhanden, kann er über einen Klick auf das Thumbnail aufgerufen werden.

Der Zugriff auf einen Volltext kann über IP-Adressen (z.B. campusweit) oder Benutzergruppen geregelt werden. 
Nicht immer ist ein Volltext vorhanden, z.B. aus urheberrechtlichen Gründen.


Publikationsliste
-----------------




.. _Export von Trefferlisten:

Möglichkeiten zum Export von Trefferlisten
------------------------------------------

Allgemeine Informationen
^^^^^^^^^^^^^^^^^^^^^^^^   
          
Der Export-Link besitzt folgenden Aufbau::

    https://mediatum.ub.tum.de/services/export/node/ID/HIERARCHIE?format=FORMATANGABE

- **ID:** ID des Verzeichnisses, dessen Inhalt exportiert werden soll. So wird die ID ermittelt:
  Nach einem Wechsel in das gewünschte Verzeichnis über den Navigationsbaum kann die gesuchte ID im Adressfeld des Browsers abgelesen werden, z.B.::

      https://mediatum.ub.tum.de/604223
      
      
- **Hierarchie:** Was wird ausgegeben?

    - Keine Angabe: die ID selbst
    - parents: das Eltern-Element
    - children: die direkten Kind-Elemente (ohne den Inhalt von Unterverzeichnissen)
    - allchildren: alle Kind-Elemente (mit den Inhalten von Unterverzeichnissen)

- **Formatangabe:** Die Daten können in unterschiedlichen Formaten ausgegeben werden. XML wird standardmäßig ausgeliefert. Möglich sind auch JSON, CSV und RSS.


| **Weitere Optionen:**

- Einschränkung auf Datentypen mit ``type=[...]``

    - ``?type=directory``: listet nur Unterverzeichnisse des Elements auf
    - ``?type=document``: listet nur Dokumente auf
    - ``?type=dt-buchbeitrag``: listet nur Buchbeiträge auf; gesucht wird der Name des Metadatenschemas

- Anzahl der angezeigten Elemente verändern mit ``limit=[...]:`` 

    - ``?limit=5``: Limitierung auf 5 Elemente
    
- Einschränkung des Ergebnisses durch eine Suche mit ``q=[...]``

    - ``?q=regen``: der Suchbegriff wird in den Metadaten und im Volltext gesucht
    - ``?q=year=2016``: der Suchbegriff wird in einem Metadatenfeld (hier: year) gesucht
          Die Operatoren => (größer gleich) und <= (kleiner gleich) können für numerische Suchen verwendet werden. Die Operator > und < können nicht verwendet werden. 
          
- Suche mit regulären Ausdrücken mit ``attrreg=[...]``, schneller als die Suche mit ``q=[...]``

    - ``?attrreg=author-contrib=.*Lei[ß|s].*``: Suche nach Leiß oder Leis im Autorenfeld
    
- Sortierung mit ``sortfield=[...]``

    - ``?sortfield=-year``: absteigende Sortierung nach dem Inhalt des Feldes "year"
    - ``?sortfield=year``: aufsteigende Sortierung nach dem Inhalt des Feldes "year"
    
- Ausgabe der Inhalte über definierte Export-Masken im Feld <mask>  mit ``mask=[...]``, angegeben wird der Name der Export-Maske
    
    - ``mask=none``: keine Ausgabe
    - ``mask=default`` oder ``mask=nodesmall``: Kurzanzeige (nodesmall)
    - ``mask=bibtex``: Ausgabe im Bibtex-Format
    - ``mask=apa``: Ausgabe im APA-Format 
    
- Angezeigte Felder auswählen (beim JSON-Format) mit ``attrspec=[...]`` und ``attrlist=[...]``

    - ``attrspec=none``: keine Felder werden angezeigt
    - ``attrspec=all``: alle Felder werden angezeigt (default)
    - ``attrspec=none&attrlist=year,author-contrib``: angezeigt werden nur die Felder year und author-contrib


**Ausführliche Informationen:**

-  Zu erweiterten Suchmöglichkeiten:
   http://wiki.ub.tum.de/mediatum\_dev/index.php5/Mediatume\_dev:Webservice\_REST
-  Zu Publikationslisten, mit mediaTUM als Quelle:
   https://www.typo3.tum.de/index.php?id=61&L=0


   
Download als Excel-Datei
^^^^^^^^^^^^^^^^^^^^^^^^

Einen Export im Excel-Format erhält man über folgenden Link::

    http://mediatum.ub.tum.de/services/export/
    node/ID/allchildren?format=csv&sep=;&delimiter=dquote&bom&mimetype=application/vnd.ms-excel

**ID** und **allchildren** sind auszutauschen bei Bedarf, Vgl. (:ref:`Export von Trefferlisten`). 
Das Ergebnis kann in einer Tabellenkalkulation sortiert und gefiltert werden. Eine Einschränkung 
der Treffermengen mit Suchen und die Einschränkung der angezeigten Felder sind nicht möglich. 


BibTeX-Export
^^^^^^^^^^^^^

Export im BibTeX-Format
"""""""""""""""""""""""

Der Export-Link für das BibTeX-Format hat folgenden Aufbau::

    http://mediatum.ub.tum.de/services/export/
    node/ID/allchildren/?format=template_test&mask=bibtex&lang=de&template=$$[defaultexport]$$\n\n&mimetype=text/plain


**ID** und **allchildren** sind auszutauschen bei Bedarf, Vgl. (:ref:`Export von Trefferlisten`).



Merkliste : Download im BibTeX-Format
"""""""""""""""""""""""""""""""""""""

.. |MerkStern| image:: ../images/MerkLiStern.png

.. |ObjekteMarkieren| image:: images/ObjekteMarkieren.png

- Aufruf eines beliebigen Verzeichnisses.

.. figure:: images/Trefferliste.png
   :alt: Trefferliste.png

    
- Auswahl des gewünschten Verzeichnisses über die Navigation, z.B. „Prof. O. Fischer“


.. figure:: images/Auswahl.png
   :alt: Auswahl.png
   
   
- In der Anzeige werden standardmäßig nur neun Treffer angezeigt. Den Link „alle anzeigen“ anklicken, um eine vollständige Trefferliste zu erhalten.
- Auf das Symbol |MerkStern| oberhalb der Trefferliste klicken („Aufgelistete Objekte in die Merkliste hinzufügen“).


.. figure:: images/Hinzufügen.png
   :alt: Hinzufügen.png
   
   
- Es erscheint die Meldung, dass die Dokumente der Merkliste hinzugefügt wurden.


.. figure:: images/Meldung.png
   :alt: Meldung.png
   
- Klickt man auf das Merklisten-Symbol |MerkStern|, wird der Inhalt der Merkliste angezeigt.


.. figure:: images/MerklisteAnzeigen.png
   :alt: MerklisteAnzeigen.png
   
   
.. figure:: images/MerklisteInhalt.png
   :alt: MerklisteInhalt.png
   
   
- Nachdem alle Objekte über den Button |ObjekteMarkieren| markiert worden sind, öffnet man über den Link „Export…“ das Export-Menü. Nach einem Klick auf das bibtex-Symbol wird der gewünschte Bibtex-Export gestartet. Die bibtex-Datei kann nun weiterverarbeitet werden.   


.. figure:: images/Export.png
   :alt: Export.png


Print-Funktion
^^^^^^^^^^^^^^

Die Print-Funktion kann über das eingeblendete Druckersymbol aufgerufen werden.
Mit ihr können alle Einträge einer Kollektion als PDF-Dokumente exportiert werden.