world = ['a', 'b', 'c', 'd', 'e']  # Base list
world2 = []  # Creates blank list
movement = int(input('Enter the movement: '))  # Gets user input for movement
length = len(world)  # Sets length variable to the length of the list

for i in range(length):  # iterate assigning i to each value of the range of 0,length
    a = world[i]  # sets a = to the value of the index i of the list

    if i + movement <= length-1:  # if the index + movement is = or less than the max index
        NewIndex = i + movement  # the new index of the current value is adding the movement
        world2.insert(NewIndex, a)  # insert the value at the new index in the blank list
    elif i + movement > length-1:  # if the index + movement is more than the max index
        NewIndex = (i + movement) - length  # the new index also subtracts the length to print at the begining
        world2.insert(NewIndex, a)  # insert the value at the new index in the blank list

print(world2)  # print the new list