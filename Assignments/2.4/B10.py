my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Creates base list
while True:  # Loops until broken, used to handle ValueError
    try:  # Try this code
        inp = int(input('Enter an integer to check if it is in the list: '))  # Takes users input and makes and int
        for i in my_list:  # loops trough assigning i to each value of my_list
            if inp == i:  # if i = the input:
                my_list[i] = 'found'  # replace i in the list with found (using indexing)
        print(my_list)  # print the new (or unchanged) value of the list
        break  # break the loop, this could be replaced with a counter to allow for multiple inputs
    except ValueError:  # If above code encounters value error:
        print('You did not enter an integer\n')  # Print that the user did not enter an int, and re start the loop