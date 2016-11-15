Sample Klein App
================

|travis|

A sample application in Python, using the Klein_ web framework.

Klein is a lightweight web framework, similar to Flask_ or Bottle_.
The primary differentiator for Klein is that it is built on the Twisted_
framework, which enables one to write *asynchronous* applications.

This sample application attempts to demonstrate a few things:

  * Basic usage of Klein.
    See hello.py_.
  * Using URL path components as arguments.
    See math.py_.
  * Composition of Klein applications.
    See composite.py_.
  * Using Twisted to write asynchronous code, with the `@inlineCallbacks`
    decorator.
    See dns.py_.

.. ------------------------------------------------------------------------- ..

.. _composite.py: src/sample_klein_app/application/composite.py
.. _dns.py: src/sample_klein_app/application/dns.py
.. _hello.py: src/sample_klein_app/application/hello.py
.. _math.py: src/sample_klein_app/application/math.py

.. _Bottle: http://bottlepy.org/
.. _Flask: http://flask.pocoo.org/
.. _Klein: https://github.com/twisted/klein/
.. _Twisted: http://twistedmatrix.com/

.. |travis| image:: https://api.travis-ci.org/wsanchez/sample-klein-app.svg?branch=master
