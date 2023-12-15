# # x - текущее число
# # y - необходимое число
# def f(x, y):
#     if x == y:
#         return 1
#     if x > y:
#         return 0
#     return f(x + 2, y) + f(x * 5, y)
#
#
# print(f(2, 50))


def f(x, y, his):
    if x == y and 16 in his:
        return 1
    if x < y:
        return 0
    return f(x - 1, y, his + [x - 1]) + f(x // 2, y, his + [x // 2])


print(f(78, 4, [2]))
