# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x == (w or y)) or (w <= z) and (y <= w)):
#                     print(x, y, z, w)
#

print("x y z w f1 f2")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = int(((x == (not(y))) <= (y and not(z))) or (z and not(w)))
#                 if not f:
#                     print(x, y, z, w)
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = int((w == x) and (y <= z))
                F2 = int((w <= x) <= (y == z))
                print(x, y, z, w, F1, F2)

x y z w f1 f2


1 0 1 1 1 0
0 1 1 0 1 1
1 0 1 0 0 0



