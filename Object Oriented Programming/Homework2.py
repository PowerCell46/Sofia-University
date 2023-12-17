
# Да се напише функция за рекурсия, която пресмята поредното число от една редица, ако всяко следващо е сбор от предходните 3
lst = [1, 2, 3]


def add_recursive_new_number(working_list, index=3, current_index=len(lst), keeper=0):
    if index > 0:
        index -= 1
        current_index -= 1
        keeper += lst[current_index]
        return add_recursive_new_number(working_list, index, current_index, keeper)
    else:
        return working_list.append(keeper)


add_recursive_new_number(lst)
print(lst)
print(f'New number: {lst[-4]} + {lst[-3]} + {lst[-2]} = {lst[-1]}')


# За същата редица да се намери чрез рекурсия сумата на елементите


def find_recursive_sum(lst, index=len(lst), current_sum=0):
    if index > 0:
        index -= 1
        current_sum += lst[index]
        return find_recursive_sum(lst, index, current_sum)
    else:
        return current_sum


print(f'Recursive sum of the list: {find_recursive_sum(lst)}')
