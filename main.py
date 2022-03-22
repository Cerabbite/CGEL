import random


possible_consonants = ['m', 'n', 'p', 't', 'k', 's', 'w', 'l', 'j']
possible_vowels = ['i', 'u', 'e', 'o', 'a']

def generate_words(possible_consonants, possible_vowels):
    words = []
    syllable_order = ''
    word_length = random.randint(3, 10)
    for i in range(word_length):
        if random.randint(0, 10) < 5:
            syllable_order += "V"
        else:
            syllable_order += "C"

    for i in range(random.randint(100, 1000)):
        word = ''
        for y in range(word_length):
            print(syllable_order[y])
            if syllable_order[y] == "C":
                word += random.choice(possible_consonants)
            else:
                word += random.choice(possible_vowels)

        words.append(word)

    return words, syllable_order

def algorithm(possible_consonants, possible_vowels):
    gen = 0
    while True:
        words, syllable_order = generate_words(possible_consonants, possible_consonants)
        score = 0

        if score >= 5000:
            break
        elif gen >= 1000:
            break

        gen += 1

    print(words)
    print(syllable_order)


algorithm(possible_consonants, possible_vowels)
