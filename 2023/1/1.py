
with open("./input.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    number_string = ""
    for char in line:
        if char.isnumeric():
            number_string += char
    number_string = number_string[0] + number_string[-1]
    if number_string == "":
        number_string = "0"
    total += int(number_string)

print(total)
