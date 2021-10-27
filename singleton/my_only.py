class MyBeautifulGril:
    __instance = None
    __is_first_init = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            MyBeautifulGril.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__is_first_init:
            self.__name = name
            print(name + " I love")
            MyBeautifulGril.__is_first_init = True
        else:
            print(name + " i'm not care")

    def show_my_heart(self):
        print(self.__name + " is my only girl")


if __name__ == '__main__':
    jenny = MyBeautifulGril("Jenny")
    jenny.show_my_heart()
    kimi = MyBeautifulGril("Kimi")
    kimi.show_my_heart()
    print(id(jenny))
    print(id(kimi))
