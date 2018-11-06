class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Foo(object):
    __metaclass__ = Singleton


foo1 = Foo()
foo2 = Foo()
print foo1 is foo2



import functools


def singleton(cls):
    _instance = {}

    @functools.wraps(cls)
    def s(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return s
    

@singleton
class Bar():
    pass


b1 = Bar()
b2 = Bar()
print b1 is b2