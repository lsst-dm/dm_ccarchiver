.. _Developer_Guide:

#########################################
CCArchiver Developer Guide
#########################################

.. Update these labels and links
.. image:: https://img.shields.io/badge/GitHub-dm_CCArchiver-green.svg
    :target: https://github.com/lsst-ts/dm_CCArchiver
.. image:: https://img.shields.io/badge/Jenkins-dm_CCArchiver-green.svg
    :target: https://tssw-ci.lsst.org/job/LSST_Telescope-and-Site/job/dm_CCArchiver/
.. image:: https://img.shields.io/badge/Jira-dm_CCArchiver-green.svg
    :target: https://jira.lsstcorp.org/issues/?jql=labels+%3D+dm_CCArchiver
.. image:: https://img.shields.io/badge/ts_xml-CCArchiver-green.svg
    :target: https://ts-xml.lsst.io/sal_interfaces/CCArchiver.html

[This section should provide an introduction of the system to the developer and an brief overview of the CSC architecture.
This should include links to background information where appropriate.]

.. _Dependencies:

Dependencies
============

[This section should list dependencies in bullet form]

* `SAL <https://ts-sal.lsst.io>`_ - v4.0.0
* ts_salobj - v5.2.0

.. Linking to the previous versions may also be worthwhile, depending on the CSC

.. _API:

CCArchiver API
=============================

The content in this section is autogenerated from docstrings.

.. The code below should insert the docstrings from the code.

.. automodapi:: lsst.dm.CCArchiver
    :no-main-docstr:
    :no-inheritance-diagram:


.. _Build:

Build and Test
==============

[This section is to walk a developer through the steps to build and test the software.]


.. _Usage:

Usage
=====

[Description on how to use ths software, scripts, any useful programs etc. Basic operations such as startup/shutdown should be explained, ideally with example code/steps]

.. _Simulator:

Simulator
=========

[Information regarding the simulator, including how to run, restrictions, differences from real operation etc should be described here]


.. _Firmware:

Updating Firmware of the CCArchiver
==================================================

[This section should discuss the firmware currently installed and how to update it when required. Linking to firmware location is expected, along with details on any support equipment to write to FPGAs etc]


.. _Documentation:

Building the Documentation
==========================

[This section is to walk the developer through building the documentation. This should be a step-by-step process as it will most likely be used by non-developers as well who wish to edit the docs]

.. _Contributing:

Contributing
============

Code and documentation contributions utilize pull-requests on github.
Feature requests can be made by filing a Jira ticket with the `CCArchiver` label.
In all cases, reaching out to the :ref:`contacts for this CSC <Contact_Personnel>` is recommended.

