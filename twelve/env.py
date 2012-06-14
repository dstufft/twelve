import os

import extensions


class Environment(object):

    def __init__(self, adapter=None, environ=None, names=None, *args, **kwargs):
        super(Environment, self).__init__(*args, **kwargs)

        if names is None:
            names = {}

        self.adapter = adapter
        self.environ = environ
        self.names = names
        self.values = {}

        self._load_all()

    def __getattr__(self, name):
        return self.values.get(name)

    def _load_all(self):
        # Load Services
        self._load_services()

    def _load_services(self):
        for plugin in extensions.get(group="twelve.services"):
            service = plugin.load()

            value = service(
                        self.environ if self.environ is not None else os.environ,
                        self.names.get(plugin.name)
                    )

            if self.adapter is not None:
                adapters = list(extensions.get(group="twelve.adapters", name="{0}.{1}".format(self.adapter, plugin.name)))
                if len(adapters):
                    adapter = adapters[0].load()
                    value = adapter(value)

            self.values[plugin.name] = value
