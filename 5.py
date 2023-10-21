# 1
# lst = []
# for i in range(1000):
#     s = bin(i)[2:]
#     s = str(s)
#     if i % 3 == 0:
#         s += s[-3:]
#     else:
#         s += bin(3 * (i % 3))[2:]
#     r = int(s, 2)
#     if r > 76:
#         lst.append(i)
# print(min(lst))

# 2
# def f_bin(n):
#     s = ""
#     while n > 0:
#         ost = n % 2
#         s = str(ost) + s
#         n = n // 2
#     return s
#
#
# lst = []
# for i in range(1000):
#     n = f_bin(i)
#     n = n + str((int(n.count("1")) % 2))
#     n = n + str((int(n.count("1")) % 2))
#     r = int(n, 2)
#     if r > 154:
#         lst.append(i)
# print(min(lst))

def f_three(n):
    s = ""
    while n > 0:
        ost = n % 3
        s = str(ost) + s
        n = n // 3
    return s


#
# lst = []
# for i in range(1, 1000):
#     n = f_three(i)
#     if i % 3 != 0:
#         n = n + f_three((i % 3) * 5)
#     r = int(n, 3)
#     if r > 146:
#         lst.append(i)
# print(min(lst))

# for i in range(131, 256):
#     n = bin(i)[2:].rjust(8, "0")
#     n_new = n[:2] + n[-2:]
#     n_new = int(n_new, 2)
#     if n_new == 10:
#         print(i, n_new)
#         break

# for i in range(1000):
#     n = bin(i)[2:]
#     if n.count("1") % 2 == 0:
#         n = "1" + n + "00"
#     else:
#         n = "11" + n
#     if int(n, 2) >= 412:
#         print(i, int(n, 2))

# for i in range(1000, 10000):
#     i = str(i)
#     lst = []
#     first = int(i[0]) + int(i[1])
#     second = int(i[1]) + int(i[2])
#     third = int(i[2]) + int(i[3])
#     lst.append(first)
#     lst.append(second)
#     lst.append(third)
#     lst.sort()
#     answ = str(lst[1]) + str(lst[2])
#     if answ == "1517":
#         print(i)

# for i in range(1000):
#     str_ = [''.join(bin(int(j))[2:].rjust(4, "0") for j in str(i))]
#     str_1 = ''
#     for j in str_:
#         for k in j:
#             if k == "1":
#                 str_1 += "0"
#             else:
#                 str_1 += "1"
#     if int(str_1, 2) == 151:
#         print(i)
count = 0
for n in range(1222222222, 1555555667):
    n1 = bin(n)[2:]
    n1 = n1 + "0" + bin(n % 3)[2:]
    n2 = int(n1, 2)
    n1 += "0" + bin(n2 % 5)[2:]
    count += 1
print(count)
# print(int(n1, 2))

