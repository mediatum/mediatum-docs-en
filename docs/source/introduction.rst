.. _intro:

Introduction
============

mediaTUM is an open source software product for image, document and video archiving and retrieval written in Python.

It can be used as:

* Repository for images and videos:
   * Supported formats: JPG, TIFF, MP4
   * The predefined structures for metadata of image and video data can be adapted.
   * Upload of individual images or complete archives
   * Automatic extraction of image metadata such as EXIF tags
   * Display of image objects in different resolutions
   * Zoom function for images

* Document respository:
   * Support for different PDF file types: PDF-X, PDF-A
   * Upload of PDF documents and fulltext search in their content
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


The source code of mediaTUM is hosted at `github.com/mediatum <https://github.com/mediatum>`_.
Contributions in the form of pull requests are welcome.
