a = True  # Creates 2 true variables for loops
b = True

while a:  # While a is true, loop. Used to loop if there is less than 3 characters for input 1
    word1 = input('Enter a word 3 or more characters: ')  # Gets the users first word
    if len(word1) >= 3:  # If the word is 3 or more characters
        a = False  # set a to false, so it doesn't get the input again

        while b:  # While b is true, loop. Used to loop if there is less than 3 characters for input 2
            word2 = input('Enter another word over 3 characters: ')  # Gets the users 2nd word
            if len(word2) >= 3:  # If the word is more than 3 characters
                b = False  # Set b to false, so it doesn't loop again

                # Main code
                filler1 = word1[:2]  # Make a new variable, which is the first 2 characters of word1
                filler2 = word2[:2]  # Make a new variable, which is the first 2 characters of word2
                word1 = filler2 + word1[2:]  # Make word 1 the first 2 letters of word 2 + the rest of word 1
                word2 = filler1 + word2[2:]  # Make word 2 the first 2 letters of word 1 + the rest of word 1

                print(word1)  # Print new word1
                print(word2)  # Print new word2

            else:  # Else, if it is less than 3 characters, loop back through, and ask for a new 2nd input
                print('Your 2nd word was too short')  # And print that the word was too short

    else:  # Else, if it is less than 3 characters, loop back through again, and ask for a new input
        print('Your word was too short')  # And print that the word was too short