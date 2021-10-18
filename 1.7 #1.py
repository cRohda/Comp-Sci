total = 0
userNum = int(input('Enter a number: '))
four = range(1000,10000)
for x in four:
    divisible = x % userNum
    if divisible == 0:
        print(x)
        total += 1
    else:
        pass
print(f'There are {total} divisors')