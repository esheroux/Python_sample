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
The list of codes should be print out one per line in lexicographic order with
no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
area_codes = []
count_bangalore_out_num = 0
count_bangalore_in_num = 0
for out_num, in_num, time_stamp, time in calls:
    if out_num[:5] == "(080)":
        count_bangalore_out_num += 1
        if in_num[0] == "(":
            area_code, number = in_num.split(")")
            area_codes.append(area_code[1:])
            if in_num[:5] == "(080)":
                count_bangalore_in_num += 1
        elif in_num[0] == "7" or in_num[0] == "8" or in_num[0] == "9":
            area_codes.append(in_num[:4])
        elif in_num[:3] == "140":
            area_codes.append(in_num[0:3])

print("The numbers called by people in Bangalore have codes:\n{}".format("\n"
      .join(sorted(set(area_codes)))))

print("{} percent of calls from fixed lines in Bangalore are calls to other \
      fixed lines in Bangalore."
      .format(int((count_bangalore_in_num/count_bangalore_out_num)*100)))
