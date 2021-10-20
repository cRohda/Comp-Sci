phrase = list(input('Enter a word or sentence: '))  # Gets the users input of a sentence
output = ""  # Creates the variable output, and makes it a empty string
# creates a range with the length of the user's phrase
for i in range(len(phrase)):  # Loops through assigning i to each num in this range
    if i % 2 == 0:  # if the number of i (index of list) is evenly divisible by 2
        print(phrase[i])  # print the character who's index is divisible by 2

# **Do it in 2 lines?**
# phrase = input('Enter a word or sentence: ')
# print(phrase[::2])
