inp = input('Enter a list of words (SEPERATED BY COMMAS, WITH NO SPACES): ')  # Gets user input
inplist = inp.split(',')  # Splits the users input at the spaces
shortest = 10e99  # Creates shortest variable, and makes it very large number
SecondShortest = 10e99  # Creates 2nd shortest variable, and makes it a very large number
length = 0  # Creates length variable with value of 0

#  This code finds the shortest value by testing the length of each value in the list
for x in inplist:  # Iterates code making each value of inplist equal to x for each time through
    current = len(x)  # Creates current variable and sets it to the length of x

    if current <= shortest:  # if the current length is less than the shortest
        shortest = current  # The shortest is the current

# This code finds the 2nd shortest value, by the same method as above but also seeing if it is LONGER than the shortest
for y in inplist:  # Iterates code making each value of inplist equal to y each time through
    current = len(y)  # Sets current to the current length

    if current == length:  # If the current length is equal to the length of the 2nd shortest, then they are the same
        length = current  # So keep the length as current (should already be set but redundancy)
        word = f'a tie between {word} and {y}'  # Make word equal to the string, saying there is a tie

    # elif, current is shorter than the 2nd shortest, but longer than the shortest
    elif SecondShortest >= current > shortest:
        SecondShortest = current  # The 2nd shortest is the current length (for elif)
        length = current  # length = the current (for final print)
        word = y  # The word = the current word

print(f'The 2nd shortest word was "{word}" with "{length}" characters')  # prints the final results
