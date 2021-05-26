from abc import ABCMeta, abstractmethod


class Office:
    def __init__(self):
        self.__observes = []
        self.__username = ''

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username
        print(self.__username + ' at office')
        self.notifies()

    def add_observe(self, observe):
        self.__observes.append(observe)

    def notifies(self):
        for o in self.__observes:
            o.update(self)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, office):
        pass


class Me(Observer):
    def update(self, office):
        if office.get_username() == 'yeling':
            print('我要找的人在办公室')


if __name__ == "__main__":
    of = Office()
    me = Me()
    of.add_observe(me)
    of.set_username('Jenne')
    of.set_username('Bob')
    of.set_username('yeling')
    of.set_username('Tom')

