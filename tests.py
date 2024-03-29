
from newbinds import NewBinds


def test1():
    x        = 2
    y        = 3
    z        = 7

    attrs    = dict(_x=x)

    binder = NewBinds(locals())

    def __init__(self, n):
        self._foo = self._x * self._y * n

    @property
    def theAnswer(self):
        return self._foo

    attrs.update(binder(locals()))

    attrs.update(_y=y)

    Foo = type('Foo', (object,), attrs)
    foo = Foo(z)

    assert hasattr(Foo, 'x') == False
    assert hasattr(Foo, 'z') == False
    assert hasattr(Foo, 'binder') == False
    assert hasattr(Foo, 'theAnswer') == True
    assert foo.theAnswer == x*y*z


if __name__ == '__main__':
    test1()
