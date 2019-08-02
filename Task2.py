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
"<telephone number> spent the longest time, <total time> seconds, on the phone
during September 2016.".
"""
call_log = {}

for out_num, in_num, time_stamp, call_time in calls:
    if out_num not in call_log:
        call_log[out_num] = int(call_time)
    elif out_num in call_log:
        call_log[out_num] += int(call_time)
    if in_num not in call_log:
        call_log[in_num] = int(call_time)
    elif in_num in call_log:
        call_log[in_num] += int(call_time)

max = max(call_log.values())
result = list(filter(lambda x: x[1] == max, call_log.items()))
number = result[0]

print("{} spent the longest time, {} seconds, on the phone during September \
      2016.".format(number[0], max))
