from twelve import services


class TestDatabases:

    def test_databases(self):
        environ = {"DATABASE_URL": "postgres://user:pass@hostname:5432/dbname"}
        expected = {"default": {"name": "dbname", "service": "postgres", "host": "hostname", "user": "user", "password": "pass", "port": 5432}}

        result = services.databases(environ)

        assert result == expected

    def test_nonstandard_name_for_default(self):
        environ = {"WIERD_DATABASE_URL": "postgres://user:pass@hostname:5432/dbname"}
        expected = {"default": {"name": "dbname", "service": "postgres", "host": "hostname", "user": "user", "password": "pass", "port": 5432}}

        result = services.databases(environ, names={"WIERD_DATABASE_URL": "default"})

        assert result == expected

    def test_standard_name_nonstandard_target(self):
        environ = {"DATABASE_URL": "postgres://user:pass@hostname:5432/dbname"}
        expected = {"mydb": {"name": "dbname", "service": "postgres", "host": "hostname", "user": "user", "password": "pass", "port": 5432}}

        result = services.databases(environ, names={"DATABASE_URL": "mydb"})

        assert result == expected

    def test_nonstandard_name_nonstandard_target(self):
        environ = {"WIERD_DATABASE_URL": "postgres://user:pass@hostname:5432/dbname"}
        expected = {"mydb": {"name": "dbname", "service": "postgres", "host": "hostname", "user": "user", "password": "pass", "port": 5432}}

        result = services.databases(environ, names={"WIERD_DATABASE_URL": "mydb"})

        assert result == expected

    def test_databases_multiple(self):
        environ = {
                    "DATABASE_URL": "postgres://user:pass@hostname:5432/dbname",
                    "SECONDARY_DATABASE_URL": "postgres://user:pass@hostname:5432/dbname2",
                }
        expected = {
                    "default": {"name": "dbname", "service": "postgres", "host": "hostname", "user": "user", "password": "pass", "port": 5432},
                    "secondary": {"name": "dbname2", "service": "postgres", "host": "hostname", "user": "user", "password": "pass", "port": 5432},
                }

        result = services.databases(environ, names={"DATABASE_URL": "default", "SECONDARY_DATABASE_URL": "secondary"})

        assert result == expected

    def test_databases_postgres(self):
        environ = {"DATABASE_URL": "postgres://user:pass@hostname:5432/dbname"}
        expected = {"default": {"name": "dbname", "service": "postgres", "host": "hostname", "user": "user", "password": "pass", "port": 5432}}

        result = services.databases(environ)

        assert result == expected

    def test_databases_postgis(self):
        environ = {"DATABASE_URL": "postgis://user:pass@hostname:5432/dbname"}
        expected = {"default": {"name": "dbname", "service": "postgis", "host": "hostname", "user": "user", "password": "pass", "port": 5432}}

        result = services.databases(environ)

        assert result == expected

    def test_databases_mysql(self):
        environ = {"DATABASE_URL": "mysql://user:pass@hostname:3306/dbname"}
        expected = {"default": {"name": "dbname", "service": "mysql", "host": "hostname", "user": "user", "password": "pass", "port": 3306}}

        result = services.databases(environ)

        assert result == expected

    def test_databases_sqlite(self):
        environ = {"DATABASE_URL": "sqlite:////var/database.db"}
        expected = {"default": {"name": "/var/database.db", "service": "sqlite", "host": None, "user": None, "password": None, "port": None}}

        result = services.databases(environ)

        assert result == expected
