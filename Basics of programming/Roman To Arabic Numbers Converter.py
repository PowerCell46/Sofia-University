inputted_roman_number = "MCXI"

roman_numbers_dictionary = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000}

current_biggest = inputted_roman_number[0]
result = roman_numbers_dictionary[current_biggest]
keeper = 0

for index in range(1, len(inputted_roman_number)):
    current_roman_number = inputted_roman_number[index]

    if roman_numbers_dictionary[current_roman_number] == roman_numbers_dictionary[current_biggest]:
        if keeper > 0:
            keeper += roman_numbers_dictionary[current_roman_number]
        else:
            result += roman_numbers_dictionary[current_roman_number]

    elif roman_numbers_dictionary[current_roman_number] > roman_numbers_dictionary[current_biggest]:

        if roman_numbers_dictionary[current_roman_number] > result:
            result = roman_numbers_dictionary[current_roman_number] - result

        else:
            result += roman_numbers_dictionary[current_roman_number] - keeper
            keeper = 0
        current_biggest = current_roman_number

    elif roman_numbers_dictionary[current_roman_number] < roman_numbers_dictionary[current_biggest]:
        there_is_not_a_bigger_number = True
        for i in range(index + 1, len(inputted_roman_number)):
            if roman_numbers_dictionary[inputted_roman_number[i]] > roman_numbers_dictionary[current_roman_number]:
                keeper += roman_numbers_dictionary[current_roman_number]
                current_biggest = current_roman_number
                there_is_not_a_bigger_number = False
                break
        if there_is_not_a_bigger_number:
            result += roman_numbers_dictionary[current_roman_number]

print(f'The inputted Roman number is equal to: {result}')
