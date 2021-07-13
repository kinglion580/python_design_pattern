class Singleton2(type):
    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class CustomClass(metaclass=Singleton2):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == '__main__':
    tony = CustomClass("Tony")
    karry = CustomClass("Karry")
    print(tony.get_name(), karry.get_name())
    print(id(tony), "\n", id(karry))
    print(tony == karry)
