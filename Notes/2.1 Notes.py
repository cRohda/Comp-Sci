# Stores the length (# of characters) of a string or length (# of items) in a list
len([1, 2, 3, 4])
len("hello")

# Can be assigned to a variable
x = len("Hello There")

# Printing prints the stored value, first is ONE not ZERO, so hello has a value of 5, NOT 4
print(x)

# Prints just the value of the index referenced, starting at 0
print('Hello There'[2])

# Can also be used to store that value, and print it from the variable it is stored as
y = ('Hello There'[0])
print(y)

# Negative indexing, starting from the end of the string and counting down from -1.
print('Hello There'[-2])  # Will print 'r'.

# Attempting to use a number outside of the range of the string/list will cause an error
# print('Hello There'[20])  | IndexError: string index out of range

# String slicing, similar to range, allows you to assign or print a collection of characters from a string
# at a given interval (such as 2, or every-other index)
# [{starting index}:{ending index}:{interval}]
# You can leave one of the values blank at it will assume the ends, so 0:infinity:1

print(input('Enter a word or phrase: ')[::2])

# Changing the value of a string
a = "7 Layers of Heller"
# a[0] = 8  # This will result in an error, strings do not support item assignment
layers = a[1:]  # Creates a new string without the number
print('8' + layers)  # Adds a different number and then the new string to the new number

# Print multiple of the same string
b = "Bloody Mary "
print(b*3)