import math


class BasePointClass:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.lat_sn = 'N'
        self.longitude = longitude
        self.long_WE = 'E'
        
    def lat_conv(self):
        if self.latitude < 0:
            self.latitude = math.fabs(self.latitude)
            self.lat_sn = 'S'

    def long_conv(self):
        if self.longitude > 180:
            self.longitude = 360 - self.longitude
            self.long_WE = 'W'

    def get_address(self):
        self.lat_conv()
        self.long_conv()
        return [self.latitude, self.lat_sn, self.longitude, self.long_WE]

    def info(self):
        self.lat_conv()
        self.long_conv()
        return {"latitude": self.latitude, "lat_sn": self.lat_sn, "longitude": self.longitude, "long_WE": self.long_WE}


class Address(BasePointClass):
    def __init__(self, latitude: float, longitude: float, name: str):
        super().__init__(latitude, longitude)
        self.name = name

    def get_address(self):
        self.lat_conv()
        self.long_conv()
        return [self.latitude, self.lat_sn, self.longitude, self.long_WE, self.name]


address1 = Address(42.698334, 23.319941, 'Sofia')
address2 = Address(43.204666, 27.910543, 'Varna')


class GeoPoint(BasePointClass):
    def __init__(self, latitude: float, longitude: float):
        super().__init__(latitude, longitude)


geoPoint1 = GeoPoint(42.698334, 23.319941)
geoPoint2 = GeoPoint(43.204666, 27.910543)


class AddressHomeWorkTask:
    def __init__(self, address: GeoPoint, name: str):
        self.address = address
        self.name = name

    def info(self):
        return f'{self.name} {self.address.info()}'
