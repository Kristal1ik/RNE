import itertools

# # itertools without walls
# lines = """51	21	93	48	45	100	67	39	18	29
# 57	43	97	51	92	10	93	32	19	58
# 63	16	31	16	78	88	90	72	37	67
# 10	57	64	25	96	50	81	65	91	69
# 99	43	95	7	40	76	18	34	5	65
# 35	19	71	77	64	38	62	56	10	2
# 100	57	27	26	51	33	100	11	53	1
# 11	79	49	46	37	69	80	31	25	39
# 22	71	20	23	11	12	39	16	64	34
# 4	25	87	84	30	48	77	13	40	33
# """
# matrix = [[int(y) for y in x.split()] for x in lines.splitlines()]
# min_s, max_s = None, None
# for path in itertools.product([0, 1], repeat=len(matrix) + len(matrix[0]) - 2):
#     if path.count(0) != len(matrix[0]) - 1:
#         continue
#     if path.count(1) != len(matrix) - 1:
#         continue
#     x, y = 0, 0
#     s = matrix[x][y]
#     for item in path:
#         if item == 0:
#             x += 1
#         else:
#             y += 1
#         s += matrix[x][y]
#     if max_s is None or s > max_s:
#         max_s = s
#     if min_s is None or s < min_s:
#         min_s = s
# print(max_s, min_s)
#


# 0, 9
# lines = '''23	96	3	62	59	10	73	30	10	81
# 44	3	99	88	53	90	42	39	36	98
# 39	32	5	8	34	9	39	95	36	41
# 33	79	22	99	29	61	65	48	70	77
# 73	49	40	39	16	49	68	37	60	10
# 98	65	67	11	14	39	74	29	70	81
# 29	90	63	44	5	4	5	28	22	94
# 88	100	15	75	42	68	50	8	98	55
# 38	21	77	25	91	92	64	72	16	67
# 65	93	45	52	51	19	96	45	7	39
# '''
# matrix = [[int(y) for y in x.split()] for x in lines.splitlines()]
# min_s, max_s = None, None
# for path in itertools.product([0, 1], repeat=len(matrix) + len(matrix[0]) - 2):
#     if path.count(0) != len(matrix[0]) - 1:
#         continue
#     if path.count(1) != len(matrix) - 1:
#         continue
#     x, y = 0, 9
#     s = matrix[x][y]
#     for item in path:
#         if item == 0:
#             x += 1
#         else:
#             y -= 1
#         s += matrix[x][y]
#     if max_s is None or s > max_s:
#         max_s = s
#     if min_s is None or s < min_s:
#         min_s = s
# print(max_s, min_s)


# Жадный (неправильный ответ)
# lines = """1  8  8  4
# 10  1  1  3
# 1  3  12  2
# 2  3  5  6"""
# matrix = [[int(y) for y in x.split()] for x in lines.splitlines()]
# x, y = 0, 0
# s = matrix[x][y]
# for i in range(len(matrix) - 1 + len(matrix[0]) - 1):
#     if y + 1 == len(matrix[0]):
#         left = 2 ** 32
#     else:
#         left = matrix[x][y + 1]
#     if x + 1 == len(matrix):
#         bottom = 2 ** 32
#     else:
#         bottom = matrix[x + 1][y]
#     if left < bottom:
#         y += 1
#         s += left
#     else:
#         x += 1
#         s += bottom
# print(s)

lines = '''23	96	3	62	59	10	73	30	10	81
44	3	99	88	53	90	42	39	36	98
39	32	5	8	34	9	39	95	36	41
33	79	22	99	29	61	65	48	70	77
73	49	40	39	16	49	68	37	60	10
98	65	67	11	14	39	74	29	70	81
29	90	63	44	5	4	5	28	22	94
88	100	15	75	42	68	50	8	98	55
38	21	77	25	91	92	64	72	16	67
65	93	45	52	51	19	96	45	7	39
'''

matrix = [[int(y) for y in x.split()] for x in lines.splitlines()]

max_sum = -2**32
min_sum = 2**32
for path in itertools.product([0, 1], repeat=len(matrix) + len(matrix[0]) - 2):
    if path.count(0) == path.count(1):
        x, y = len(matrix) - 1, 0
        sum_ = matrix[x][y]
        for i in path:
            if i == 0:
                y += 1
            elif i == 1:
                x -= 1
            sum_ += matrix[x][y]
        if sum_ > max_sum:
            max_sum = sum_
        if sum_ < min_sum:
            min_sum = sum_

print(max_sum, min_sum)