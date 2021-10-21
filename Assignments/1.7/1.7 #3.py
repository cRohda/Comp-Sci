phrase = list(input('Enter a word or sentence: '))  # Gets the users input of a sentence
output = ""  # Creates the variable output, and makes it a empty string
counter = 0  # Creates a variable to count the number of times through the loop
# creates a range with the length of the user's phrase
for i in phrase:  # Loops through assigning i to each num in this range
    if counter % 2 == 0:  # if the number of counter is evenly divisible by 2
        print(i) # print the character
    counter += 1  # adds one to counter

# **Do it in 2 lines?**
# phrase = input('Enter a word or sentence: ')
# print(phrase[::2])
