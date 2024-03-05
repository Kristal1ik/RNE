# with open('9.txt') as f:
#     data = f.read().splitlines()
# n = 0
# for i in data:
#     i = list(map(int, i.split("\t")))
#     if len(i) == len(set(i)) and (((max(i) + min(i)) / 2) < (sum(i) / len(i))):
#         n += 1
# print(n)

data = [1,2,2]
sums = {}
for element in data:
    sums[element] = data.count(element) * element
print(sums)