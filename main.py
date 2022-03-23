import random

# What will a humand decide?
#   Grammar tenses
#   Rough word length (between x and y)
#   Phonetics (For now later the algorithm might be able to choose his own phonetics)

# What does the algorithm need to solve?
#   The syllable_order
#   What words mean what (Based upon the top 10.000 most used English words)
#   Pronouns

# The algorithm will generate between 1 and 500 different words and 1.000 sample sentences based upon the 1.000 most used sentences in English.



"""
Step 1: Create a gene that contains all the information for the syllalble order, exact word length, pronouns structure, grammar rules
Step 2: Generate the dictionary from the gene with 1 to 500 words
Step 3: Generate grammatically correct sentences from the 1 to 500 words and the sample sentences in English
Step 4: Give the text to a human and make it give feedback. The feedback will be a score between 0 and 100 for the syllable order, grammar rules, pronouns, readability etc
Step 5: Create a new language with the input of the human
Repeat step 1 to 5 upuntill the language is super easy to learn
"""

# The algorithm looks for synonyms and words that have roughly the same meaning to store in the same word

possible_consonants = ['m', 'n', 'p', 't', 'k', 's', 'w', 'l', 'j']
possible_vowels = ['i', 'u', 'e', 'o', 'a']

grammar_style = ['present', 'past', 'future']

word_length = [4, 10]
