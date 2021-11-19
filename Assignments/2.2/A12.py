inp = input('Enter a word or phrase: ')  # Gets the users input of a phrase
ph1 = inp[:1]  # Makes a place holder variable of the first character
ph2 = inp[-1:-2:-1]  # Makes a place holder variable of the last character

# Makes a variable that is the last character (ph2) + the middle characters + the last character (ph1)
swap = ph2 + inp[1:-1] + ph1
print(swap)  # Prints the final variable