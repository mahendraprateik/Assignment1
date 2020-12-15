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
print("First record of texts, {sender} texts {receiver} at time {timestamp}".format(sender=texts[0][0], receiver=texts[0][1], timestamp=texts[0][2]))
print("Last record of calls, {caller} calls {receiver} at time {timestamp}, lasting {duration} seconds".format(caller=calls[-1][0], receiver=calls[-1][1], timestamp=calls[-1][2],duration=calls[-1][3]))
