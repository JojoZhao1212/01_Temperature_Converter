# includes RegEx to check filename is valid (A-Z a-z 0-9 and underscores)

import re

# Data to be Outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# assume valid data for now.
filename = input("Enter a Filename (leave off the extension): ")

valid_file = "[A-Zaz"
if re.match(valid_file, filename):
    # add .txt to stuffix!
    filename = filename + ".txt"

    # Create file to hold data
    f = open(filename, "w+")

    for item in data:
        f.write(item + "\n")

    # close file
    f.close()

else:
    print("Oops!")
