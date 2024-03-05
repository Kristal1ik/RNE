def f(x, y, h):
    if h == 3 and x + y >= 49:
        return 1
    if h == 3 and x + y < 49:
        return 0
    if x + y >= 49 and h < 3:
        return 0

    return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 3, y, h + 1) or f(x, y * 3, h + 1)


for x in range(1, 44):
    if f(x, 5, 1) == 1:
        print(x)
