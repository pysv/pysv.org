################################################
#Readme of https://github.com/pysv/pysv_buildout
################################################

The buildout configuration of the Python Software Verband Plone 4 Website

=================================
Installation for Development
=================================

Overview
===========

The current pysv_buildout tree
----------------------------------
pysv_buildout:

    ├── README.md
    ├── README.txt
    ├── base.cfg
    ├── bootstrap.py
    ├── deploy.cfg
    ├── devel.cfg
    ├── src
    │   └── README.txt
    ├── var
    │   └── README.txt
    └── versions.cfg


Prerequisites
===================

- Python 2.7
- virtualenv
- libxslt-dev

Checkout & Prepare Source
=============================

Clone Repository locally
----------------------------

commands::

    git clone git@github.com:pysv/pysv_buildout.git
    
Create virtualenv
----------------------

commands::

    cd pysv_buildout/
    virtualenv virt_env
    source virt_env/bin/activate


Make the devel.cfg the default buildout.cfg
----------------------------------------------

**Do this locally only!** Never check in this symbolic link into the repository!

commands::

    ln -s devel.cfg buildout.cfg

bootstrap your buildout
--------------------------

commands::

    python bootstrap.py
    ./bin/develop co pysv.policy
    ./bin/buildout


Start Zope in debugmode
------------------------------

    bin/instance fg

[http://localhost:13090/](http://localhost:13090/)

