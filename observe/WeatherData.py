class Subject:
    def register_observer(self, o):
        pass

    def remove_observer(self, o):
        pass

    def notify_observers(self):
        pass


class Observer:
    def update(self, temp, humidity, pressure):
        pass


class DisplayElement:
    def display(self):
        pass


class WeatherData(Subject):
    observers = []
    temp = ''
    humidity = ''
    pressure = ''

    def register_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            o.update(self.temp, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure


class CurrentConditionsDisplay(Observer, DisplayElement):
    temp = ''
    humidity = ''

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + self.temp + "F degrees and " + self.humidity + "% Humidity")


class StatisticsDisplay(Observer, DisplayElement):
    temp = ''
    humidity = ''

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print("Statistics: " + self.temp + "F degrees and " + self.humidity + "% Humidity")


class ForecastDisplay(Observer, DisplayElement):
    temp = ''
    humidity = ''

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + self.temp + "F degrees and " + self.humidity + "% Humidity")

