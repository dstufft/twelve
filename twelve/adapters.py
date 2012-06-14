from twelve.compat import extensions


def django_debug(value):
    return value.lower() in ["true", "t", "yes", "on", "y"]


def django_databases(values):
    databases = {}

    for name, config in values.items():
        database = {}

        for k, v in config.items():
            if v is None:
                continue

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


def django_emails(values):
    emails = {}

    for name, config in values.items():
        email = {}

        for k, v in config.items():
            if v is None:
                continue

            if k == "service":
                if v == "smtp":
                    email["BACKEND"] = "django.core.mail.backends.smtp.EmailBackend"
            elif k == "tls":
                email["USE_TLS"] = v
            else:
                email[k.upper()] = v

        emails[name] = email

    return emails


if extensions is not None:
    extensions.register("twelve.adapters", "django.debug", "twelve.adapters:django_debug")
    extensions.register("twelve.adapters", "django.databases", "twelve.adapters:django_databases")
    extensions.register("twelve.adapters", "django.emails", "twelve.adapters:django_emails")
