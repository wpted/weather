import os
import requests


class Weather:
    def __init__(self, api_key):
        self.url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key

    def get_weather(self, city):
        url = f"{self.url}?q={city}&appid={self.api_key}&units=metric"
        try:
            result = requests.get(url=url)
            result.raise_for_status()

            return result.json()
        except requests.exceptions.RequestException as e:
            SystemExit(e)


def main():
    MY_KEY = os.environ["api_key"]
    w1 = Weather(MY_KEY)
    city_to_check = input("Enter a city name to check the weather:\n")
    print(w1.get_weather(city_to_check))


if __name__ == '__main__':
    main()
