import urlparse

import extensions

# Register database schemes in URLs.
urlparse.uses_netloc.append("postgres")
urlparse.uses_netloc.append("postgis")
urlparse.uses_netloc.append("mysql")
urlparse.uses_netloc.append("sqlite")


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


extensions.register("twelve.services", "databases", "twelve.services:databases")
