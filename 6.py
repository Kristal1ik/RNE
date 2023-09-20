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

s = set()
word = "парабола"
for w in itertools.permutations(word, r=8):
    w = "".join(w)
    w2 = w.replace("о", "а").replace("р", "п").replace("б", "п").replace("л", "п")
    if "пп" not in w2 and "аа" not in w2:
        s.add(w)
print(len(s))
print(s)
