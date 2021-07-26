
# Need to import the regular expression library re
import re

# Data to be outputted
data = ['I', 'love', 'computers']

# Get filename, can't be blank / invalid
# assume valid data for now.

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a Filename (leave off the extension): ")
    # Regular expression to check file name.Can be Upper or lower case letters,
    valid_char = "[A-Za-z0-9_]"  # number or underscores
    for letter in filename:
        if re.match(valid_char, letter):
            continue  # If the letter is valid, goes back and checks the next

        elif letter == " ":  # otherwise, find problem
            problem = "(no spaces allowed)"

        else:
            problem = ("{}s not allowed".format(letter))
        has_error = "yes"
        break

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":  # describe problem
        print("Invalid filename - {}".format(problem))
        print()
    else:
        print("You entered a valid filename")  # or allow valid file name

# add .txt to stuffix!
filename = filename + ".txt"

# Create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item + "\n")


# close file
f.close()
