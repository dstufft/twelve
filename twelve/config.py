import os

from twelve.compat import extensions


class Configuration(object):

    def __init__(self, adapter=None, environ=None, names=None, *args, **kwargs):
        super(Configuration, self).__init__(*args, **kwargs)

        if names is None:
            names = {}

        self.adapter = adapter.lower()
        self.environ = environ
        self.names = names
        self.values = {}

    def __getattr__(self, name):
        if not name in self.values:
            names = [plugin.name for plugin in extensions.get(group="twelve.services")]
            environ = self.environ if self.environ is not None else os.environ

            if name in names:
                # We are trying to get a Backing Service, Load it
                self.values[name] = self._load_service(name, environ=environ)
            elif name.upper() in environ:
                self.values[name] = self._get_environ_value(name, environ=environ)
            else:
                self.values[name] = None

        return self.values[name]

    def __repr__(self):
        return "<twelve.Configuration [{0}]>".format(",".join(self.values))

    def _get_environ_value(self, name, environ):
        value = environ.get(name.upper())

        if self.adapter is not None:
            adapters = list(extensions.get(group="twelve.adapters", name="{0}.{1}".format(self.adapter, name)))
            if len(adapters):
                adapter = adapters[0].load()
                value = adapter(value)

        return value

    def _load_service(self, name, environ):
        for plugin in extensions.get(group="twelve.services", name=name):
            service = plugin.load()

            value = service(environ, self.names.get(plugin.name))

            if self.adapter is not None:
                adapters = list(extensions.get(group="twelve.adapters", name="{0}.{1}".format(self.adapter, plugin.name)))
                if len(adapters):
                    adapter = adapters[0].load()
                    value = adapter(value)

            return value
