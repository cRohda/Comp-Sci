counter = 0

for x in range (1, 4):
    for blank in range(1, 4-x):
        print(end='  ')
    while counter != (2*x-1):







constant = 0

for x in range(1, 4):
    for space in range(1, (3 - x) + 1):
        print(end="  ")
    while constant != (2 * x - 1):
        print("* ", end="")
        constant += 1
    k = 0
    print()
