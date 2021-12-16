list1 = [[1, 2, 3], [4, 5, 6], [4, 5, 6]]  # base list
list1[2] = [7, 8, 9]  # Re-Assigns the last value in the list to a list of 7, 8, 9

for i in list1:  # Iterates through assigning i to each value (list) within list1
    for x in i:  # Iterates through assigning x to each value of i (the list within list1)
        print(x, end=' ')  # prints the number within the list
    print()  # prints a blank line after finishing each inner list