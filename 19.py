import sys

sys.setrecursionlimit(1000000)


# Петя сделал неудачный ход, Ваня выиграл (всего два хода) — без рекурсии
# for s in range(1, 56):
#     if ((s + 1) * 2 >= 56 and s + 1 < 56) or \
#             ((s + 4) * 2 >= 56 and s + 4 < 56) or \
#             ((s * 2) * 2 >= 56 and s * 2 < 56):
#         print(s)
#         break
# print("df")


# Петя сделал неудачный ход, Ваня выиграл (всего два хода) — с рекурсией
# s — количество камней
# h — количество ходов
# 1 — начальное состояние
# 2 — первый ход
# 3 — второй ход
# def f(s, h):
#     if h == 3 and s >= 68:
#         return 1
#     if h == 3 and s < 68:
#         return 0
#     if h < 3 and s >= 68:
#         return 0
#     return f(s + 1, h + 1) or f(s + 4, h + 1) or f(s * 5, h + 1)
#
#
# for s in range(1, 68):
#     if f(s, 1):
#         print(s)


def f(x, y, h):
    if x * y >= 512 and h == 3:
        return 1
    if h == 3 and x * y < 512:
        return 0
    if x * y >= 512:
        return 0
    if h % 2 == 0:
        return f(x + 1, y, h + 1) and f(x, y + 1, h + 1) and \
           f(x + 5, y, h + 1) and f(x, y + 5, h + 1) and \
           f(x * 2, y, h + 1) and f(x, y * 2, h + 1)
    return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or \
           f(x + 5, y, h + 1) or f(x, y + 5, h + 1) or \
           f(x * 2, y, h + 1) or f(x, y * 2, h + 1)


m = 1000000000000
for s in range(1, 512):
    for s2 in range(1, 512):
        if f(s, s2, 1) == 1:
            print(s, s2, s * s2)
            m = min(m, s+s2)
print(m)
