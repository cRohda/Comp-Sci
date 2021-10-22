for x in range(1, 6):  # Repeat this process making x the next value each time (starting at 1, ending at 5)
    for y in range(x, 0, -1):  # Repeat this process making y the next value each time (starting with x, going backwards
        print(y, end='')  # print the value of y, and don't start a new line
    print()  # Print nothing to start a new line
for a in range(1, 5):  # Repeat this process making a the next value each time (starting at 1, ending at 4)
    for b in range(5 - a, 0, -1):  # Repeat this process making b the next value, starting at 5-a going backwards to 0
        print(b, end='')  # print the value of b, and don't start a new line
    print()  # Print nothing to start a new line
