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
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
import re

def get_recepient_codes(area_code):
  """
  parameters
  area_code (string): area code of the caller. eg: (080) for Bangalore

  Returns:
  area codes/prefixes called by given area code
  """

receiver_dict = {}

for line in range(0, len(calls)):
  if "(080)" in calls[line][0]:
    if "(" in calls[line][1]:
      fixed_area_code = re.search('\((.+?)\)', calls[line][1]).group(1)
      if receiver_dict.get(fixed_area_code)==None:
        receiver_dict[fixed_area_code] = 1
      else:
        receiver_dict[fixed_area_code] += 1
    elif " " in calls[line][1]:
      if receiver_dict.get(calls[line][1][0:4])==None:
        receiver_dict[calls[line][1][0:4]] = 1
      else:
        receiver_dict[calls[line][1][0:4]] += 1
    else:
      if receiver_dict.get("140")==None:
        receiver_dict["140"] = 1
      else:
        receiver_dict["140"] += 1
  else:
    continue

total_calls = 0
calls_to_bangalore = receiver_dict['080']

sorted_receivers = sorted(receiver_dict.keys())

print(f"The numbers called by people in Bangalore have codes:")

for r in sorted_receivers:
  total_calls = total_calls + receiver_dict[r]
  print(r)


print(f"{round(calls_to_bangalore*100/total_calls, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
