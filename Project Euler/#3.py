# What is the largest prime factor of the number 600851475143?
# Doesn't work because number is to large for my MacBook

Num = 1
prime = 1
totalPrimeFactors = 0
end = 600851475143

while Num < end:
    Factor = end % Num
    if Factor == 0:
        while prime <= Num:
            primeFactor = Num % prime
            if primeFactor == 0:
                totalPrimeFactors += 1
            prime += 1
        if totalPrimeFactors == 2:
            greatestFactor = Num
    Num += 1
print(greatestFactor)