from functools import lru_cache  # импортируем кэширование


# @lru_cache(None)
# def f(a, b):
#     if a + b >= 50:
#         return 0  # условие выигрыша
#
#     moves = [f(a + 2, b), f(a * 3, b), f(a, b + 2), f(a, b * 3)]
#     win_petya = [i for i in moves if i <= 0]
#     if win_petya:
#         return -max(win_petya) + 1
#     else:
#         return -max(moves)
#
#
# n = 0
# for i in range(1, 40):
#     for j in range(1, 40):
#         if f(i, j) == -3 and not (f(i, j) == -2) and not (f(i, j) == -1):
#             n += 1
# print(n)

# @lru_cache(None)
# def f(a):
#     if a >= 65:
#         return 0  # условие выигрыша
#     if a * 3 > 109:
#         moves = [f(a + 7), f(a + 5)]
#     else:
#         moves = [f(a + 7), f(a * 3), f(a + 5)]
#     win_petya = [i for i in moves if i <= 0]
#     if win_petya:
#         return -max(win_petya) + 1
#     else:
#         return -max(moves)
#
#
# n = 0
# for i in range(1, 40):
#     if f(i) == 2:
#         print(i)
# print(n)

@lru_cache(None)
def f(a, b, c):
    if a + b + c >= 300:
        return 0  # условие выигрыша

    moves = [f(a+b+c, b, c), f(a, b+a+c, c), f(a, b, c+a+b),
             f(a*3, b, c), f(a, b*3, c), f(a, b, c*3)]
    win_petya = [i for i in moves if i <= 0]
    if win_petya:
        return -max(win_petya) + 1
    else:
        return -max(moves)


n = 0
lst = []
for i in range(1, 101):
    if f(45, i, i + 25) == 3 and not (f(45, i, i + 25) == 2) and not (f(45, i, i + 25) == 1):
        lst.append(i)
        n += 1
print(n)
print(lst)