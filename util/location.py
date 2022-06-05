import requests


class Location:
    def __init__(self):
        """
        __ip_info is private and can only access here.
        """
        __ip_info = Location.__get_location()
        self.region = __ip_info["region"]
        self.city = __ip_info["city"]
        self.ip = __ip_info["ip"]

    def __repr__(self):
        return f"Location:{self.__dict__}"

    def __getitem__(self, item):
        return self.__dict__[item]

    @classmethod
    def __get_location(cls) -> dict:
        """
        Get the location from the IP provided.
        :return: dict
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
    print(l1)
    print(l1.__dict__)
    print(type(vars(l1)))
    print(vars(Location()))



if __name__ == '__main__':
    main()
