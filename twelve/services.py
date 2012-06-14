import urlparse

from twelve.compat import extensions

# Register database schemes in URLs.
urlparse.uses_netloc.append("postgres")
urlparse.uses_netloc.append("postgis")
urlparse.uses_netloc.append("mysql")
urlparse.uses_netloc.append("sqlite")

# Register email schemes in URLs.
urlparse.uses_netloc.append("smtp")
urlparse.uses_netloc.append("smtp+tls")


def databases(environ, names=None):
    if names is None:
        names = {"DATABASE_URL": "default"}

    databases = {}

    for k, v in names.items():
        url = environ.get(k)

        if url is not None:
            url = urlparse.urlparse(url)

            databases[v] = {
                "service": url.scheme,
                "user": url.username,
                "password": url.password,
                "host": url.hostname,
                "port": url.port,
                "name": url.path[1:],
            }

    return databases


def emails(environ, names=None):
    if names is None:
        names = {"EMAIL_URL": "default"}

    emails = {}

    for k, v in names.items():
        url = environ.get(k)

        if url is not None:
            url = urlparse.urlparse(url)

            emails[v] = {
                "service": url.scheme.split("+", 1)[0],
                "user": url.username,
                "password": url.password,
                "host": url.hostname,
                "port": url.port,
                "tls": url.scheme.split("+", 1)[-1].lower() == "tls"
            }

    return emails

if extensions is not None:
    extensions.register("twelve.services", "databases", "twelve.services:databases")
    extensions.register("twelve.services", "emails", "twelve.services:emails")
