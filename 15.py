

# for A in range(300):
#     n = 0
#     for x in range(300):
#         if ((x & 42 != 0) or (x & 13 != 0)) <= ((x & 30 == 0) <= (x & A != 0)):
#             n += 1
#     if n == 300:
#         print(A)


p = [i for i in range(3, 39)]
q = [i for i in range(21, 58)]
A = []
mx_len = 0
for a1 in range(100):
    for a2 in range(a1, 100):
        n = 0
        for x in range(100):
            if ((x in q) <= (x in p)) <= (not (a1 <= x <= a2)):
                n += 1
        if n == 100:
            mx_len = max(mx_len, a2-a1+1)
print(mx_len)
