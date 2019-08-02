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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_numbers = []

for out_num, in_num, time_stamp in texts:
    phone_numbers.append(out_num)
    phone_numbers.append(in_num)

for out_num, in_num, time_stamp, time in calls:
    phone_numbers.append(out_num)
    phone_numbers.append(in_num)

print("There are {} different telephone numbers in the records."
      .format(len(set(phone_numbers))))
