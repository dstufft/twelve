Twelve
======

Twelve is a utility for using 12factor_ inspired settings in Python. It provides
a ``Configuration`` class which abstracts away pulling settings out of the environment
and normalizing them and small adapters to make it easy to use those values
in various popular frameworks.

There have been a few projects doing similar things, such as `dj-database-url`_,
`dj-cache-url`_, and `django-heroku-memcacheify`_. Each one of them handling the
backing service configuration for a single archetype of service (database, cache, etc)
and tied to a specific framework (and in one case, to a specific framework on a
specific hosting platform).

Twelve attempts to provide a uniform and simple API to using 12factor_ inspired
configuration without being tied to a specific archetype of backing service, nor
to a single framework or hosting provider.

.. _12factor: http://www.12factor.net/
.. _dj-database-url: https://crate.io/packages/dj-database-url/
.. _dj-cache-url: https://github.com/ghickman/django-cache-url
.. _django-heroku-memcacheify: https://crate.io/packages/django-heroku-memcacheify/

Basic Usage
-----------

::

    # Setup Environment (Normally Done Externally to Configuration)
    import os
    os.environ["DATABASE_URL"] = "postgres://user:pass@hostname:5432/dbname"

    # Load Twelve Configuration
    import twelve
    config = twelve.Configuration()

    # Use Values
    import psycopg2
    conn = psycopg2.connect(
                        host=config.databases["default"]["host"],
                        port=config.databases["default"]["port"],
                        user=config.databases["default"]["user"],
                        password=config.databases["default"]["password"],
                        database=config.databases["default"]["name"],
                    )


Basic Usage w/ Django Adapter
-----------------------------

::

    # Setup Environment (Normally Done Externally to Configuration)
    import os
    os.environ["DATABASE_URL"] = "postgres://user:pass@hostname:5432/dbname"

    # Load Twelve Environment
    import twelve
    config = twelve.Configuration(adapter="django")

    DATABASES = config.databases
