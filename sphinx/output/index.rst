
Module Documentation
********************

**class newbinds.NewBinds(excludedBinds=())**

   Copy a dictionary, while retaining only updates.

   The intended purpose of this class is to simplify the code creating
   attribute dictionaries for class construction, but it would also
   work anywhere else a lot of bindings which include function or
   class definitions (values that aren’t expressions) are bundled into
   a dictionary.

   Example usage: the locals dictionary is passed at instantiation,
   additional bindings are made, and then the instance is called with
   the updated locals dictionary. A new dictionary is made with the
   bindings that were not present at instantiation. Bindings to the
   instance are also omitted.

   The set of excluded symbols is accessible via the “excludedBinds”
   property and may be revised.

   **__call__(dIn)**

      Returns a copy, with the excluded bindings omitted, as well as
      any references to the instance.

   **__init__(excludedBinds=())**

      Takes an iterable of symbols to exclude
