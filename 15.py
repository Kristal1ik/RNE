# for A in range(300):
#     n = 0
#     for x in range(300):
#         if ((x & 42 != 0) or (x & 13 != 0)) <= ((x & 30 == 0) <= (x & A != 0)):
#             n += 1
#     if n == 300:
#         print(A)


# p = [i for i in range(3, 39)]
# q = [i for i in range(21, 58)]
# A = []
# mx_len = 0
# for a1 in range(100):
#     for a2 in range(a1, 100):
#         n = 0
#         for x in range(100):
#             if ((x in q) <= (x in p)) <= (not (a1 <= x <= a2)):
#                 n += 1
#         if n == 100:
#             mx_len = max(mx_len, a2 - a1 + 1)
# print(mx_len)

# for a in range(1, 1000):
#     n = 0
#     for x in range(1, 1000):
#         if (((x % 4 == 0) <= (not(x % 6 == 0))) or (x % a == 0)) == False:
#             n = 1
#             break
#     if n == 0:
#         print(a)
#
#
# def f(x, a_left, a_right):
#     return (15 <= x <= 44) <= ((not (20 <= x <= 46) and not (a_left <= x <= a_right)) <= (not (15 <= x <= 44)))
#
#
# len_min = 1e9
# for i in range(-100, 100):
#     for j in range(i, 100):
#         for x in range(1, 1000):
#             flag = True
#             if not(f(x, i, j)):
#                 flag = False
#                 break
#         if flag:
#             if j - i < len_min:
#                 len_min = j - i
#                 # print(i, j)
# print(len_min)

# for a in range(1, 1000):
#     f = True
#     for x in range(1, 1000):
#         if not((x & 15 != 0) <= ((x & 34 == 0) <= (x & a != 0))):
#             f = False
#     if f:
#         print(a)
#         break

# p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
# q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
# lst_a = []
# for a in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         if not(((x in q) <= (x in a)) and (not (x in a) <= (x not in p))):
#             flag = False
#             break
#     if flag:
#         lst_a.append(a)
# print(lst_a)

for a in range(1, 300):
    flag = True
    for x in range(1, 300):
        for y in range(1, 300):
            if not((2 * x + y > a) or (y < x) or (x < 28)):
                flag = False
    if flag:
        print(a)
