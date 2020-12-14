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

#prepare caller dict and receiver dict
callers_dict = {}
receivers_dict = {}

for line in range(0, len(calls)):
    if callers_dict.get(calls[line][0])==None:
        callers_dict[calls[line][0]] = 1
    else:
        pass
    if receivers_dict.get(calls[line][1])==None:
        receivers_dict[calls[line][1]] = 1
    else:
        pass

#prepare message sender and receiver dict
sender_dict = {}
text_receivers_dict = {}

for line in range(0, len(texts)):
    if sender_dict.get(texts[line][0])==None:
        sender_dict[texts[line][0]] = 1
    else:
        pass
    if text_receivers_dict.get(texts[line][1])==None:
        text_receivers_dict[texts[line][1]] = 1
    else:
        pass

telemarketers = []

sorted_callers = sorted(callers_dict.keys())

print("These numbers could be telemarketers: ")

for caller in sorted_callers:
    if (receivers_dict.get(caller) == None) & (sender_dict.get(caller) == None) & (text_receivers_dict.get(caller) == None):
        print(caller)
