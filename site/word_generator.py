import random

C = "M N P T K S W L J"
C = C.split(" ")
V = "A E I O U"
V = V.split(" ")
print(C)
print(V)

syllable_structure = ["CV", "VC", "CV", "CCV", "VCC", "CCVC", "CVCC", "CCVCC"]

amm_words = 100

for g in range(amm_words):
    for i in syllable_structure:
        word = ""
        for y in i:
            if y == "C":
                word += random.choice(C)
            elif y == "V":
                word += random.choice(V)

        print(word)
