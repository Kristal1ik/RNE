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

with open("9.csv") as f:
    data = f.read().splitlines()
n = 0
for i in data:
    line = list(map(int, i.split(";")))
    d = dict()
    for j in line:
        if j not in d.keys():
            d[j] = 1
        else:
            d[j] += 1
    f3 = False
    f1_count = 0
    f3_num = 0
    f1_sum = 0
    for k, v in d.items():
        if v == 3:
            f3 = True
            f3_num = k
        elif v == 1:
            f1_count += 1
            f1_sum += k
    if f3 and f1_count == 4 and f1_sum / 4 < f3_num:
        n += 1
print(n)
