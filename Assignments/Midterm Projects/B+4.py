list1 = [15, -1, 11, -5, -5, 5, 3, -1, -7, 13, -11, -11, 7, 13]  # Base list
even_list = []  # Creates blank list

# Problem 3 code
for i in list1:  # Iterates through list1 assigning i to the next value each time through
    if i % 2 == 0:  # If 'i' is divisible by 2 (even) then:
        even_list.append(i)  # Add the value of 'i' to a new list 'even_list'
print(even_list)  # Print the value of 'even_list'

# New code
smallest = even_list[0]  # Set smallest variable to the 0 index of even_list
for x in even_list:  # Iterates through even_list assigning 'x' to the next value each time through
    if x < smallest:  # if 'x' is less than the current value of 'smallest'
        smallest = x  # re-assign 'smallest' to the value of x, as x is smaller
    else:  # else if 'x' is not less than smallest
        pass  # do nothing

print(smallest)  # finally, print the value of smallest
