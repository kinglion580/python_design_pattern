def singletonDecorator(cls, *args, **kargs):
    instance = {}

    def wrapper_singleton(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]

    return wrapper_singleton


@singletonDecorator
class Singleton3:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == '__main__':
    tony = Singleton3("Tony")
    karry = Singleton3("Karry")
    print(tony.get_name(), karry.get_name())
    print(id(tony), "\n", id(karry))
    print(tony == karry)
