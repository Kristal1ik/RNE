# with open('9.txt') as f:
#     data = f.read().splitlines()
# n = 0
# for i in data:
#     i = list(map(int, i.split("\t")))
#     if len(i) == len(set(i)) and (((max(i) + min(i)) / 2) < (sum(i) / len(i))):
#         n += 1
# print(n)

# data = [1,2,2]
# sums = {}
# for element in data:
#     sums[element] = data.count(element) * element
# print(sums)

# with open("9.csv") as f:
#     data = f.read().splitlines()
# n = 0
# for i in data:
#     line = list(map(int, i.split(";")))
#     d = dict()
#     for j in line:
#         if j not in d.keys():
#             d[j] = 1
#         else:
#             d[j] += 1
#     f3 = False
#     f1_count = 0
#     f3_num = 0
#     f1_sum = 0
#     for k, v in d.items():
#         if v == 3:
#             f3 = True
#             f3_num = k
#         elif v == 1:
#             f1_count += 1
#             f1_sum += k
#     if f3 and f1_count == 4 and f1_sum / 4 < f3_num:
#         n += 1
# print(n)

# with open("9_4.txt", encoding="utf-8") as f:
#     data = f.read().splitlines()
# n = 0
#
# for i in data:
#     line = list(map(int, i.split(";")))
#     d = dict()
#     for j in line:
#         if j not in d:
#             d[j] = 1
#         else:
#             d[j] += 1
#     f2 = False
#     f1_count = 0
#     lst1 = []
#     f2_num = 0
#     for k, v in d.items():
#         if v == 2:
#             f2 = True
#             f2_num = k
#         elif v == 1:
#             f1_count += 1
#             lst1.append(k)
#     if len(lst1) == 5 and f2:
#         proizv = 1
#         lst1 = sorted(lst1)[:3]
#         for j in lst1:
#             proizv *= j
#         if proizv > f2_num ** 2:
#             n += 1
# print(n)


# def ost(lst):
#     set_ost = set()
#     for i in lst:
#         set_ost.add(i%6)
#     if len(lst) == len(set_ost):
#         return True
#     return False
#
# with open("9_4_щелчок.csv") as f:
#     data = f.read().splitlines()
# n = 0
# f = False
# for i in data:
#     if not f:
#         i = i[3:]
#         f = True
#     i = list(map(int, i.split(";")))
#     if ost(i) and (sum(i) % 25 == 0 or sum(i) % 7 == 0):
#         n += 1
# print(n)

# def sum_last(lst):
#     summ = 0
#     for i in lst:
#         summ += i % 10
#     if summ % 15 == 0:
#         return True
#     return False
#
#
# with open("9_5_щелчок.csv") as f:
#     data = f.read().splitlines()
# f = False
# n = 0
# for i in data:
#     if not f:
#         i = i[3:]
#         f = True
#     i = list(map(int, i.split(";")))
#     if sum_last(i) and (sum(i) > sum(i) // len(i)):
#         n += 1
# print(n)
#

# def one_repeat(lst):
#     set_lst = set(lst)
#     if len(set_lst) == len(lst):
#         return True
#     return False
#
#
# with open("9_7_щелчок.csv") as f:
#     data = f.read().splitlines()
# f = False
# n = 0
# for i in data:
#     if not f:
#         f = True
#         i = i[3:]
#     i = sorted(list(map(int, i.split(";"))))
#     if one_repeat(i) and not((max(i) - min(i)) > i[1]):
#         n += 1
#     elif not one_repeat(i) and (max(i) - min(i)) > i[1]:
#         n += 1
# print(n)

def chet_nechet(lst):
    chet = 0
    nechet = 0
    for i in range(1, len(lst) + 1):
        if i % 2 == 0:
            chet += lst[i - 1]
        else:
            nechet += lst[i - 1]
    return abs(chet - nechet) > 40

def twice(lst):
    return len(lst) == (len(set(lst))+1)

def sr(lst):
    if (max(lst) + min(lst)) < (2 * (sum(lst) / len(lst))):
        return True
    return False

with open("9_9_щелчок.csv") as f:
    data = f.read().splitlines()
n = 0
f = False
for i in data:
    if not f:
        f = True
        i = i[3:]
    i = list(map(int, i.split(";")))
    f1 = chet_nechet(i)
    f2 = twice(i)
    f3 = sr(i)
    if f1 and not f2 and not f3:
        n += 1
    elif not f1 and f2 and not f3:
        n += 1
    elif not f1 and not f2 and f3:
        n += 1
print(n)
