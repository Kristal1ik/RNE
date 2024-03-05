def eval(n):
    lst = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            lst.append(i)
    return lst


#
#
# lst_all = []
# mx_len = 0
# mx_n = 0
# for i in range(120115, 120200 + 1):
#     if mx_len <= len(eval(i)):
#         mx_n = i
#         mx_len = len(eval(i))
# print(mx_len, mx_n)


# lstt = []
# n = 1
# for i in range(2422000, 2422080 + 1):
#     if len(eval(i)) == 0:
#         lstt.append([n, i])
#         n += 1
#
# print(lstt)

# lst = []
# a = 289123456 ** (1 / 2)
# b = 389123456 ** (1/2)
# print(a, b)
# for i in range(289123456, 389123456):
#     if
# print(lst)

# lst = []
# n = 0
# for i in range(500000, 1000000):
#     if n >= 5:
#         break
#     lst_n = eval(i)
#     for j in lst_n:
#         if str(j)[-1] == "8" and j != 8:
#             lst.append([i, lst_n])
#             n += 1
#             break
#
# for i in lst:
#     print(i[0], i[1])


from fnmatch import *

for x in range(0, 10 ** 10, 4891):
    if fnmatch(str(x), '1?2711*0'):
        print(x)
