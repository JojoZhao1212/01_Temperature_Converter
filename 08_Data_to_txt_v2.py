# Data to be Outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# assume valid data for now.
filename = input("Enter a Filename (leave off the extension): ")

# add .txt to stuffix!
filename = filename + ".txt"

# Create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item + "\n")


# close file
f.close()
