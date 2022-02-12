movies = {}

loop = True


# Clears console
def clearconsole():
    print('\n' * 150)


# Gets dictionary inputs
while loop:
    name = input('Enter movie name: ')
    info = []
    genre = input('Enter genre: ')
    info.append(genre)
    year = input('Enter year of release: ')
    info.append(year)
    movies[name] = info

    # Asks if user would like to input another value
    while True:
        again = input('Would you like to enter another movie? (Y/N): ')
        print()
        if again.lower() == 'y':
            break
        elif again.lower() == 'n':
            loop = False
            break
        else:
            print('I did not recognize that input')

clearconsole()
# Printing dictionary and formatting
for i in movies:
    print(i, end=': ')  # Prints key
    spacing = 0

    # Prints definition
    for x in movies[i]:
        print(x, end='')  # Prints genre

        # Adds a single dash between the genre and year
        if spacing == 0:
            print(' - ', end='')
        spacing = 1
    print()
