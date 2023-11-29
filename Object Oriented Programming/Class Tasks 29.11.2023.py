import random

# First Task
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce_yourself(self):
        return f'Hi, my name is {self.name} and I am {self.age} years old.'

    def start_working(self):
        if self.age >= 18:
            return f'Starting to work...'
        else:
            return f'You are not old enough to start working...'


me = Human('Peter', 20)

print(me.introduce_yourself())
print(me.start_working())

underage = Human('Ivan', 16)

print(underage.introduce_yourself())
print(underage.start_working())


#Second Task
class Building:
    def __init__(self, building_type, height, construction_year, city):
        self.building_type = building_type
        self.height = height
        self.construction_year = construction_year
        self.city = city

    def show_data(self):
        print(f'Building type: {self.building_type}, Height: {self.height}, Construction Year: {self.construction_year}, City: {self.city}')

    def is_tall(self):
        if self.height > 30:
            print('The building is tall.')
        else:
            print('The building is not tall.')

    def should_be_rebuild(self):
        if self.construction_year < 1990:
            print('Should be rebuild')
        else:
            print('Should\'t be rebuild')

    def increase_height(self):
        self.height += 2
        print(f'Building size increased from {self.height -2} to {self.height}!')


sofia_building = Building('Construction Site', 20, 1934, 'Sofia')

sofia_building.show_data()

sofia_building.should_be_rebuild()

sofia_building.is_tall()

sofia_building.increase_height()


# Third Task
class GameDice:
    def __init__(self, number_of_sides: int, colour: str) -> None:
        self.number_of_sides = number_of_sides
        self.colour = colour

    def roll_the_dice(self) -> int:
        return random.randrange(1, self.number_of_sides)

    def change_number_of_sides(self, new_number_of_sides: int) -> None:
        self.number_of_sides = new_number_of_sides


dice = GameDice(6, 'Black and White')


print(f'The dice rolled on {dice.roll_the_dice()}.')

dice.change_number_of_sides(10)

print(f'The new number of sides is {dice.number_of_sides}.')

