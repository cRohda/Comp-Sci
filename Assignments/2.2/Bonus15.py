inp = input('Enter a sentence: ')  # Gets users input

old = 'abcdefghijklmnopqrstuvwxyz'  # Lists for indexing if character is lower case
new = 'zyxwvutsrqponmlkjihgfedcba'

oldcaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Lists for indexing if character is uppercase
newcaps = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

for i in inp:  # Iterate through code for each character in the input
    if i.isupper():  # if the character is uppercase, run the code with the uppercase lists
        index = oldcaps.index(i)  # Gets the index from the first list
        print(newcaps[index], end='')  # Prints that index in the 2nd list, the opposites, and doesn't start a new line
    elif i.islower():  # elif, the character is lowercase, run the code with lowercase lists
        index = old.index(i)  # Gets the index from the first list
        print(new[index], end='')  # Prints that index in the 2nd list, the opposites, and doesn't start a new line
    else:  # Else, it must be a special character, or space
        print(i, end='')  # So change nothing, print the character and don't start a new line.