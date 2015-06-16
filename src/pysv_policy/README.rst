##############################################
#Readme of https://github.com/pysv/pysv_policy
##############################################

The buildout configuration of the Python Software Verband Plone 4 Website

.. contents:: Overview
    :depth: 2

=======================================================================
policy package to rule the configuration of the Python Software Verband
=======================================================================



pysv_policy
===========

The policy package to rule the configuration of the Python Software Verband Plone 4 Website

Buildout
--------

::
    ln -s develop.cfg buildout.cfg
    ./bin/bootstrap.sh

Tests
-----
:

   ./bin/test --all


Internationalization
--------------------



Update pysv.policy in Plone Instance
------------------------------------

http://localhost:13090/Plone/manage/

go to: portal_setup -> Import

select pysv.policy

Click on: Import all steps


