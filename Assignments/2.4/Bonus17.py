list1 = ['a', 2, 4, 2, 'a', 8, 4, 9, 2, 'b']  # Creates base list
list2 = []  # Creates empty final list

for i in list1:  # Iterates through assigning i to each value in list1
    if i in list2:  # If the value of i can be found in list2:
        pass  # do nothing
    else:  # If the value of i cannot be found in list2 already
        list2.append(i)  # Add i to list2
print(list2)  # Print the new value of list2