def binary_search(binary_list: List[int], searched_number: int) -> List[int]:
    first_half = (binary_list[:len(binary_list) // 2])
    second_half = (binary_list[len(binary_list) // 2:])
    if len(second_half) == 1:
        print(second_half)
        return second_half
    elif second_half[0] > searched_number:
        print(first_half)
        return binary_search(first_half, searched_number)
    else:
        print(second_half)
        return binary_search(second_half, searched_number)


binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 2)
