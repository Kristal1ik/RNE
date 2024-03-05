import sys

sys.setrecursionlimit(1000000)


# def f(n):
#     if n > 2024:
#         return n
#     elif n <= 2024:
#         return n * f(n + 1)
#
#
# print(f(2022) / f(2024))

# def ff(n):
#     if n < 11:
#         return n
#     elif n >= 11:
#         return n + ff(n - 1)
#
#
# print(ff(2024) - ff(2021))

# def f(n):
#     if n < 3:
#         return 1
#     elif n > 2 and n % 2 != 0:
#         return f(n - 1) + 3 * f(n - 2)
#     if n > 2 and n % 2 == 0:
#         summ = 0
#         for i in range(1, n):
#             summ += (f(i))
#         return summ
#
#
# print(f(28))

# def f(n):
#     if n >= 2000:
#         return 2000
#     if n < 2000 and n % 2 != 0:
#         return n * f(n + 1)
#     if n < 2000 and n % 2 == 0:
#         return n * f(n + 1) / 2
#
#
# print(f(1998) / f(2001))

def f(n):
    if n == 1:
        return 3
    if n > 1:
        return 3 * n + 2 * f(n - 1)


print(f(2024) - 4 * f(2022))
