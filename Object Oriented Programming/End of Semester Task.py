class Animal:
    def __init__(self, type: str, name: str, age: int, price: float):
        self.type = type
        self.name = name
        self.age = age
        self._price = None
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value:float):
        if value > 0:
            self._price = value
        else:
            print(f'Invalid Price - setting it to the default value of 10 BGN!')
            self._price = 10

    def christmas_discount(self, discount_percentage: int) -> None:
        if discount_percentage == 0 or discount_percentage == 100:
            raise ValueError(f"Cannot decrease the price by {discount_percentage}%!")

        self.price -= (self.price / 100) * discount_percentage
        print(f'New Price of {self.name}: {self.price:.2f} BGN!\nHappy Holidays!')

    def __str__(self) -> str:
        return f'{self.name} of Type "{self.type}" is {self.age} years old and costs {self.price:.2f} BGN.'

    def showcase(self):
        return self.__str__()


cat = Animal('Cat', 'Sharo', 8, 50)
cat.christmas_discount(3)
dog = Animal('Dog', 'Raffy', 3, 150)
salamander = Animal('Salamander', 'Fluffy', 1, 300)


class BasePetShop:
    def __init__(self, name: str, location: str, pets: [Animal]):
        self.name = name
        self.location = location
        self.pets = pets
        self.income = 0

    def add_pet(self, pet: Animal) -> str:
        self.pets.append(pet)
        return f'{pet.name} successfully added to {self.name}!'

    def sell_pet(self, pet_name: str) -> str:
        pet = [p for p in self.pets if p.name == pet_name]
        if len(pet) > 0:
            self.pets.remove(pet[0])
            self.income += pet[0].price
            return f'{pet[0].name} was successfully sold for {pet[0].price:.2f} BGN.'
        else:
            return f'No such pet found in the {self.name}!'

    def __repr__(self):
        pets = "\n  ".join([p.showcase() for p in self.pets])
        return f'{self.name} located at {self.location} with income of {self.income} BGN.\nAvailable Pets in the Store:\n  {pets}'


myShop = BasePetShop('My Zoo Shop', 'Sofia Center', [cat, dog, salamander])

fish = Animal('Fish', 'Dorry', 3, 20)

# print(myShop.add_pet(fish))
#
# print(myShop.sell_pet('Dorry'))
#
# print(myShop)


def write_in_file(filename: str, message: str) -> None:
    file = open(filename, 'a')
    file.writelines(f'{message}\n')
    file.close()


class PetShop(BasePetShop):
    def __init__(self, name: str, location: str, pets: [Animal], space: int, slogan: str):
        super().__init__(name, location, pets)
        self.space = space
        self.slogan = slogan
        write_in_file('petshop_logger.txt', f'Initializing {self.name} with: {", ".join([p.name for p in pets])}.')

    def add_pet(self, pet: Animal) -> str:
        if self.space > 0:
            self.space -= 1
            self.pets.append(pet)

            message = f'{pet.name} successfully added to {self.name}!'
            write_in_file('petshop_logger.txt', message)
            return message
        else:
            return f'Not enough space in {self.name}!'

    def sell_pet(self, pet_name: str) -> str:
        pet = [p for p in self.pets if p.name == pet_name]
        if len(pet) > 0:
            self.pets.remove(pet[0])
            self.income += pet[0].price
            message = f'{pet[0].name} was successfully sold for {pet[0].price:.2f} BGN!'
            write_in_file('petshop_logger.txt', message)
            return message
        else:
            return f'No such pet found in the {self.name}!'

myPetShop = PetShop('Zoo', 'Durvenitsa', [cat, salamander, dog], 4, 'We live together!')
myPetShop.add_pet(cat)
print(myPetShop.sell_pet('Fluffy'))
print(myShop)
