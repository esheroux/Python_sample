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
"First record of texts, <incoming number> texts <answering number> at time
<time>"
"Last record of calls, <incoming number> calls <answering number> at time
<time>, lasting <during> seconds"
"""
first_text = texts[0]
tx_out_num, tx_in_num, tx_time = first_text
print("First record of texts, {} texts {} at time {}".format(tx_out_num,
      tx_in_num, tx_time))

last_call = calls[-1]
cl_out_num, cl_in_num, cl_time, cl_during = last_call
print("Last record of calls, {} calls {} at time {}, lasting {} seconds"
      .format(cl_out_num, cl_in_num, cl_time, cl_during))
