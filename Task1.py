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
unique_tele_nums = set()

# Looping through texts list to read all numbers and append them to numbers
for call in calls:
    unique_tele_nums.add(call[0])
    unique_tele_nums.add(call[1])

# Looping through calls list to read all numbers and add them to numbers
for text in texts:
    unique_tele_nums.add(text[0])
    unique_tele_nums.add(text[1])

print("There are {length_of_numbers} different telephone numbers in the records.".format(length_of_numbers=len(unique_tele_nums)))
