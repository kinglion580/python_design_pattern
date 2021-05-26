from abc import ABCMeta, abstractmethod


class WaterHeater:
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        self.notifies()

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, waterheater):
        pass


class DrinkMode(Observer):
    def update(self, waterheater):
        if waterheater.get_temperature() >= 100:
            print('you can drink')


class WashingMode(Observer):
    def update(self, waterheater):
        temperature = waterheater.get_temperature()
        if 50 <= temperature < 70:
            print('you can wash')


if __name__ == "__main__":
    wh = WaterHeater()
    dm = DrinkMode()
    wh.add_observer(dm)
    wh.set_temperature(60)
    wh.set_temperature(100)
