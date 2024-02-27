import math


def avg(*args):
    return sum([val for val in args]) / len(args)


def mean(*args):
    if len(args) % 2 != 0:
        return list(args)[len(list(args)) // 2 - 1]
    else:
        return (avg(args[len(args) // 2 - 1] + args[len(args) // 2])) / 2


def mode(*args):
    dict = {}
    elements = set(args)
    for el in elements:
        dict[el] = args.count(el)
    sorted_dict = sorted(dict.items(), key=lambda x: x[-1])
    max_value = max([el[1] for el in sorted_dict])
    if [el[1] for el in sorted_dict].count(max_value) == 1:
        return sorted_dict[0][0]
    else:
        return [el[0] for el in sorted_dict if el[1] == max_value]


print(5 + 3)

print((10 - 5) * 7)

print(avg(5 + 6 + 7 + 8))

print(math.sqrt(3) + math.sqrt(4) + math.sqrt(5))

print(avg(3, 5, 7))

res1 = [3, 7, 5, 4, 5, 6, 7, 8, 6, 5]
res2 = [34, 54, 17, 26, 34, 25, 14, 24, 25, 23]
res3 = [154, 167, 132, 145, 154, 145, 113, 156, 154, 123]


print(avg(*res1))
print(avg(*res2))
print(avg(*res3))


print(mean(*res1))
print(mean(*res2))
print(mean(*res3))


print(mode(*res1))
print(mode(*res2))
print(mode(*res3))
