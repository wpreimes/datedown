========
datedown
========

Small library to download files with date and time based filenames or folder
structures. In parallel using wget.

Recursive wget can be slow and result in cumbersome local folder structures.
This library downloads exact filenames based on exact dates or a range of dates.
Remote and local filenames and paths are built using the `Python strftime and
strptime format specification
<https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>`_

The library uses the Python multiprocessing module to start multiple wget
instances for possibly faster downloading. At the end of the download process it
verfies that all the files were downloaded. No support for checksums at the
moment.

Installation
============

* Install `wget <https://en.wikipedia.org/wiki/Wget>`_ if it is not already on
  your system.
* ``pip install datedown``

Usage
=====

Coming.

Note
====

This project has been set up using PyScaffold 2.5.6. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
