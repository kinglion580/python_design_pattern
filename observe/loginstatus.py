import time

from abc import ABCMeta, abstractmethod


class Observable:
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self, object_):
        for o in self.__observers:
            o.update(self, object_)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable, object_):
        pass


class Account(Observable):
    def __int__(self):
        self.__latestRegion = {}

    def login(self, name, ip, time_):
        region = self.__get_region(ip)
        if self.__is_long_distance(name, region):
            self.notify_observer({"name": name, "ip": ip, "region": region, "time": time_})
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
    def update(self, observable, object_):
        print("[sms sender]: " + object_["name"] + " 你的账号异常，最近一次登录信息：\n"
              + "登录ip：" + object_["ip"] + "登录地区：" + object_["region"]
              + "登录时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object_["time"])))


class MailSender(Observer):
    def update(self, observable, object_):
        print("[mail sender]: " + object_["name"] + " 你的账号异常，最近一次登录信息：\n"
              + "登录ip：" + object_["ip"] + "登录地区：" + object_["region"]
              + "登录时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object_["time"])))


def test_login():
    account = Account()
    sms = SmsSender()
    mail = MailSender()
    account.add_observer(sms)
    account.add_observer(mail)
    account.login("yl", "127.0.0.1", time.time())
    account.login("yl", "111.111.111", time.time())
