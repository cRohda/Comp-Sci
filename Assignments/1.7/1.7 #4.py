List = [2, "a", "b", True, False, 12.5, 'Hello', ['x', 12.5], 'Gm', 12.654, [2, 5]]

strings = 0
booleans = 0
ints = 0  # Creates the counter for each type and makes them zero
floats = 0
lists = 0

for x in List:  # Loop through trying each item in the list
    if type(x) == str:  # If the item is a string add 1 to strings
        strings += 1
    elif type(x) == bool:  # If the item is a boolean add 1 to booleans
        booleans += 1
    elif type(x) == int:  # If the item is an int add 1 to ints
        ints += 1
    elif type(x) == float:  # If the item is a float add 1 to floats
        floats += 1
    elif type(x) == list:  # If the item is a list add 1 to lists
        lists += 1

# Print the totals
print(f'Strings: {strings}\nBooleans: {booleans}\nIntegers: {ints}\nFloats: {floats}\nLists: {lists}')