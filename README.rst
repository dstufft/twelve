Twelve
======

Twelve is a utility for using 12factor_ inspired settings in Python. It provides
an ``Environment`` class which abstracts away pulling settings out of the environment
and normalizing them and small shims/adapters to make it easy to use those values
in various popular frameworks.

.. _12factor: http://www.12factor.net/


Basic Usage
-----------

::

    # Setup Environment (Normally Done Externally to Configuration)
    import os
    os.environ["DATABASE_URL"] = "postgres://user:pass@hostname:5432/dbname"

    # Load Twelve Environment
    import twelve
    env = twelve.Environment()

    # Use Values
    import psycopg2
    conn = psycopg2.connect(
                        host=env.databases["default"]["host"],
                        port=env.databases["default"]["port"],
                        user=env.databases["default"]["user"],
                        password=env.databases["default"]["password"],
                        database=env.databases["default"]["name"],
                    )

    # Make Queries


Basic Usage w/ Django Adapter
-----------------------------

::

    # Setup Environment (Normally Done Externally to Configuration)
    import os
    os.environ["DATABASE_URL"] = "postgres://user:pass@hostname:5432/dbname"

    # Load Twelve Environment
    import twelve
    env = twelve.Environment(adapter="django")

    DATABASES = env.databases

