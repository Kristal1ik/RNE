from functools import lru_cache  # импортируем кэширование
import sys



@lru_cache(None)
def f(a, b):
    if a + b >= 50:
        return 0  # условие выигрыша

    moves = [f(a + 2, b), f(a * 3, b), f(a, b + 2), f(a, b * 3)]
    win_petya = [i for i in moves if i <= 0]
    if win_petya:
        return -max(win_petya) + 1
    else:
        return -max(moves)


n = 0
for i in range(1, 40):
    for j in range(1, 40):
        if f(i, j) == -3 and not (f(i, j) == -2) and not (f(i, j) == -1):
            n += 1
print(n)
