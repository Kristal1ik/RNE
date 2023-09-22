# 1
# n = int("11011001", 2)
# for i in range(2**7, 2**9):
#     nn = n
#     for j in range(127):
#         nn = nn ^ int(i)
#         if nn == int("1100011", 2):
#             print(i)
# print(bin(186))

# 2
# n = 41
# m = 57
# r = 0
# while n != m:
#     if n != m:
#         if n < m:
#             n += 3
#         else:
#             m += 7
#         r += 1
# print(r)

#3
# n=0
# for i in range(1, 65):
#     for j in range(1, 65):
#         x = 2**i - 1
#         y = 2**j - 1
#         proizv = bin(x*y)[2:]
#         if (x>y) and ("0" in proizv) and ("1" in proizv) and (abs(proizv.count("1") - proizv.count("0"))<=13):
#             n+= 1
#
# print(n)

#4
# n = int(input())
# index = 0
# nn = 0
# numbers = list(map(int, input().split()))
# numbers_ind = [i for a, i in sorted(zip(numbers, [j for j in range(n)]))]
#
# for i in numbers_ind:
#     if index <= i:
#         nn += abs(index - i)
#         index = i
#     else:
#         nn += n-index+i
#         index = i
# print(nn)
#

#5
n = int(input())
summ = 0

lst = [0] * 501
for i in range(n):
    s = list(map(int, input().split()))
    lst[s[0]], lst[s[1]] = lst[s[0]] - s[2], lst[s[1]]+s[2]
    if lst[s[0]] <0:
        summ-=lst[s[0]]
        lst[s[0]] = 0
print(abs(summ))

