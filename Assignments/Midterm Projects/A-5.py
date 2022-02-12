list1 = [15, -2, 10, -5, -4, 6, 3, -1, -8, 13, -12, -11, 7, 14]  # Base list
even_list = []  # Creates blank list

# Problem 3 code

for i in list1:  # Iterates through list1 assigning i to the next value each time through
    if i % 2 == 0:  # If 'i' is divisible by 2 (even) then:
        even_list.append(i)  # Add the value of 'i' to a new list 'even_list'
print(even_list)  # Print the value of 'even_list'

# Using option 2

# New code
sorted_list = []  # Creates empty list 'sorted_list'

while len(even_list) > 0:  # Loops as long as there are values in even_list
    smallest = even_list[0]  # Sets variable smallest to the 0 index of even_list
    for i in even_list:  # iterates through the values remaining in even_list, assigning i to each one
        if i < smallest:  # if "i" is less than smallest:

            # then 'i' is the smallest number, this will go through every number to find the smallest number in the list
            smallest = i

    sorted_list.append(smallest)  # add the next smallest number to the new list
    even_list.remove(smallest)  # remove the smallest number from the original list

print(sorted_list)  # Print the sorted list
