.. image:: https://badge.waffle.io/pysv/pysv.org.png?label=ready&title=Ready 
 :target: https://waffle.io/pysv/pysv.org
 :alt: 'Stories in Ready'
======================================================
Buildout und Plone Policy der http://python-verband.de
======================================================

Die Buildout-Konfiguration von der Python Software Verband Plone 4 Website

.. contents:: Overview
    :depth: 2

Installation zum Development
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

Kommandos::

    git clone git@github.com:pysv/pysv_buildout.git
    
Make the devel.cfg the default buildout.cfg
-------------------------------------------

Kommandos::

    cd pysv_buildout
    ln -s devel.cfg buildout.cfg

Dieser Symlink wird von git ignoriert. Das ist gut so.    

Virtualenv erstellen
--------------------

Kommandos::

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
