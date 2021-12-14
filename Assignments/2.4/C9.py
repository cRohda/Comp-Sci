list1 = [1, 2, 3, 4, 5]  # Creates list 1
list2 = ['a', 'b', 'c', 'd', 'e']  # Creates list 2
new = []  # Creates a blank list
position = 2  # Sets position variable to 2

a = list1.pop(position)  # Sets a to the {position} index of list1, and removes that value from the list
new.append(a)  # appends the value of a to new
a = list2.pop(position)  # Re-assigns a to the {position} index of list2, and removes that value from the list
new.append(a)  # appends the value of a to new

print(list1, list2, new)  # Prints the lists