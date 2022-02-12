list1 = [15, -2, 10, -5, -4, 6, 3, -1, -8, 13, -12, -11, 7, 14]  # Base list

for i in list1:  # Iterates through list1 assigning i to the next value each time through
    if i % 2 == 0:  # If 'i' is divisible by 2 (even) then:
        print(i)  # Print the current value of 'i'
    else:  # Else, if 'i' is not divisible by 2 (odd):
        pass  # Do nothing
