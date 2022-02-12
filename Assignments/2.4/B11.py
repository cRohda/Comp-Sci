my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Creates base list

inp = int(input('Enter an integer to check if it is in the list: '))  # Gets user input and makes it an integer

if inp in my_list:  # checks if value of inp can be found in the list
    my_list[inp] = 'found'  # replaces the value of inp in the list with the str 'found'
else:  # if inp cannot be found in the list
    print('Not Found')  # print 'not found'
print(my_list)  # print the value of the list
