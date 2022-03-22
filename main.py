import random

# What does the algorithm need to solve?
#   The word length
#   The syllable_order
#   What words mean what
#   The grammar of the language


possible_consonants = ['m', 'n', 'p', 't', 'k', 's', 'w', 'l', 'j']
possible_vowels = ['i', 'u', 'e', 'o', 'a']


def check():
    return int(input("How readable is this word? (The higher the score the better) You can use http://ipa-reader.xyz/ as an helper. "))

def generate_word(syllable_order):
    for g in range(5):
        if syllable_order[g] == "V"

def fitness(syllable_order):
    generate_word(syllable_order)
    ans = check()

    if ans == 100:
        return 0
    else:
        return abs(1/ans)


#syllable_order = ''
word_length = 5
solutions = []
for i in range(1000):
    syllable_order = ''
    for i in range(word_length):
        if random.random() < .5:
            syllable_order += "V"
        else:
            syllable_order += "V"

    solutions.append(syllable_order)

max_generations = 1000

for i in range(max_generations):
    rankedSolutions = []

    for y in solutions:
        rankedSolutions.append(fitness())
