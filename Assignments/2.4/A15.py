list1 = [2, 0, -6, 10, 5, 7]  # Creates initial list
list2 = []  # Creates empty list for final product

while len(list1) > 0:  # Loops as long as there are values in list1
    smallest = 10e99  # Sets variable smallest to a very large number
    for i in list1:  # iterates through the values remaining in list1, assinging i to each one
        if i < smallest:  # if i is less than smallest:

            # then i is the smallest number, this will go through every number to find the smallest number in the list
            smallest = i

    list2.append(smallest)  # add the next smallest number to the new list
    list1.remove(smallest)  # remove the smallest number from the original list
print(list2)  # finally, print the new list

