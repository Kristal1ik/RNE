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

for i in range(131, 256):
    n = bin(i)[2:].rjust(8, "0")
    n_new = n[:2] + n[-2:]
    n_new = int(n_new, 2)
    if n_new == 10:
        print(i, n_new)
        break
