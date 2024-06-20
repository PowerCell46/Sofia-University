def calculate_regression(first_lst, second_lst):
    first_lst_avg = sum(first_lst) / len(first_lst)
    second_lst_avg = sum(second_lst) / len(second_lst)

    first_result = 0
    for index in range(len(first_lst)):
        first_result += (first_lst[index] - first_lst_avg) * (second_lst[index] - second_lst_avg)

    second_result = 0
    for index in range(len(first_lst)):
        second_result += (first_lst[index] - first_lst_avg) ** 2

    b = first_result / second_result
    a = second_lst_avg - (b * first_lst_avg)

    return a, b


mothers_height_lst = [150, 155, 160, 165, 170]
children_height_lst = [160, 165, 167, 170, 175]

a, b = calculate_regression(mothers_height_lst, children_height_lst)

print(f"Coefficient a: {a}")
print(f"Coefficient b: {b}")

# Predicting the height of a child, knowing the height of the mother (160 см)
predicted_height = a + b * 160
print(f"Predicting the height of a child with mother 160 cm tall: {predicted_height} cm.")
