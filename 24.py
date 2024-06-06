# with open("24 (1).txt") as file:
#     data = file.readline()
# n = 1
# now = 1
#
# for i in range(1, len(data)):
#     if data[i - 1] not in "ABC" or data[i] not in "ABC":
#         now += 1
#     else:
#         n = max(n, now)
#         now = 1
# print(n)

# вариант 2 -- заменить b, c на a, потом заменить "aa" на "a a"

# with open("24 (2).txt") as file:
#     data = file.readline().split("WW")
# n = 0
# now = 1
# count = 1
# for i in range(1, len(data)):
#     if not(data[i] == "W" and data[i-1] == "W") and now < 100:
#         count += 1
#     if data[i] == "W" and data[i-1] == "W":
#         now += 1
#     if now == 100:
#         n = max(n, count)
#         now = 1
#         count = 1
# print(n)

# with open("24") as file:
#     data = file.readline()
# n = 1
# max_n = 0
# for i in range(1, len(data)):
#     if data[i] != data[i - 1]:
#         n += 1
#     else:
#         max_n = max(n, max_n)
#         n = 1
# max_n = max(n, max_n)
# print(max_n)

# with open("24_1") as file:
#     data = file.readline()
# n = 1
# max_n = 0
# for i in range(0, len(data) - 2, 3):
#     if data[i] + data[i+1] + data[i+2] == "LDR":
#         print(data[i], data[i + 1], data[i + 2])
#
#         n += 1
#     else:
#         max_n = max(n, max_n)
#         n = 1
# max_n = max(n, max_n)
# print(max_n)

# s = "abcdefghiujklmnopqrstuvwxyz"
# with open("24_2.txt") as file:
#     data = file.readline().lower()
# d = {}
# for i in range(27):
#     d[s[i]] = 0
# for i in range(1, len(data) - 2):
#     if data[i] == data[i + 1]:
#         d[data[i + 2]] += 1
# print(d)
# print(max(d.values()))

# with open("24_3.txt") as file:
#     data = file.readline().lower()
# min_g = 1000000000
# index = 0
# for i in range(len(data)):
#     if min_g > data[i].count("G"):
#         min_g = data[i].count("G")
#         index = i
#
#
# print(min_g, index)
# d = {}
# s = "abcdefghijklmnopqrstuvwxyz"
#
# for i in range(27):
#     d[s[i]] = 0
# print(len((data)))
# for i in range(len(data)):
#     if i == index:
#         for j in data[i]:
#             print(i)
#
#             print(d[j])
#             d[j] += 1
# print(d)

# s = input()
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# max_k = ""
# max_v = 0
# for k, v in d.items():
#     if max_v < v:
#         max_v = v
#         max_k = k
# print(max_k)

# import collections
#
# s = input()
# cnt = collections.Counter(s)
# print(cnt.most_common(1)[0][0])

# with open("24_4.txt") as file:
#     data = file.readline()
# d = {}
# for i in range(1, len(data)-1):
#     if data[i-1] == data[i+1]:
#         if data[i] not in d:
#             d[data[i]] = 1
#         else:
#             d[data[i]] += 1
# max_k = ""
# max_v = 0
#
# for k, v in d.items():
#     if max_v < v:
#         max_v = v
#         max_k = k
# print(max_k)

# with open("24_5.txt") as file:
#     data = file.readline().split("KL")
# new_data = []
# for i in data:
#     new_data.append(i.split("LK"))
# mx = 0
# for i in new_data:
#     for j in i:
#         mx = max(mx, len(j))
# print(mx)


# f = open('24_6.txt')
# n = f.read()
# n = n.replace('AB', 'x').replace('CB', 'x')
# k = 0
# m = 0
# for i in range(len(n)):
#     if n[i] == 'x':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 0
# print(m)

# with open("24_7.txt") as file:
#     data = file.readline()
# n = 1
# mx_n = 0
# for i in range(1, len(data)):
#     if int(data[i-1]) > int(data[i]):
#         n += 1
#     else:
#         mx_n = max(mx_n, n)
#         n = 1
# print(mx_n)

# with open("24_8.txt") as file:
#     data = file.read().split()
#
# mx = 0
# n = 0
# lst = 0
# for i in range(0, len(data)-1):
#     if n < 210 and data[i] == "T":
#         n += 1
#     else:
#         mx = max(mx, lst)
#         n = 0
#     mx += 1
# print(mx)


# n = 1
# mx_n = 1
# with open("24_9.txt") as file:
#     data = file.read()
# for i in range(1, len(data)):
#     if int(data[i]) <= int(data[i-1]):
#         n += 1
#     else:
#         mx_n = max(n, mx_n)
#         n = 1
# print(mx_n)

# with open("24_10.txt") as file:
#     data = file.read()
# v = 0
# lst = []
# for i in range(len(data)):
#     if data[i] == "V":
#         lst.append(i)

# for i in range(1, len(data)):
#     if v < 120 and data[i] == "V":
#         v += 1
#     else:


# with open("24_11.txt") as file:
#     data = file.read()
# n = 0
# max_n = 0
# for i in range(1, len(data) - 1):
#     if data[i] == "P" and data[i-1] == "P":
#         max_n = max(n, max_n)
#         n = 1
#     else:
#         n += 1
# max_n = max(n, max_n)
#
# print(max_n)


# with open("24_12.txt") as file:
#     data = file.read()
# mx_posl = 0
# posl = 1
# for i in range(len(data) - 1):
#     if (data[i] == "X" and data[i+1] == "X") or (data[i] == "Y" and data[i+1] == "Y"):
#         if mx_posl < posl:
#             mx_posl = posl
#         posl = 1
#     else:
#         posl += 1
#         # print(data[i], data[i+1])
#
# print(mx_posl)

with open("24_егкр.txt") as f:
    data = f.read()

# for i in range(1, 1000):
#     if i * "FSWY" in data:
#         print(i)
print(45 * "FSWY")