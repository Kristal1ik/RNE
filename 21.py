def f(x, h):
    if x >= 68 and (h == 5 or h == 3):
        return 1
    if x < 68 and h == 5:
        return 0
    if x >= 68:
        return 0
    if h % 2 == 0:
        return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
    else:
        return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)


def f1(x, h):
    if x >= 68 and h == 3:
        return 1
    if x < 68 and h == 3:
        return 0
    if x >= 68:
        return 0
    if h % 2 == 0:
        return f1(x + 1, h + 1) or f1(x + 4, h + 1) or f1(x * 5, h + 1)
    else:
        return f1(x + 1, h + 1) and f1(x + 4, h + 1) and f1(x * 5, h + 1)


for s in range(1, 68):
    if f(s, 1) == 1:
        print(s)

print("---------")

for s in range(1, 68):
    if f1(s, 1) == 1:
        print(s)


