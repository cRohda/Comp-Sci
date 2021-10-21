# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

x = 1
Sum = 0
while x < 999:
    x += 1
    if x % 3 == 0 or x % 5 == 0:
        Sum = Sum + x
print(Sum)
