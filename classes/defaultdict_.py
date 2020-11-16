import collections


class defaultdict_(collections.UserDict):
    def __init__(self, default_factory=None, *args, **kwargs):
        if not callable(default_factory) and default_factory is not None:
            raise TypeError('first argument must be callable or None')

        super().__init__(*args, **kwargs)
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)

        self[key] = self.default_factory()
        return self[key]

    def __repr__(self):
        return (f'{type(self).__name__}({self.default_factory!r}, '
                f'{self.data!r})')
