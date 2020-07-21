..
  This is a template for documentation that will accompany each CSC.
  It consists of a user guide and development guide, however, cross linking between the guides is expected.
  This template is provided to ensure that the documentation remains similar in look, feel, and contents to users.
  The headings below are expected to be present for all CSCs, but for many CSCs, additional fields will be required.
  An example case can be found at https://ts-athexapod.lsst.io/v/develop/

  ** All text in square brackets [] must be re-populated accordingly **

  See https://developer.lsst.io/restructuredtext/style.html
  for a guide to reStructuredText writing.

  Use the following syntax for sections:

  Sections
  ========

  and

  Subsections
  -----------

  and

  Subsubsections
  ^^^^^^^^^^^^^^

  To add images, add the image file (png, svg or jpeg preferred) to the
  images/ directory. The reST syntax for adding the image is

  .. figure:: /images/filename.ext
   :name: fig-label

  Caption text.

  Feel free to delete this instructional comment.

.. Fill out data so contacts section below is auto-populated
.. add name and email between the *'s below e.g. *Marie Smith <msmith@lsst.org>*
.. |CSC_developer| replace::  *Stephen R Pietrowicz <srp@illinois.edu>*
.. |CSC_product_owner| replace:: *Michael Reuter <mareuter@lsst.org>*

.. Note that the "ts_" prefix is omitted from the title

#########################
CCArchiver
#########################

.. update the following links to point to your CSC (rather than the athexapod)
.. image:: https://img.shields.io/badge/GitHub-dm_CCArchiver-green.svg
    :target: https://github.com/lsst-dm/dm_CCArchiver
.. image:: https://img.shields.io/badge/Jenkins-dm_CCArchiver-green.svg
    :target: https://tssw-ci.lsst.org/job/LSST_Telescope-and-Site/job/dm_CCArchiver/
.. image:: https://img.shields.io/badge/Jira-dm_CCArchiver-green.svg
    :target: https://jira.lsstcorp.org/issues/?jql=labels+%3D+dm_CCArchiver
.. image:: https://img.shields.io/badge/ts_xml-dm_CCArchiver-green.svg
    :target: https://ts-xml.lsst.io/sal_interfaces/CCArchiver.html

.. TODO: Delete the note when the page becomes populated

.. Warning::

   **This CSC documentation is under development and not ready for active use.**

.. _Overview:

Overview
========

[This section is to present an overview of the CSC.
This should include a top-level description of the primary use-case(s) as well as any pertinent information.
Example information may be link(s) to the higher-level classes which may be used to operate it, or mention of other CSCs (with links) that it operates in concert with.]

The Data Management ComCam Archiver (dm_CCArchiver) coordinates archiving
activities for the Commissioning Camera.  This service interacts with other
services coordinate retrieval and archival of image data from the data
acquisition system.

The primary services that the CCArchiver interacts with are the Forwarder 
(dm_Forwarder) and the ComCam Controller.  The Forwarder retrieves and assembles
images. The ComCam Controller presents where files should be deposited and 
stages files where the Data Backbone (DBB) and the ComCam Observatory 
Operations Data Service (OODS) can act on them.  These services communicate
to each other using RabbitMQ.  A Redis database is also used to advertise
service availablity and service health.


The archiver begins in the STANDBY state. When it receives a START command,
it transitions to the DISABLED state.  This causes the CCArchiver to attempt
to pair with an available Forwarder service through a Redis database. It also
establishes connections to a RabbitMQ server. After the archiver receives an 
ENABLE SAL command, it is ready to receive messages.

When the "startIntegration" message is received, the CCArchiver sends a 
message to the ComCam Controller, informing it that a new archive image will
arrive soon.  In the controller’s response is the target directory for where
the image is supposed to be deposited by the forwarder. This target directory
changes over time. The target directory is then sent in a message to the 
Forwarder, which sends back an acknowledgment that the message was received.

When the "endReadout" message is received, the CCArchiver sends the message to
the Forwarder, which sends back an acknowledgment that the message was
received.


When the "largeFileObjectAvailable" is received indicating that the header is
available from the HeaderService, the CCArchiver sends the message to the
Forwarder, which sends back an acknowledgment that the message was received.

When the telemetry message "IMAGE_RETRIEVAL_FOR_ARCHIVING" message is received
via RabbitMQ from the ComCam Controller, the CCArchiver translates this into the
"imageRetrievalForArchiving" message and transmits it via SAL.  

Note that "IMAGE_RETRIEVAL_FOR_ARCHIVING" indicates that the Forwarder has
contacted the ComCam Controller and told it that it has finished writing 
the file.  The ComCam Controller links data to the staging area of the DBB
and the ComCam OODS. Additionally, the Controller sends a message to the 
ComCam OODS that it can ingest the file that was written.  The ComCam OODS
ingests the images into the Butler repository and issues a RabbitMQ 
message to the ComCam Archiver about the status of the file ingestion.  

When the message "CC_FILE_INGEST_REQUEST" is received from the ComCam OODS,
the ComCam Archiver translates that messages and transmits the status of the 
Butler file ingestion via SAL as a CCArchiver event.

.. note:: If you are interested in viewing other branches of this repository append a `/v` to the end of the url link. For example `https://ts-xml.lsst.io/v/`


.. _User_Documentation:

User Documentation
==================

.. This template has the user documentation in a subfolder.
.. However, in cases where the user documentation is extremely short (<50 lines), one may move that content here and remove the subfolder.
.. This will require modification of the heading styles and possibly renaming of the labels.
.. If the content becomes too large, then it must be moved back to a subfolder and reformatted appropriately.

User-level documentation, found at the link below, is aimed at personnel looking to perform the standard use-cases/operations with the CCArchiver.

.. toctree::
    user-guide/user-guide
    :maxdepth: 2

.. _Configuration:

Configuring the CCArchiver
=========================================
.. For CSCs where configuration is not required, this section can contain a single sentence stating so.
   More introductory information can also be added here (e.g. CSC XYZ requires both a configuration file containing parameters as well as several look-up tables to be operational).

The configuration for the CCArchiver is described at the following link.

.. toctree::
    configuration/configuration
    :maxdepth: 1


.. _Development_Documentation:

Development Documentation
=========================

.. This template has the user documentation in a subfolder.
.. However, in cases where the user documentation is extremely short (<50 lines), one may move that content here and remove the subfolder.
.. This will require modification of the heading styles and possibly renaming of the labels.
.. If the content becomes too large, then it must be moved back to a subfolder and reformatted appropriately.

This area of documentation focuses on the classes used, API's, and how to participate to the development of the CCArchiver software packages.

.. toctree::
    developer-guide/developer-guide
    :maxdepth: 1

.. _Version_History:

Version History
===============

.. At the time of writing the Version history/release notes are not yet standardized amongst CSCs.
.. Until then, it is not expected that both a version history and a release_notes be maintained.
.. It is expected that each CSC link to whatever method of tracking is being used for that CSC until standardization occurs.
.. No new work should be required in order to complete this section.

The version history of the CCArchiver is found at the following link.

.. toctree::
    version-history
    :maxdepth: 1


.. _Contact_Personnel:

Contact Personnel
=================

For questions not covered in the documentation, emails should be addressed to |CSC_developer| and |CSC_product_owner|.

This page was last modified |today|.

