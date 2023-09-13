
# matrix = [[1, 2, 3], [4, 5, 6]]
# k = int(input())
# print(matrix[k])

# 9
# matrix = [[2, 6, 4], [8, 3, 0]]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] % 2 == 0:
#             print(matrix[i][j])

# for i in range(len(matrix)):
#     for j in range(0, len(matrix[i]), 2):
#         print(matrix[i][j] )

# from random import randint
#
# m = 5
# n = 5
# matr = []
# middle = 0
# for i in range(m):
#     l = []
#     for j in range(n):
#         num = randint(1,10)
#         middle += num
#         l.append(num)
#     matr.append(l)
# middle /= (m*n)
# min_diff = float('inf')
# s = 0
# stolb = 0
# for i in range(m):
#     for j in range(n):
#         diff = abs(middle - matr[i][j])
#         if diff < min_diff:
#             s = i
#             stolb = j
#             min_diff = diff
#
# print(matr)
# print(middle)
# print(s, stolb)

from random import randint

m = int(input())
matr = []
for i in range(m):
    l = []
    for j in range(m):
        num = randint(1,10)
        l.append(num)
    matr.append(l)


print(matr)
