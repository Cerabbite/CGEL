import random

C = "M N P T K S W L J"
C = C.split(" ")
V = "A E I O U"
V = V.split(" ")
print(C)
print(V)

syllable_structure = ["CV", "VC", "CV", "CCV", "VCC", "CCVC", "CVCC", "CCVCC"]

amm_words = 1000

words = []

for g in range(len(syllable_structure)):
    i = syllable_structure[g]#random.choice(syllable_structure)
    for g in range(amm_words):
        word = ""
        for y in i:
            if y == "C":
                word += random.choice(C)
            elif y == "V":
                word += random.choice(V)
        if not word in words:
            print(word, i)
            words.append(word)
