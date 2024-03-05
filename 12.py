def f(s):
    while '12' in s or '5522' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '55', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '5522' in s:
            s = s.replace('5522', '21', 1)
    return s

for n in range(3, 10000):
    s = '1' + '2' * n
    r = f(s)
    summ = sum([int(i) for i in r])
    if summ == 142:
        print(n, s, r)
        break

# def algo(s):
#     while '12' in s or '5522' in s or '2222' in s:
#         if '12' in s:
#             s = s.replace('12', '55', 1)
#         if '2222' in s:
#             s = s.replace('2222', '1', 1)
#         if '5522' in s:
#             s = s.replace('5522', '21', 1)
#     return s
#
#
# for n in range(3, 10000):
#     s = '1' + '2' * n
#     r = algo(s)
#     summ = sum([int(i) for i in r])
#     if summ == 142:
#         print(n, s, r)
#         break
