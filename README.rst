.. image:: https://badge.waffle.io/pysv/pysv.org.png?label=ready&title=Ready 
 :target: https://waffle.io/pysv/pysv.org
 :alt: 'Stories in Ready'
======================================================

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/pysv/pysv.org
   :target: https://gitter.im/pysv/pysv.org?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
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


bootstrap your environment
--------------------------

commands::

    ./bootstrap.sh


Start Zope in debugmode
-----------------------

::

    bin/instance fg

Open Zope in the browser
------------------------

`localhost:13090 <http://localhost:13090/>`_ 
