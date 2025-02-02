# create a mad lib game using python

# import the random module
import random

# create a list of words
nouns = ['apple', 'banana', 'car', 'dog', 'elephant', 'fish', 'giraffe', 'house', 'igloo', 'jacket', 'kite']
verbs = ['ate', 'bought', 'caught', 'danced', 'eats', 'flew', 'grew', 'hopped', 'is', 'jumps', 'kicked']
adjectives = ['angry', 'big', 'clumsy', 'dusty', 'excited', 'furry', 'green', 'happy']
adverbs = ['awkwardly', 'bravely', 'cheerfully', 'daintily', 'eagerly', 'fondly', 'gracefully']

# create a madlib template
madlib = f"""Once upon a time, there was a {random.choice(adjectives)} {random.choice(nouns)} who loved to {random.choice(verbs)}.
One day, they decided to {random.choice(verbs)} to the {random.choice(nouns)}.
When they arrived, they saw a {random.choice(adjectives)} {random.choice(nouns)}.
The {random.choice(nouns)} was {random.choice(adverbs)} {random.choice(verbs)}.
The {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)}.
The {random.choice(nouns)} and the {random.choice(nouns)} lived happily ever after."""

# print the madlib
print(madlib)
