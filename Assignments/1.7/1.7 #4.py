List = [2, 324.3214, 'a', 'b', True, [2, 5]]  # The list in question
x = 0  # creates x, counts up each time through to know when to stop counting the types
string = 0
Boolean = 0
Integer = 0  # Variables to count the number of each type
Decimal = 0
Group = 0
for i in List:  # For each value in list
    if type(List[x]) == str:  # if the type is a string
        string += 1  # Add one to the string count
    elif type(List[x]) == bool:  # if the type is a boolean
        Boolean += 1  # add one to the boolean count
    elif type(List[x]) == int:  # this same process repeats for each type
        Integer += 1
    elif type(List[x]) == float:
        Decimal += 1
    elif type(List[x]) == list:
        Group += 1
    if x <= len(List):  # if x is less than/equal too the length of the list
        x += 1  # add one fo x
    else:  # if x is more than the length of the list (this means it's tried every value)
        break  # end the loops
# Prints the number of each type
print(f'Strings: {string}\nBooleans: {Boolean}\nIntegers: {Integer}\nFloats: {Decimal}\nLists: {Group}')
