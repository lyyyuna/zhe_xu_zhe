def Singleton(cls):
    _instance = [None]

    def get_instance(*args, **kwargs):
        if _instance[0] == None:
            _instance[0] = cls(*args, **kwargs)
        return _instance[0]
    return get_instance


@Singleton
class Myclass():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(self.x, self.y, self.z)


if __name__ == '__main__':
    m1 = Myclass(1, 2, 3)
    m1.display()
    m2 = Myclass(22, 33, 44)
    m2.display()
