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
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

max_number = calls[0][0]
max_duration = int(calls[0][3])
time_spent = {calls[0][0]: int(calls[0][3]), calls[0][1]: int(calls[0][3])}

def update_dict(number, duration):
    """
    Function to update time_spent dict with number as key and duration as value

    parameters:
    number (string): number in question
    duration (string): duration of the call made

    """
    if number in time_spent:
        time_spent[number] = int(time_spent[number]) + int(duration)
    else:
        time_spent[number] = int(duration)

def check_max(max_number, max_duration, number, duration):
    """
    Function to check re-evaluate and return current maximum duration and the associated number

    parameters:
    max_number (string): current mnumber with max duration
    max_duration (int): max duration
    number (string): number in question
    duration (string): duratioon of the number

    returns: Updated max number and max duration
    max_number, max_duration
    """
    if int(duration) > max_duration:
        return number, int(duration)
    else:
        return max_number, max_duration

for line in range(1, len(calls)):
    update_dict(calls[line][0], calls[line][3])
    max_number, max_duration = check_max(max_number, max_duration, calls[line][0], time_spent[calls[line][0]])
    update_dict(calls[line][1], calls[line][3])
    max_number, max_duration = check_max(max_number, max_duration, calls[line][1], time_spent[calls[line][1]])


print(f"{max_number} spent the longest time, {max_duration} seconds, on the phone during September 2016.")
