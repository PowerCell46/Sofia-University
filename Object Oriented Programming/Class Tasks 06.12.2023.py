
class Storage:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str) -> None:
        if self.capacity > 0:
            self.capacity -= 1
            self.storage.append(product)
            print('Product added to the Storage!')
        else:
            print('There is not enough Capacity!')

    def get_products(self) -> str:
        return 'Products in the Storage are: ' + ', '.join(self.storage)


storage = Storage(4)
# storage.add_product('apple')
# storage.add_product('banana')
# storage.add_product('potato')
# storage.add_product('tomato')
# storage.add_product('bread')
#
# print(storage.get_products())


class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self) -> str:
        if self.bullets > 0:
            self.bullets -= 1
            return 'shooting...'
        else:
            return 'no bullets left'

    def info(self) -> str:
        return f'Remaining bullets: {self.bullets}'

    # def __str__(self):
    #     return self.info()


# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.info())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.info())


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product[0] == first_letter]

    def info(self) -> str:
        info_products = ', '.join(self.products)
        return f'Items in the {self.name} catalogue: {info_products}.'

    # def __str__(self):
    #   return self.info()


catalogue = Catalogue('Furniture')
# catalogue.add_product('Sofa')
# catalogue.add_product('Mirror')
# catalogue.add_product('Desk')
# catalogue.add_product('Chair')
# catalogue.add_product('Carpet')
# print(catalogue.get_by_letter('C'))
# print(catalogue.info())


class Town:
    def __init__(self, city_name: str):
        self.city_name = city_name
        self.latitude = '0°N'
        self.longitude = '0°E'

    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude

    def info(self) -> str:
        return f'Town: {self.city_name} | Latitude: {self.latitude} | Longitude: {self.longitude}'


sofia = Town('Sofia')
sofia.set_latitude('42.698334')
sofia.set_longitude('23.319941')
print(sofia.info())
