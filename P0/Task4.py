"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Lets make some sets!
# calls_from
# calls_to

calls_from, calls_to, _, __ = zip(*calls)
texts_from, texts_to, _ = zip(*texts)

possible_telemarketers = set(calls_from) - set(calls_to) - set(texts_from) - set(texts_to)

for t in sorted(possible_telemarketers):
    print(t)
