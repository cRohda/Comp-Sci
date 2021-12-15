list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']  # Given code
position = 2

a = list1.pop(position)  # Sets a the value of index {position} in list1 and removes it from the list
b = list2.pop(position)  # Sets b the value of index {position} in list2 and removes it from the list

list1.insert(position, b)  # inserts b at {position} in list1
list2.insert(position, a)  # inserts a at {position} in list2

print(list1,'\n', list2)  # prints the 2 lists, (\n creates a new in the print)