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


# def f(x, y, his):
#     if x == y and 16 in his:
#         return 1
#     if x < y:
#         return 0
#     return f(x - 1, y, his + [x - 1]) + f(x // 2, y, his + [x // 2])
#
#
# print(f(78, 4, [2]))


# def f(x, y, his):
#     if x == y and 14 not in his:
#         return 1
#     if x > y:
#         return 0
#     return f(x + 1, y, his + [x + 1]) + f(x * 2, y, his + [x * 2]) + f(x ** 2, y, his + [x ** 2])
#
#
# print(f(3, 25, [3]))


# def f(x, y, his):
#     if x == y and 15 not in his and 14 in his:
#         return 1
#     if x > y:
#         return 0
#     return f(x + 1, y, his + [x + 1]) + f(x + 3, y, his + [x + 3]) + f(x * 3, y, his + [x * 3])
#
#
# print(f(7, 20, [7]))

def eval_count(m):
    n = 0
    for i in m:
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count == 1:
            n += 1
    return n


def f(x, y, his):
    if x == y and eval_count(his) == 3:
        return 1
    if x > y:
        return 0
    return f(x + 1, y, his + [x + 1]) + f(x + 3, y, his + [x + 3]) + f(x * 2, y, his + [x * 2])


print(f(1, 35, [1]))
