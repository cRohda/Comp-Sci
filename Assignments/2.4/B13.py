my_list = ['Hi', 12, -3.6, 'a', 2 < 5]  # Base list

for i in range(len(my_list)):  # iterates through assigning i to the next index in the list
    my_list.pop(i)  # Remove the current index from the list
    if i % 2 == 0:  # if the index is evenly divisible by 2 (even)
        my_list.insert(i, 'e')  # Insert 'e' at that value
    else:  # if it is not divisible by 2 (odd)
        my_list.insert(i, 'o')  # Insert 'o'o at that value
print(my_list)  # print the new value of the list