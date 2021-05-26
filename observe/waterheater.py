from abc import ABCMeta, abstractmethod


class Observable:
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self):
        for o in self.__observers:
            o.update(self)


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        self.notify_observer()


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable):
        pass


class DrinkMode(Observer):
    def update(self, observable):
        if isinstance(observable, WaterHeater) and observable.get_temperature() >= 100:
            print('you can drink')


class WashingMode(Observer):
    def update(self, observable):
        temperature = observable.get_temperature()
        if isinstance(observable, WaterHeater) and 50 <= temperature < 70:
            print('you can wash')


if __name__ == "__main__":
    wh = WaterHeater()
    dm = DrinkMode()
    wm = WashingMode()
    wh.add_observer(dm)
    wh.add_observer(wm)
    wh.set_temperature(60)
    wh.set_temperature(100)
