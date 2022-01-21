list1 = [15, -2, 10, -5, -4, 6, 3, -1, -8, 13, -12, -11, 7, 14]  # Base list
even_list = []  # Creates blank list

for i in list1:  # Iterates through list1 assigning i to the next value each time through
    if i % 2 == 0:  # If 'i' is divisible by 2 (even) then:
        even_list.append(i)  # Add the value of 'i' to a new list 'even_list'
print(even_list)  # Print the value of 'even_list'
