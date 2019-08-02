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
The list of numbers should be print out one per line in lexicographic order
with no duplicates.
"""

tele_num = []
tx_out_nums, tx_in_nums, tx_times = zip(*texts)
cl_out_nums, cl_in_nums, cl_times, cl_during = zip(*calls)

for cl_out_num in cl_out_nums:
    if cl_out_num not in cl_in_nums and cl_out_num not in tx_out_nums \
       and cl_out_num not in tx_in_nums:
        tele_num.append(cl_out_num)

print("These numbers could be telemarketers:\n{}"
      .format("\n".join(sorted(set(tele_num)))))
