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
f = open("26_2.txt")
_ = f.readline()
print(_)
start = 1_633_046_400
sec_in_week = 60 * 60 * 24 * 7
end = start + sec_in_week
data = []
for line in f:
    pair = list(map(int, line.split()))
    if pair[0] == 0:
        pair[0] = start
    if pair[1] == 0:
        pair[1] = end
    pair[0] -= start
    pair[1] -= start
    if pair[0] > sec_in_week or pair[1] < 0:
        continue
    pair[0] = max(0, pair[0])
    pair[1] = min(sec_in_week, pair[1])
    data.append(pair)
seconds = [0] * sec_in_week
for item in data:
    for i in range(item[0], item[1]):
        seconds[i] += 1
print(max(seconds), )
