.. _intro:

Introduction
============

Mediatum is an open source software product for image, document and video archiving and retrieval written in Python.
It was originally developed in the framework of the DFG project IntegraTUM and is continuously expanded with new functionalities as required.

It can be used as:


* Repository for images and videos:
   * Supported formats: JPG, TIFF, MP4
   * The predefined structures for metadata of image and video data can be adapted.
   * Upload of individual images or complete archives
   * Automatic extraction of image metadata such as EXIF tags
   * Display of image objects in different resolutions
   * Zoom function for images

* Document respository:
   * Supported of different PDF file types: PDF-X, PDF-A
   * Upload of PDF-files with support of fulltext search
   * Automatic extraction of PDF-file metadata
   * Predefined metadata schemas for text-based media

* Digital library for academic fulltext publications:
   * OAI interface
   * URN generation
   * Standard workflows with defined steps starting from the document upload,
     to internal processing by differently authorized users,
     quality control of the metadata and finally publication of the document

For all these use cases you will also get:

* Flexible definition of masks for selective editing and display of metadata fields
* Export to BibTeX
* A Web-API to request entries in XML or JSON format


The source code of Mediatum is hosted at https://github.com/mediatum/mediatum .
Contributions in the form of pull requests are welcome.



Concepts & features
-------------------

General concepts
^^^^^^^^^^^^^^^^

A mediatum instance comprises collections, directories and data nodes.
Metadata can be added and edited for all data items.
Role-based access control allows a fine-grained manipulation of who can see or edit data nodes.

Full-texts and metadata can be indexed by web search engines.


Editor
^^^^^^

The editor provides functionality to change the structure and metadata of collections and nodes.


Authentication and access control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Authentication via LDAP is provided.

The authorization system manages and checks the access privileges of users.


File upload
^^^^^^^^^^^

Different file formats can be uploaded and displayed:

* PDF documents
* Image files (JPEG, TIFF)
* Video files (MP4)
* Audio files (MP3)

Are we doing any kind of file format validation?

Displaying documents and media
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Images:

* Browsing thumbnails
* Viewing high-resolution versions of images
* EXIF metadata manipulation
* Zoomify viewer (flash)


Playing video and audio files.


Search features
^^^^^^^^^^^^^^^

Two different search modes are implemented: simple and extended.

Mediatum provides search on the meta data and the fulltext of submitted documents.
Text is also extracted from e.g. PDF files.
`PostgreSQL fulltext search <https://www.postgresql.org/docs/current/static/textsearch.html>`_ is used as search engine.
It is also accessible via the webservice.

Result pages can be sorted by multiple criteria.

Workflows
^^^^^^^^^

Workflows define how documents are entering Mediatum.


Versioning
^^^^^^^^^^

Data nodes are versioned to ensure that no data can get lost during editing.


REST API webservice / data export
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The webservice can be accessed at  `/services/export <https://mediatum.ub.tum.de/services/export>`_

It can serve data in JSON, XML and other formats (OAI, Z39.50).

The API is defined by the code in `/web/services <https://github.com/mediatum/mediatum/tree/postgres/web/services>`_.

Eamples:

 * with HTTPie: ``http --verify=no "https://mediatumtest.ub.tum.de:8443/services/export/node/1109402?format=json&nodetype&nodename&files"``


Data import
^^^^^^^^^^^

Metadata can be imported via multiple formats: BibTeX files, DOIs.


Usage and content statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aggregated data about the number and types of documents and accesses/downloads can be generated.


