total = 0  # Creates variable to store total number of multiple
userNum = int(input('Enter a number: '))  # takes an input from the user for their number
four = range(1000,10000)  # creates a variable storing all the numbers between 1000-10000 (4 digit numbers)
for x in four:  # set x to the next value in the range {four} each time through the loop
    divisible = x % userNum  # store modulo of x % userNum
    if divisible == 0:  # if the modulo of above is 0,
        print(x)  # print the value of x (the multiple)
        total += 1  # then add one to the total number of multiples
    else:  # if it isn't 0
        pass  # do nothing
print(f'There are {total} 4 digit multiples')  # print the total multiples