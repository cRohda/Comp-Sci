# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

Num1 = 100
Num2 = 100

while Num1 < 994:
    Num2 = 100
    while Num2 < 1000:
        Product = Num1 * Num2
        Palindrome = f'{Product}'
        if Palindrome == Palindrome[::-1]:
            Highest = Product
            M1 = Num1
            M2 = Num2
        else:
            pass
        Num2 += 1
    Num1 += 1

print(f"The largest palindrome is: {Highest}, Made with {M1} and {M2}")


