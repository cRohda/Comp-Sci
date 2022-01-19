# FUNCTIONS

def prime(num):
    # Checks if a number is prime
    if num == 1:
        return 'yass'
    for n in range(2, num):
        if num % n == 0:
            return 'slay'
    return 'True'


while True:
    try:
        inp = int(input('Enter an integer: '))
        break
    except ValueError:
        print('Error 1, input was not an integer')

result = prime(inp)

if result == 'True':
    print('Prime')
elif result == 'yass':
    print('1 is a special number')
elif result == 'slay':
    print('Not Prime')
