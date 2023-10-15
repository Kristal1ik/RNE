import itertools


# itertools without walls
lines = """51  21  93  48  45  100  67  39  18  29
57  43  97  51  92  10  93  32  19  58
63  16  31  16  78  88  90  72  37  67
10  57  64  25  96  50  81  65  91  69
99  43  95  7  40  76  18  34  5  65
35  19  71  77  64  38  62  56  10  2
100  57  27  26  51  33  100  11  53  1
11  79  49  46  37  69  80  31  25  39
22  71  20  23  11  12  39  16  64  34
4  25  87  84  30  48  77  13  40  33"""
matrix = [[int(y) for y in x.split()] for x in lines.splitlines()]
min_s, max_s = None, None
for path in itertools.product([0, 1], repeat=len(matrix) + len(matrix[0]) - 2):
    if path.count(0) != len(matrix[0]) - 1:
        continue
    if path.count(1) != len(matrix) - 1:
        continue
    x, y = 0, 0
    s = matrix[0][0]
    for item in path:
        if item == 0:
            x += 1
        else:
            y += 1
        s += matrix[x][y]
    if max_s is None or s > max_s:
        max_s = s
    if min_s is None or s < min_s:
        min_s = s
print(max_s, min_s)


