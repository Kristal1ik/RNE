import itertools
#
# n = 0
# mn = []
# for i in itertools.product("ольга", repeat=5):
#     data = ''.join(i)
#     n += 1
#     mn.append(data)
# mn = sorted(mn)
# print(mn.index("ольга") + 1)


# n = 1
# ans = 0
# mn = []
# for i in itertools.product("реплика",repeat=6):
#     data = ''.join(i)
#     if n % 2 == 0 and data[0] != "к" and data.count("и") > 1:
#         ans += 1
#     n += 1
# print(ans)

#
import itertools

lst = ["00", "11", "22", "33", "44", "55", "66", "77", '01', '10', '03', '30', '05', '50', '07', '70', '21', '12', '23', '32', '25', '52', '27', '72', '41', '14', '43', '34', '45', '54', '47', '74', '61', '16', '63', '36', '65', '56', '67', '76']
n = 0
for i in itertools.permutations("01234567", r=5):
    item = int("".join(i))
    if len(str(item)) == 5 and "1" not in str(item):
        print(item)

        item = str(item).replace("0", "2").replace("4", "2").replace("6", "2")
        item = str(item).replace("3", "1").replace("5", "1").replace("7", "1")
        if "11" not in item and "22" not in item:
            n += 1
print(n)



# for i in range(0, 8, 2):
#     for j in range(1, 8, 2):
#         lst.append(str(i) + str(j))
#         lst.append(str(j) + str(i))
# print(lst)
