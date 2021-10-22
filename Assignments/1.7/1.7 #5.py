user = input('Enter some characters: ')  # Gathers the characters for the list
letter = 0
integer = 0  # Creates variables for counting number of each type
Punct = 0
Blank = 0

# Lists to store the different types of characters, referenced for detecting each type
PunctList = ['!', ',', '?', '.', "'", ':', ';']
IntList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
AlphList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for x in user:  # Loops through each character in the input and tries the bellow code
    if x in AlphList:  # If the character being tested is in AlphList
        letter += 1  # Then it is a letter, so it adds 1 to the letter count
    elif x in IntList:  # If the character is in IntList
        integer += 1  # Then it is a number, so it adds 1 to the number count
    elif x == ' ':  # If the character is a blank space
        Blank += 1  # Add one to blank
    elif x in PunctList:  # If the character is in PunctList
        Punct += 1  # It is punctuation, so add one to Punct
# Print the amount of each
print(f'letter: {letter}\nIntegers: {integer}\nPunctuation: {Punct}\nBlank: {Blank}')
