x = int(input('Enter a number: '))
index = 0
for i in range(1, int(x/2) +1):
    if x % i == 0:
        print(i)
        index += 1
print(x)
print(f'There were {index + 1} divisors')