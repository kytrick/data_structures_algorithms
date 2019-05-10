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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

import datetime

texts_datetime = []
for t in texts:
    datified = datetime.datetime.strptime(t[2], "%d-%m-%Y %H:%M:%S")
    texts_datetime.append([t[0], t[1], datified])

earliest_text = min(texts_datetime, key= lambda x:x[2])

print("First record of texts, " + str(earliest_text[0]) + " texts " + str(earliest_text[1]) + " at time " +  str(earliest_text[2]))

calls_datetime = []
for c in calls:
    datified = datetime.datetime.strptime(c[2], "%d-%m-%Y %H:%M:%S")
    calls_datetime.append([c[0], c[1], datified, c[3]])

latest_call = max(calls_datetime, key = lambda x:x[2])

print("Last record of calls, " + str(latest_call[0]) +  " calls " + str(latest_call[1]) + " at time " + str(latest_call[2]) + "lasting " + str(latest_call[3]) + " seconds")
