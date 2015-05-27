=============================
django-newsletter2go
=============================

.. image:: https://badge.fury.io/py/django-newsletter2go.png
    :target: https://badge.fury.io/py/django-newsletter2go

.. image:: https://travis-ci.org/productgang/django-newsletter2go.png?branch=master
    :target: https://travis-ci.org/productgang/django-newsletter2go

.. image:: https://coveralls.io/repos/productgang/django-newsletter2go/badge.png?branch=master
    :target: https://coveralls.io/r/productgang/django-newsletter2go?branch=master

An email backend for Django that uses Newsletter2Go transactional emails

Documentation
-------------

The full documentation is at https://django-newsletter2go.readthedocs.org.

Quickstart
----------

Install django-newsletter2go::

    pip install django-newsletter2go

Use it in a project by adding this to your settings::

    INSTALLED_APPS += ('newsletter2go', )
    NEWSLETTER2GO_API_KEY = 'asdf'  # Your API key
    EMAIL_BACKEND='newsletter2go.backends.Newsletter2GoEmailBackend'

Then you can use it as normal with the Django mail module: https://docs.djangoproject.com/en/1.8/topics/email/

Features
--------

* TODO
