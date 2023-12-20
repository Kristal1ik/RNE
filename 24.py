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
with open("24") as file:
    data = file.readline()
n = 1
max_n = 0
for i in range(1, len(data)):
    if data[i] != data[i - 1]:
        n += 1
    else:
        max_n = max(n, max_n)
        n = 1
max_n = max(n, max_n)
print(max_n)