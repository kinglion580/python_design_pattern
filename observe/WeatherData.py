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
    temp = 0
    humidity = 0
    pressure = 0.0

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

        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    temp = ''
    humidity = ''

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity

        self.display()

    def display(self):
        print("Current conditions: " + str(self.temp) + "F degrees and " + str(self.humidity) + "% Humidity")


class StatisticsDisplay(Observer, DisplayElement):
    max_temp = 0.0
    min_temp = 200
    temp_sum = 0.0
    num_readings = 0
    humidity = ''

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self.temp_sum += temp
        self.num_readings += 1

        if temp > self.max_temp:
            self.max_temp = temp

        if temp < self.min_temp:
            self.min_temp = temp

        self.display()

    def display(self):
        print("Avg/Max/Min temperature = " + str(self.temp_sum / self.num_readings) + "/"
              + str(self.max_temp) + "/" + str(self.min_temp))


class ForecastDisplay(Observer, DisplayElement):
    current_pressure = 29.92
    last_pressure = 0.0

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure

        self.display()

    def display(self):
        print("Forecast ")
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same")
        elif self.current_pressure < self.last_pressure:
            print("Watch out for cooler, rainy weather")


class WeatherStation:
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)

