range(10)  # stores the value of all numbers 0- 1 less than selected
range(2,8)  # stores the value of all numbers first to 1 less than that selected
range(2,18,2)  # stores the value of the first number - 1 less than the 2nd number, at the interval of the 3rd

# num1, starting number
# num2, number it will not pass (or reach, ends less than that number
# num3, the interval for counting up

for x in [1,2,4]:  # sets x to each of the values listed each time through
    print(x)  # prints the value of x each time through the loops
    if x == 4:
        break

my_list = [2,14.4, "ravens","y"]
for x in my_list:  # assigns x to each of of the referenced list
    print(x)
    if x == 'y':
        break

print("")  # adding a blank line so it looks nice :)

for i in "Go Red Sox!":  # assigns i to each of the CHARACTERS listed in the string
    print(i)
