list1 = [15, -2, 10, -5, -4, 6, 3, -1, -8, 13, -12, -11, 7, 14]  # Base list
even_list = [-2, 10, -4, 6, -8, -12, 14]  # creates and sets even_list

# Removed code from problem 3 because value of even_list is already assigned

for i in range(len(even_list)):  # iterates through the indices of even_list and assigns 'i' to the next one each time
    idx = i  # Assign idx to the current value of 'i' (next value to be sorted)

    # iterates through the indices of even_list starting at i+1 to find the number that should be next
    for j in range(i + 1, len(even_list)):

        # if the value of even_list at index idx is greater than the value of even_list at the index j
        if even_list[idx] > even_list[j]:
            idx = j  # set idx equal to j

    # Swapping
    # Creates temporary variables to store value's during swap
    temp1 = even_list[i]
    temp2 = even_list[idx]

    # Swaps using the temporary variables
    even_list[i] = temp2
    even_list[idx] = temp1

print(even_list)  # Prints the end result
