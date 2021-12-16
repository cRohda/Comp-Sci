list1 = [-13, 4, -3, 15, 8]  # creates base list

for x in range(2):  # Iterates the code bellow twice
    smallest = 10e99  # Assigns smallest to a large number
    largest = -10e99  # Assigns largest to a very small number
    for i in list1:  # Iterates through the list assigning i to the next value
        if i < smallest:  # if i is smaller than the smallest:
            smallest = i  # then i is the smallest
        if i > largest:  # if i is larger than the largest
            largest = i  # then i is the largest
    list1.remove(smallest)  # remove the smallest value from the list
    list1.remove(largest)  # remove the largest value from the list
    # Loops one more time, and now that the smallest and largest are removed the new smallest and largest are
    # the 2nd largest and 2nd smallest


# Prints the sum of 2nd largest and 2nd smallest
print(f'The Sum of the 2nd smallest and 2nd largest is: {smallest + largest}')