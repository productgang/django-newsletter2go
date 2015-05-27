========
Usage
========

To use django-newsletter2go in a project, add to your settings::

    INSTALLED_APPS += ('newsletter2go', )
    NEWSLETTER2GO_API_KEY = 'asdf'  # Your API key
    EMAIL_BACKEND='newsletter2go.backends.Newsletter2GoEmailBackend'
