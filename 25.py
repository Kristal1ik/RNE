def eval(n):
    lst = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            lst.append(i)
    return lst


lst_all = []
mx_len = 0
mx_n = 0
for i in range(120115, 120200 + 1):
    if mx_len <= len(eval(i)):
        mx_n = i
        mx_len = len(eval(i))
print(mx_len, mx_n)

