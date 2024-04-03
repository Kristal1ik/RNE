# with open("27A_2") as file:
#     data = file.read().splitlines()
# data = data[1:]
# lst = []
# max_sum = 0
#
# for i in data:
#     i = list(map(int, i.split()))
#     max_sum += max(i)
# else:
#     sum_now = 0
#     for i in range(len(data)):
#         i = list(map(int, data[i].split()))
#         sum_now_now = max_sum - max(i) + min(i)
#         if sum_now_now % 5 != 0:
#             sum_now = max(sum_now_now, sum_now)
#     print(sum_now)
import itertools
import math

# import itertools
#
# with open("27А_1.txt") as file:
#     n = int(*file.readline().split())
#     lines = file.read().splitlines()[1:]
#     data = []
#     for line in lines:
#         data.append(list(map(int, line.split())))
#
# print(n)
# print(data)
# mx_sm = 0
#
#
# def chet_check(lst):
#     n_chet = 0
#     for i in lst:
#         if int(i) % 2 == 0:
#             n_chet += 1
#     if n_chet > len(lst) // 2:
#         return 0
#     return 1
#
#
# for prod in itertools.product("01", repeat=n):
#     sm = []
#     print(prod)
#     for j in range(n):
#         print(prod[int(j)])
#         print(data[j])
#         print(int(data[j][prod[int(j)]]))
#         sm.append(int(data[j][prod[int(j)]]))
#     print(sm)

# with open("27А_2.txt") as file:
#     n = int(*file.readline().split())
#     lines = file.read().splitlines()
#     data = []
#     for line in lines:
#         data.append(list(map(int, line.split())))
# mn_sm = math.inf
# for i in itertools.product("01", repeat=n):
#     sm = 0
#     for j in range(n):
#         sm += data[j][int(i[j])]
#     if mn_sm > sm and sm % 3 == 0:
#         mn_sm = sm
#
# print(mn_sm)

with open("27A_3.txt") as file:
    n = int(*file.readline().split())
    lines = file.read().splitlines()
    data = []
    for line in lines:
        data.append(list(map(int, line.split())))
new_data = []
for i in range(n):
    if int(data[i][0]) % 2 != 0:
        new_data.append(list(map(int, data[i])))
sm_max = 0
for i in itertools.product("01", repeat=n):
    sm_big = 0
    sm_small = 0
    sm_ans = 0
    for j in range(len(new_data)):
        if i[j] == "1":
            sm_big += max(new_data[j])
            sm_small += min(new_data[j])
        sm_ans += sm_big + sm_small
    if sm_ans > sm_max:
        sm_max = sm_ans
print(sm_max)

