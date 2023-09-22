import itertools

# s = set()
# word = "вава"
# for w in itertools.permutations(word, r=3):
#     s.add("".join(w))
# print(len(s))
# print(*s, sep="\n")
# print(help(itertools.permutations))

# s = set()
# word = "абвгд"
# for w in itertools.product(word, repeat=5):
#     w = "".join(w)
#     if w[0] != "а" and "аа" not in w and "бб" not in w and "вв" not in w and "гг" not in w and "дд" not in w:
#         s.add(w)
# print(len(s))
# print(s)

# s = set()
# n = 0
# word = "101101"
# for w in itertools.permutations(word, 4):
#     w = "".join(w)
#     if "11" not in w and "00" not in w:
#         s.add(w)
#         n += 1
# print(n)

# s = set()
# word = "росомаха"
# for w in itertools.permutations(word, r=8):
#     w = "".join(w)
#
#     if "11" not in w and "оо" not in w and "00" not in w:
#         s.add(w)
# print(len(s))
# print(s)

# s = set()
# word = "андрей"
# for w in itertools.product(word, repeat=7):
#     w = "".join(w)
#     if w[0] != "й" and w.count("й" ) == 1 and w.count("а") == 1:
#         s.add(w)
# print(len(s))
# print(s)

# s = set()
# word = "тимофей"
# for w in itertools.product(word, repeat=5):
#     w = "".join(w)
#     if w.count("т") >= 1 and w.count("й") <=1:
#         s.add(w)
# print(len(s))
# print(s)

# s = set()
# word = "парабола"
# for w in itertools.permutations(word, r=8):
#     w = "".join(w)
#     w2 = w.replace("о", "а").replace("р", "п").replace("б", "п").replace("л", "п")
#     if "пп" not in w2 and "аа" not in w2:
#         s.add(w)
# print(len(s))
# print(s)

# s = set()
# word = "01234567"
# for w in itertools.product(word, repeat=5):
#     w = "".join(w)
#     w2 = w.replace("2", "0").replace("3", "1").replace("4", "0").replace("5", "1").replace("6", "0").replace("7", "1")
#     if "1" not in w and "11" not in w2 and "00" not in w2 and w[0] != "0":
#         i2 = set(w)
#         if len(w) == len(i2):
#             s.add(w)
# print(len(s))
# print(s)
import math

s = set()
word = sorted("алгоритм")
n = 1
for w in itertools.product(word, repeat=5):
    w = "".join(w)
    if w[0] != "г" and w.count("и") >= 2 and n % 2 != 0:
        s.add(w)
    n += 1
print(len(s))
