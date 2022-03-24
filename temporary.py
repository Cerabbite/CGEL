import nltk
from nltk.corpus import wordnet
from difflib import SequenceMatcher

word_a = "management"
word_b = "administration"

a = wordnet.synsets(word_a)
b = wordnet.synsets(word_b)

# maybe use this instead of difflib https://stackoverflow.com/questions/65199011/is-there-a-way-to-check-similarity-between-two-full-sentences-in-python
#ratio = SequenceMatcher(None, a[0].definition(), b[0].definition()).ratio()

#print(a)
#print(b)
#print(ratio)
#imp https://www.youtube.com/watch?v=zu9AcxfklrI

synonyms = []
for syn in wordnet.synsets(word_a):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)

synonyms = []
for syn in wordnet.synsets(word_b):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)
