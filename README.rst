################################################
#Readme of https://github.com/pysv/pysv_buildout
################################################

The buildout configuration of the Python Software Verband Plone 4 Website

.. contents:: Overview
    :depth: 2

============================
Installation for Development
============================


Abhängigkeiten
==============

- Python 2.7
- virtualenv >1.9
- diverse dev packages (python-dev, et al) und build-essential

Checkout & Prepare Source
=========================

Clone Repository locally
------------------------

commands::

    git clone git@github.com:pysv/pysv_buildout.git
    
Make the devel.cfg the default buildout.cfg
-------------------------------------------

commands::

    ln -s devel.cfg buildout.cfg

Dieser Symlink wird von git ignoriert. Das ist gut so.    

Create virtualenv
-----------------

commands::

    cd pysv_buildout/
    virtualenv --no-site-packages --no-setuptools --clear .
    

bootstrap your buildout
-----------------------

commands::

    ./bin/python2.7 bootstrap.py
    ./bin/buildout


Start Zope in debugmode
-----------------------

::

    bin/instance fg

Open Zope in the browser
------------------------

`localhost:13090 <http://localhost:13090/>`_ 
