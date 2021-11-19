y = True
x = 1
divisors = 0
prime = 0
while y == True:
    x += 1
    divisors = 0
    for i in range(1, int(x ** (1/2))+1):
        if x % i == 0:
            divisors += 1
    if divisors == 1:
            prime += 1
            print(f'{x} is the {prime} prime number')
    if prime == 10001:
        y = False
print(f'{x} is the 10001st prime number!')