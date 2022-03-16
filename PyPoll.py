import csv
dir(csv)

file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

        import os
        dir(os)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

Traceback (most recent call last):
  File "PyPoll.py", line 24, in <module>
    open(file_to_save, "w")


file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")
outfile.close ()
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

election_data = open(file_to_load, 'r')
file_reader = csv.reader(election_data)
for row in file_reader:
    print(row[0])

file_reader = csv.reader(election_data)
headers = next(file_reader)
print(headers)