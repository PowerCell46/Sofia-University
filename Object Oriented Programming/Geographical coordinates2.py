import math


class GeoPoint:
    def __init__(self, latitude: float, longitude: float, name: str, lat_sn='N', long_WE='E'):
        self._latitude = None
        self.latitude = latitude
        self.lat_sn = lat_sn
        self._longitude = None
        self.longitude = longitude
        self.long_WE = long_WE
        self.name = name

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if -90 <= value <= 90:
            self._latitude = value
        else:
            if value < -90:
                self._latitude = - 90
            else:
                self._latitude = 90

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if 0 <= value <= 360:
            self._longitude = value
        else:
            if value < 0:
                self._longitude = 0
            else:
                self._longitude = 360

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
        return [self.name, self.latitude, self.lat_sn, self.longitude, self.long_WE]

    def __repr__(self):
        self.lat_conv()
        self.long_conv()
        return f'Geo Point name: {self.name}.\nLatitude: {self.latitude} {self.lat_sn}.\nLongitude: {self.longitude} {self.long_WE}.'


class Address:
    def __init__(self, geo_coord: GeoPoint, name: str):
        if not isinstance(geo_coord, GeoPoint):
            geo_coord = GeoPoint(0, 0, 'Default Point')

        self.geo_coord = geo_coord
        self.name = name

    def __repr__(self):
        return f'Address Name: {self.name}.\n{self.geo_coord}'

    def info(self) -> str:
        return self.__repr__()


burgasPoint = GeoPoint(42.510578, 27.461014, 'Burgas Point')
# print(burgasPoint)

Burgas = Address(burgasPoint, 'Burgas')
# print(Burgas.info())


rusePoint = GeoPoint(43.835571, 25.965654, 'Ruse Point')
# print(rusePoint)

Ruse = Address(rusePoint, 'Ruse')
# print(Ruse.info())
