# x = 3
# y = 7
# ans = ((5 * x + 7 * y) / (x - y)) + ((7 * x - 3) / ((1 / (x + x ** 2)) - (1 / (y ** 0.5))))
# print(ans)

# a, b, c = list(map(int, input().split()))
# d = b ** 2 - 4 * a * c
# if d < 0:
#     print("d<0")
# elif d >= 0:
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     print("x1:", x1, "x2:", x2)

n = int(input())
for i in range(n):
    lst = []
    for j in range(i+1):
        lst.append("*")
    print(''.join(lst))
