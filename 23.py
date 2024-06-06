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

# def eval_count(m):
#     n = 0
#     for i in m:
#         count = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 count += 1
#         if count == 1:
#             n += 1
#     return n
#
#
# def f(x, y, his):
#     if x == y and eval_count(his) == 3:
#         return 1
#     if x > y:
#         return 0
#     return f(x + 1, y, his + [x + 1]) + \
#     f(x + 3, y, his + [x + 3]) + f(x * 2, y, his + [x * 2])
#
#
# print(f(1, 35, [1]))


# def f(x, y, his):
#     if x == y and 10 in his and 17 not in his:
#         return 1
#     if x > y:
#         return 0
#     return f(x + 2, y, his + [x + 2]) + \
#            f(x + 3, y, his + [x + 3]) + f(x * 2, y, his + [x * 2])
#
#
# print(f(3, 25, [3]))

# def f(n, t):
#     if n == t:
#         return 1
#     if n > t:
#         return 0
#     return f(n + 4, t) + f(n * 2, t)
#
#
# print(f(13, 42))
#
# def f(n, t, his):
#     if n == t and 10 in his and 11 not in his and 12 not in his:
#         return 1
#     if n > 40:
#         return 0
#     return f(n + 1, t, his + [n + 1]) + f(n * 2, t, his + [n * 2]) + f(n ** 2, t, his + [n ** 2])
#
#
# print(f(2, 40, []))


# def f(n, t, his):
#     if n == t and 10 in his and 20 not in his :
#         return 1
#     if n < 5:
#         return 0
#     return f(n - 2, t, his + [n - 2]) + f(n - 3, t, his + [n - 3]) + f(n // 5, t, his + [n // 5])
#
#
# print(f(41, 5, []))

# def f(n, t, his):
#     if n == t and 25 not in his:
#         return 1
#     if n > 115:
#         return 0
#     return f(n + 3, t, his + [n + 3]) + f(n * 2, t, his + [n * 2]) + f(n * 5, t, his + [n * 5])
#
#
# print(f(5, 115, []))

# def not_five(lst):
#     for i in lst:
#         if i % 5 == 0:
#             return False
#     return True


# def f(start, finish, his):
#     if start == finish and not_five(his):
#         return 1
#     if start > finish:
#         return 0
#     return f(start + 4, finish, his + [start + 4]) + f(start + 5, finish, his + [start + 5])
#
# print(f(31, 60, []))


def f(start, finish, his):
    if start == finish and 9 in his and 21 not in his:
        return 1
    if start > finish:
        return 0
    return f(start + 1, finish, his + [start + 1]) + f(start * 2, finish, his + [start * 2]) + f(start * 3, finish,
                                                                                                 his + [start * 3])
print(f(2, 37, []))