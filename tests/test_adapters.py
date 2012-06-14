from twelve import adapters


class TestDjango:

    def test_databases_postgres(self):
        values = {"default": {"name": "dbname", "service": "postgres", "host": "hostname", "user": "user", "password": "pass", "port": 5432}}
        expected = {"default": {"ENGINE": "django.db.backends.postgresql_psycopg2", "HOST": "hostname", "PORT": 5432, "USER": "user", "PASSWORD": "pass", "NAME": "dbname"}}

        result = adapters.django_databases(values)

        assert result == expected

    def test_databases_postgis(self):
        values = {"default": {"name": "dbname", "service": "postgis", "host": "hostname", "user": "user", "password": "pass", "port": 5432}}
        expected = {"default": {"ENGINE": "django.contrib.gis.db.backends.postgis", "HOST": "hostname", "PORT": 5432, "USER": "user", "PASSWORD": "pass", "NAME": "dbname"}}

        result = adapters.django_databases(values)

        assert result == expected

    def test_databases_mysql(self):
        values = {"default": {"name": "dbname", "service": "mysql", "host": "hostname", "user": "user", "password": "pass", "port": 3306}}
        expected = {"default": {"ENGINE": "django.db.backends.mysql", "HOST": "hostname", "PORT": 3306, "USER": "user", "PASSWORD": "pass", "NAME": "dbname"}}

        result = adapters.django_databases(values)

        assert result == expected

    def test_databases_sqlite(self):
        values = {"default": {"name": "/var/database.db", "service": "sqlite", "host": None, "user": None, "password": None, "port": None}}
        expected = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "/var/database.db"}}

        result = adapters.django_databases(values)

        assert result == expected
