import requests


class Location:
    def __init__(self):
        self.city = Location.get_location()["city"]
        self.ip = Location.get_location()["ip"]

    @classmethod
    def get_location(cls):
        """
        Get the location from the IP provided.
        :return:
        """
        #  Website for real-time IP to geolocation API look-up
        ip_info_url = "http://ipinfo.io/json"
        try:
            response = requests.get(url=ip_info_url)
            response.raise_for_status()
            return response.json()


        except requests.exceptions.RequestException as e:
            SystemExit(e)


def main():
    l1 = Location()
    print(l1.city)


if __name__ == '__main__':
    main()
