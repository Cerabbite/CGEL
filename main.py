import random

# What will a humand decide?
#   Grammar tenses
#   Rough word length (between x and y)
#   Phonetics (For now later the algorithm might be able to choose his own phonetics)

# What does the algorithm need to solve?
#   The syllable_order
#   What words mean what


possible_consonants = ['m', 'n', 'p', 't', 'k', 's', 'w', 'l', 'j']
possible_vowels = ['i', 'u', 'e', 'o', 'a']


def check():
    return int(input("How readable is this word? (The higher the score the better) You can use http://ipa-reader.xyz/ as an helper. "))

def generate_word(syllable_order):
    possible_consonants = ['m', 'n', 'p', 't', 'k', 's', 'w', 'l', 'j']
    possible_vowels = ['i', 'u', 'e', 'o', 'a']
    word = []
    for g in range(5):
        if syllable_order[g] == "V":
            word.append(random.choice(possible_vowels))
        else:
            word.append(random.choice(possible_consonants))

    l_word = ""
    for i in word:
        l_word += i

    print(l_word)

def fitness(syllable_order):
    generate_word(syllable_order)
    ans = check()

    if ans == 100:
        return 0
    else:
        if ans == 0:
            ans += 1
        return abs(1/ans)


#syllable_order = ''
word_length = 5
solutions = []

population = 20
for i in range(population):
    syllable_order = ''
    for i in range(word_length):
        if random.random() < .5:
            syllable_order += "V"
        else:
            syllable_order += "C"

    solutions.append(syllable_order)

max_generations = 1000

for i in range(max_generations):
    rankedSolutions = []

    for y in solutions:
        rankedSolutions.append((fitness(y), y))

    rankedSolutions.sort()

    print(f"======== Generation {i} ========")
    print(f"Best solution: {rankedSolutions[0]}")

    bestSolutions = rankedSolutions[:10]


    for s in bestSolutions:
        for i in range(word_length):
            if random.random() > random.uniform(0.71, 0.95):
                if s[i] == "V":
                    s[i] == "C"
                else:
                    s[i] == "V"

        newGen.append(s)

    solutions = newGen
