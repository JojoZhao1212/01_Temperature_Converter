"""" Converting  Celsius to Fahrenheit v1
Converting from degrees Celsius to Fahrenheit
Function takes in a value, does the conversion and puts answer into a list
"""


def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    return celsius


# Main Routine
temperatures = [32, 0, 40, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)

