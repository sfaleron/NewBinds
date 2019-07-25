
Copy a dictionary, while retaining only updates.

The intended purpose of this class is to simplify the code creating attribute dictionaries for class construction, but it would work anywhere a lot of function or class definitions (values that aren’t expressions) end up in a dictionary (or other container, via post-processing); for instance, a container to allow parameterized selection among several functions or classes.

See |tests|_ for example usage.

.. |tests| replace:: ``tests.py``
.. _tests: https://github.com/sfaleron/NewBinds/blob/master/test.py
