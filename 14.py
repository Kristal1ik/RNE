def f_ss(n, ss):
    s = ""
    while n > 0:
        ost = n % ss
        s += str(ost)
        n = n // ss
    return s[::-1]


#
#
# for x in range(8):
#     for y in range(7):
#         one = int(f"{x}01{y}4", 9)
#         two = int(f"{x}{y}544", 8)
#         if (one + two) % 89 == 0:
#             print(int(one + two) // 89)

# print(str(bin(4 ** 2020 + 2 ** 2017 - 15)).count("1"))


# for x in range(12):
#     for y in range(17):
#         one = int(f"2AB{x}", 12)
#         two = int(f"{x}8E", 17)
#         if (one + two) % 27 == 0:
#             print(int(one + two) // 27)

# for x in range(22):
#     one = int(f"63{x}59685", 22)
#     two = int(f"17{x}53", 22)
#     three = int(f"36{x}5", 22)
#     if (one + two + three) % 21 == 0:
#         print(int(one + two) // 21)

# n = f_ss(3 * 343 ** 8 + 5 * 49 ** 12 + 7 ** 15 - 49, 7)
# print(n)


# for a in range(100):
#     if all(x & 29 == 0 or (x & 17 != 0 or x & a) for x in range(100)):
#         print(a)

# for i in range(7, 36):
#     if int("12", i) * int("33", i) == int("406", i):
#         print(i)
#     else:
#         print("sd")


print("бесит все")



