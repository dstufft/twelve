import extensions


def django_databases(values):
    databases = {}

    for name, config in values.items():
        database = {}

        for k, v in config.items():
            if k == "service":
                if v == "postgres":
                    database["ENGINE"] = "django.db.backends.postgresql_psycopg2"
                elif v == "postgis":
                    database["ENGINE"] = "django.contrib.gis.db.backends.postgis"
                elif v == "mysql":
                    database["ENGINE"] = "django.db.backends.mysql"
                elif v == "sqlite":
                    database["ENGINE"] = "django.db.backends.sqlite3"
            else:
                database[k.upper()] = v

        databases[name] = database

    return databases


extensions.register("twelve.adapters", "django.databases", "twelve.adapters:django_databases")
