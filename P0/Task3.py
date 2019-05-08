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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import string
import re
from collections import defaultdict

# part A
# limit search to only those calls originating from bangalore fixed lines
bangalore_area_code = '080'
bangalore_recipients = [i[1] for i in calls if str(i[0]).startswith('(080)')]

# create regexs to match the types of phone numbers in the exercise
fixed_regex = re.compile(r'^\((0\d*)\)')
mobile_regex = re.compile(r'^([7-9]\d{3})\d*\s\d+')
telemarketer_regex = re.compile(r'^140\d*')

# build lists of each type of phone number
fixed_recipients = list(filter(fixed_regex.match, bangalore_recipients))
mobile_recipients = list(filter(mobile_regex.match, bangalore_recipients))
telemarketer_recipients = list(filter(telemarketer_regex.match, bangalore_recipients))

# build dictionary
area_codes = defaultdict(lambda:0)
for f in bangalore_recipients:
    m = re.match(fixed_regex, f)
    if m:
        area_codes[m.group(1)] += 1
    m = re.match(mobile_regex, f)
    if m:
        area_codes[m.group(1)] += 1

codes = sorted(area_codes.keys())
print("The numbers called by people in Bangalore have codes: ")
for c in codes:
    print(c)

# part B
# split bangalore recipients into 2 groups:  also in bangalore, and everyone else

fixed_line_to_fixed_line = [i for i in bangalore_recipients if i.startswith('(080)')]

percentage = 100 * len(fixed_line_to_fixed_line)/len(bangalore_recipients)

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore. ".format(percentage))
