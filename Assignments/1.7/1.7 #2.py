total = 1  # sets initial total, since its multiplication it cannot start at 0
userNum = int(input('Enter a number: '))  # takes the users input of a number
if userNum > 0:  # if the users number is positive,
    y = list(range(1,userNum+1))  # set the value of y to a positive list
elif userNum < 0:  # but if the users number is negative
    y = list(range(-1,userNum-1,-1))  # set the value of y to a negative list
for x in y:  # set x to the next number in the list y each time through the loop
    total = total * x  # multiply the total by the number from the list (x)
print(total)  # print the total