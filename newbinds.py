
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
