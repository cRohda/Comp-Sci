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

# .upper
c = 'hello'
print(c.upper())  # prints the value but makes it uppercase letters

# .lower
d = 'GOODBYE'
print(d.lower())  # prints the value but makes it lower case letters

# These can also be used to store values, meaning it can be used in if statements too
e = 'hello'
if e.upper() == 'HELLO':
    print('It is lowercase but i read it as uppercase')

# .split
f = 'Good Morning Ella!'
print(f.split())  # Splits the string at every space (by default) into different values of a list
flist = f.split()  # Stores the value of the list of the split string
folist = f.split('o')  # Splits the string at the selected character. The selected value is removed in the list
print(folist)

old = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n',
       'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']