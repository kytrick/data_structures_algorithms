"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

from collections import defaultdict, Counter
d = defaultdict(lambda:0)

for c in calls:
    d[c[0]] += int(c[3])
    d[c[1]] += int(c[3])

call_totals = Counter(d)

print(str(call_totals.most_common(1)[0][0]) + " spent the longest time, " + str(call_totals.most_common(1)[0][1]) + " seconds, on the phone during September 2016.")
