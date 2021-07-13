class Singleton1(object):
    __instance = None
    __is_first_init = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            Singleton1.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__is_first_init:
            self.__name = name
            Singleton1.__is_first_init = True

    def get_name(self):
        return self.__name


if __name__ == '__main__':
    tony = Singleton1("Tony")
    karry = Singleton1("Karry")
    print(tony.get_name(), karry.get_name())
    print(id(tony), "\n", id(karry))
    print(tony == karry)


"""
应用场景：
1. 希望一个类只有一个且只能有一个实例
2. 项目中的一些全局管理类 (Manager) 可以用单例模式来实现
"""