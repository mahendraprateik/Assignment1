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
# initializing numbers variable
numbers = [(texts[0][0])]

# Looping through texts list to read all numbers and append them to numbers
for line in range(1, len(texts)):
    if texts[line][0] not in numbers:
        numbers.append(texts[line][0])
    if texts[line][1] not in numbers:
        numbers.append(texts[line][1])

# Looping through calls list to read all numbers and add them to numbers
for line in range(0, len(calls)):
    if calls[line][0] not in numbers:
        numbers.append(calls[line][0])
    if calls[line][1] not in numbers:
        numbers.append(calls[line][1])

print(f"There are {len(numbers)} different telephone numbers in the records.")
