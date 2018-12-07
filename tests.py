
from __future__ import absolute_import

from newbinds import NewBinds


def test1():
    x     = 14
    y     = 3

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


if __name__ == '__main__':
    test1()

