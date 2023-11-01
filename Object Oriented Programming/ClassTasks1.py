def my_function():
    print("Hello from a function")
#  Void Function, printing a Hello message


def my_function(fname):
    print(fname + " Refsnes")
#  Void function with one parameter printing a message on the console

#  Calling the function
my_function("Emil")
my_function("Tobias")
my_function("Linus")


def person_details(name: str, address: str, phone_number: str):
    print(f'Person: {name}, Address: {address}, Phone Number: {phone_number}')


def multiply_numbers(first_num: int, second_num: int):
    return first_num * second_num

multiply_numbers_lambda_method = lambda a, b : a * b

# print(multiply_numbers_lambda_method(4, 5))


def find_inner_sum(m: int):
    return sum([num for num in range(m + 1)])

# print(find_inner_sum(5))

def print_cash_receipt():

    def print_row():
        print(''.join(['-' for _ in range(25)]))

    print_row()
    print(''.join([' ' if _ != 0 else "|" for _ in range(6)]) + f'CASH RECEIPT' + ''.join([' ' if _ != 6 else "|" for _ in range(7)]))
    print_row()
    print(''.join([' ' if _ != 0 else "|" for _ in range(8)]) + f'PRODUCTS:' + ''.join([' ' if _ != 7 else "|" for _ in range(8)]))
    print_row()
    print(''.join([' ' if _ != 0 else "|" for _ in range(6)]) + f'MOCHA COFFEE' + ''.join([' ' if _ != 6 else "|" for _ in range(7)]))
    print(''.join([' ' if _ != 0 else "|" for _ in range(6)]) + f'ESPRESSO COFFEE' + ''.join( [' ' if _ != 3 else "|" for _ in range(4)]))
    print(''.join([' ' if _ != 0 else "|" for _ in range(6)]) + f'Caffè Verona' + ''.join([' ' if _ != 6 else "|" for _ in range(7)]))
    print(''.join([' ' if _ != 0 else "|" for _ in range(8)]) + f'Pike Place' + ''.join([' ' if _ != 6 else "|" for _ in range(7)]))
    print_row()
    print(''.join([' ' if _ != 0 else "|" for _ in range(4)]) + f'TOTAL PRICE: 34.48$' + ''.join([' ' if _ != 1 else "|" for _ in range(2)]))
    print_row()

print_cash_receipt()


entered_number = int(input("Enter a number that has to be recognized: "))
print(f'{entered_number} is  a positive number!') if entered_number > 0 else print(f'{entered_number} is zero!') if entered_number == 0 else print(f'{entered_number} is a negative number!')
