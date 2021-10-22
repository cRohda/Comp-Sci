counter = 0

for x in range (1, 4):
    for blank in range(1, 4-x):
        print(end='  ')
    while counter != (2*x-1):
        print('* ', end='')
        counter += 1
    print()