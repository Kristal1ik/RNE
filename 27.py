with open("27A_2") as file:
    data = file.read().splitlines()
data = data[1:]
lst = []
max_sum = 0

for i in data:
    i = list(map(int, i.split()))
    max_sum += max(i)
else:
    sum_now = 0
    for i in range(len(data)):
        i = list(map(int, data[i].split()))
        sum_now_now = max_sum - max(i) + min(i)
        if sum_now_now % 5 != 0:
            sum_now = max(sum_now_now, sum_now)
    print(sum_now)