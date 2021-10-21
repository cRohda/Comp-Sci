user = input('Enter some characters: ')
string = 0
integer = 0
Punct = 0
Blank = 0
x = 0
PunctList = ['!', ',', '?', '.', "'", ':', ';']
for x in user:
    if type(user) == str:
        string += 1
    elif user == ' ':
        Blank += 1
    elif user in PunctList:
        Punct += 1
    elif type(user) == int:
        integer += 1
print(f'Strings {string}\nIntegers: {integer}\nPunctuation: {Punct}\nBlank: {Blank}')
