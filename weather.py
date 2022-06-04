import os
import datetime as dt
import requests


class Weather:
    def __init__(self, api_key):
        self.url = "https://api.openweathermap.org/data/3.0/onecall?"
        self.time = dt.datetime.now()
        self.api_key = api_key
        self.city = None
        self.lat = 25.06
        self.lon = 125.56

    def weather(self):
        parameter = {
            "appid": self.api_key,
            "lat": self.lat,
            "lon": self.lon
        }

        result = requests.get(url=self.url, params=parameter)
        result.raise_for_status()

        return result.json()


def main():
    MY_KEY = os.environ["api_key"]
    w1 = Weather(MY_KEY)
    print(w1.weather())


if __name__ == '__main__':
    main()
