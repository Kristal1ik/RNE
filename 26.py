import itertools

# with open("26_1") as f:
#     data = f.read().splitlines()
# n = data[0]
# data = data[1:]
# tusi = []
# for s in data:
#     start, end = list(map(int, s.split()))
#     tusi.append([end, start])
# tusi.sort()
# zal = 0  # зал освободится
# correct = []  # подошли
# break_ = []
# for tusa in tusi:
#     if tusa[1] >= zal:
#         correct.append(tusa)
#         zal = tusa[0] + 15
#     if len(correct) == 17 and tusa[1] >= zal:
#         break_.append(tusa[1] - zal + 15)
# print(len(correct))
# print(correct)
#
# f = open("26_2.txt")
# _ = f.readline()
# print(_)
# start = 1_633_046_400
# sec_in_week = 60 * 60 * 24 * 7
# end = start + sec_in_week
# data = []
# for line in f:
#     pair = list(map(int, line.split()))
#     if pair[0] == 0:
#         pair[0] = start
#     if pair[1] == 0:
#         pair[1] = end
#     pair[0] -= start
#     pair[1] -= start
#     if pair[0] > sec_in_week or pair[1] < 0:
#         continue
#     pair[0] = max(0, pair[0])
#     pair[1] = min(sec_in_week, pair[1])
#     data.append(pair)
# seconds = [0] * sec_in_week
# for item in data:
#     for i in range(item[0], item[1]):
#         seconds[i] += 1
# print(max(seconds), )

# f = open('26_2.txt')
# _ = f.readline()
# data = []
# s = 1_634_515_200
# sec = 60 * 60 * 7 * 24
# end = s + sec
# for line in f:
#     g = list(map(int, line.split()))
#     print(g)
#     if g[0] == 0:
#         g[0] = s
#     if g[1] == 0:
#         g[1] = end
#
#     g[0] -= s
#     g[1] -= s
#     if g[0] > sec or g[1] < 0:
#         continue
#     g[0] = max(0, g[0])
#     g[1] = min(sec, g[1])
#     data.append(g)
# # print(*data, sep='\n')
# seconds = [0] * sec
# h = 0
# for j in data:
#     for i in range(j[0], j[1]):
#         h += 1
#         seconds[i] += 1
# print(max(seconds))

f = open('26_3')
s, n = list(map(int, f.readline().split()))
data = []
for i in range(n):
    data.append(int(f.readline()))
data.sort()
count = 0
summa = 0
max_ = 0
for i in range(n):
    if data[i] + summa < s:
        count += 1
        summa += data[i]
        max_ = data[i]
    else:
        break
for i in range(n-1, 0, -1):
    if summa - max_ + data[i] < s:
        max_ = data[i]
        break
print(summa, max_)
