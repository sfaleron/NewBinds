
class NewBinds(object):
    """Copy a dictionary, while retaining only updates.

    The intended purpose of this class is to simplify the code
    creating attribute dictionaries for class factories, but it
    would also work anywhere else a lot of bindings which include
    function definitions are bundled into a dictionary.

    Example usage: the locals dictionary is passed at instantiation,
    additional bindings are made, and then the instance is called with
    the updated locals dictionary. A new dictionary is made with the
    bindings that were not present at instantiation. Bindings to the
    instance are also omitted.

    The set of excluded symbols is accessible via the "excludedBinds"
    property and may be revised."""

    def __init__(self, excludedBinds=()):
        """Takes an iterable of symbols to exclude"""

        self._excludedBinds = set(excludedBinds)

    def __call__(self, dIn):
        """Returns a copy, with the excluded bindings omitted,
        as well as any references to the instance."""

        dOut = {}
        for key, val in dIn.items():
            if not (key in self._excludedBinds or val is self):
               dOut[key] = val

        return dOut

    @property
    def excludedBinds(self):
        """Access the (mutable) set of excluded symbols."""
        return self._excludedBinds

if __name__ == '__main__':
    x     = 14
    y     = 3

    # or globals(), they're the same at module-level
    newBinds = NewBinds(locals())

    def __init__(self, n):
        self._foo = self._x * n

    @property
    def theAnswer(self):
        return self._foo

    attrs = newBinds(locals())

    attrs.update(_x=x)

    Foo = type('Foo', (object,), attrs)
    foo = Foo(y)

    assert hasattr(Foo, 'x') == False
    assert hasattr(Foo, 'newBinds') == False
    assert hasattr(Foo, 'theAnswer') == True
    assert foo.theAnswer == x*y
