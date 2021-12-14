my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Creates list
for x in my_list:  # Iterates through each value of the list
    i = my_list.index(x)+1  # Assigns i to the index of the list +1. This makes sure 0 is printed last instead of first
    # Prints the next number, going backwards using negative index. Doesn't create a new line
    print(my_list[-i], end=' ')