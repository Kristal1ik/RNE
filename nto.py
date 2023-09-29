# 1
# n = int("11011001", 2)
# for i in range(2**7, 2**9):
#     nn = n
#     for j in range(127):
#         nn = nn ^ int(i)
#         if nn == int("1100011", 2):
#             print(i)
# print(bin(186))

# 2
# n = 41
# m = 57
# r = 0
# while n != m:
#     if n != m:
#         if n < m:
#             n += 3
#         else:
#             m += 7
#         r += 1
# print(r)

# 3
# n=0
# for i in range(1, 65):
#     for j in range(1, 65):
#         x = 2**i - 1
#         y = 2**j - 1
#         proizv = bin(x*y)[2:]
#         if (x>y) and ("0" in proizv) and ("1" in proizv) and (abs(proizv.count("1") - proizv.count("0"))<=13):
#             n+= 1
#
# print(n)

# 4
# n = int(input())
# index = 0
# nn = 0
# numbers = list(map(int, input().split()))
# numbers_ind = [i for a, i in sorted(zip(numbers, [j for j in range(n)]))]
#
# for i in numbers_ind:
#     if index <= i:
#         nn += abs(index - i)
#         index = i
#     else:
#         nn += n-index+i
#         index = i
# print(nn)
#

# 5
# n = int(input())
# summ = 0
#
# lst = [0] * 501
# for i in range(n):
#     s = list(map(int, input().split()))
#     lst[s[0]], lst[s[1]] = lst[s[0]] - s[2], lst[s[1]]+s[2]
#     if lst[s[0]] <0:
#         summ-=lst[s[0]]
#         lst[s[0]] = 0
# print(abs(summ))

# 1
# a, b, c = map(int, input().split())
# middle_summ = int((a + b + c) / 2)
# lst = [0, 0, 0]
# if middle_summ - a >0:
#     middle_summ -= a
#     if middle_summ - b >0:
#         middle_summ -= b
#         lst[0], lst[1], lst[2] = a, b, middle_summ
#     else:
#         lst[0], lst[1] = a, middle_summ
# else:
#     lst[0] = middle_summ
# print(*lst)

# for i in range(1, a+ 1):
#     for j in range(1, b+1):
#         for k in range(1, c + 1):
#             if i + j + k == middle_summ:
#                 lst[0], lst[1], lst[2] = i, j, k
# print(*lst)

# 2
# from functools import cmp_to_key
#
#
# def fitness(letter):
#     if letter == 'r':
#         return -3
#     elif letter == 'g':
#         return -2
#     elif letter == 'b':
#         return -1
#
#
# def compare(item1, item2):
#     if fitness(item1[0]) < fitness(item2[0]):
#         return -1
#     elif fitness(item1[0]) > fitness(item2[0]):
#         return 1
#     else:
#         return 0
#
#
# s = input()
# s2 = list(map(int, input().split()))
# colors = [(s[i], s2[i]) for i in range(len(s))]
# colors = sorted(colors, key=cmp_to_key(compare))
# for i in colors:
#     print(i[1], end=' ')


# 3
# import itertools
# import sys
#
# def check(s):
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             return False
#     return True
#
#
# s = input()
# parts = []
# first = -1
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         if first == -1:
#             first = i
#             parts.append((s[:i], 1, i))
#         else:
#             parts.append((s[first:i], first + 1, i))
#             parts.append((s[i:], i + 1, len(s)))
#
# for x in itertools.permutations(parts):
#     for i in range(2):
#         for j in range(2):
#             for k in range(2):
#                 tmp1 = x[0][0]
#                 tmp2 = x[1][0]
#                 tmp3 = x[2][0]
#                 if i:
#                     tmp1 = tmp1[::-1]
#                 if j:
#                     tmp2 = tmp2[::-1]
#                 if k:
#                     tmp3 = tmp3[::-1]
#                 if check(tmp1 + tmp2 + tmp3):
#                     print(x[0][1], x[0][2], 180 if i else 0)
#                     print(x[1][1], x[1][2], 180 if j else 0)
#                     print(x[2][1], x[2][2], 180 if k else 0)
#                     sys.exit()
# print("no")


# 4
# from pprint import pprint
#
# matr = []
# n = int(input())
# for i in range(1, n + 1):
#     lst_x = []
#     for j in range(1, n + 1):
#         lst_y = []
#         for k in range(1, n + 1):
#             lst_y.append(0)
#         lst_x.append(lst_y)
#
#     matr.append(lst_x)
# lst = []
# for x in range(n):
#     for y in range(n):
#         for z in range(n):
#             if matr[x][y][z] == 0:
#                 matr[x][y][z] = 1
#                 lst.append([x, y, z])
#                 for i in range(n):
#                     matr[x][y][i] = -1 if matr[x][y][i] != 1 else 1
#                 for j in range(n):
#                     matr[x][j][z] = -1 if matr[x][j][z] != 1 else 1
#                 for k in range(n):
#                     matr[k][y][z] = -1 if matr[k][y][z] != 1 else 1
# pprint(matr)
# print(lst, len(lst))
# put your python code here


from copy import deepcopy

matr = []
n = int(input())
for i in range(1, n + 1):
    lst_x = []
    for j in range(1, n + 1):
        lst_y = []
        for k in range(1, n + 1):
            lst_y.append(0)
        lst_x.append(lst_y)

    matr.append(lst_x)
lst = []


def solve(x0, y0, z0, n1):
    global lst
    global n
    global matr
    temp_matr = deepcopy(matr)
    for x in range(x0, n):
        for y in range(y0, n):
            for z in range(z0, n):
                if matr[x][y][z] == 0:
                    matr[x][y][z] = 1
                    lst.append([x, y, z])
                    for i in range(n):
                        matr[x][y][i] = -1 if matr[x][y][i] != 1 else 1
                    for j in range(n):
                        matr[x][j][z] = -1 if matr[x][j][z] != 1 else 1
                    for k in range(n):
                        matr[k][y][z] = -1 if matr[k][y][z] != 1 else 1
                    if not solve(x, y, z, n1 + 1):
                        matr = temp_matr
                        lst.pop()
                    else:
                        return True
            z0 = 0
        y0 = 0
    if n**2 != n1:
        return False
    return True


solve(0, 0, 0, 0)

for x in lst:
    print(*x)

