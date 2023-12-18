with open("24 (1).txt") as file:
    data = file.readline()
n = 1
now = 1


for i in range(1, len(data)):
    if data[i-1] not in "ABC" or data[i] not in "ABC":
        now += 1
    else:
        n = max(n, now)
        now = 1
print(n)
