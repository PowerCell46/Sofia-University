#  Направете списък от четните числа  от 1 до 100, като използвате цикъл

nums_1_to_100 = [n + 1 for n in range(100)]

# Изведете списъка, така че да има по 4 числа на ред

[print(n + 1, n + 2, n + 3, n + 4) for n in range(97) if n % 4 == 0]

#  Преоформете горните две задачи под формата на функция с два входни параметъра  ot и do. Изпълнете функцията с различни входни параметри.

def print_nums_from_to(start_num: int, end_num: int):
    nums_from_start_to_end = [start_num + 1 for start_num in range(end_num)]
    starting_point = start_num
    [print(start_num, start_num + 1, start_num + 2, start_num + 3) for start_num in range(start_num, end_num - 2) if (start_num - starting_point) % 4 == 0]

print_nums_from_to(1, 100)
