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


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable):
        pass


class Account(Observable):
    def __int__(self):
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__get_region(ip)
        if self.__is_long_distance(name, region):
            pass
        self.__latestRegion[name] = region

    def __get_region(self, ip):
        ip_regions = {
            "127.0.0.1": "local",
            "100.100.100.100": "sichuan",
        }
        region = ip_regions.get(ip)
        return "" if region is None else region

    def __is_long_distance(self, name, region):
        latest_region = self.__latestRegion.get(name)
        return latest_region is not None and latest_region != region


class SmsSender(Observer):
    def update(self, observable):
        pass


class MailSender(Observer):
    def update(self, observable):
        pass