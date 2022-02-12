def value(p, n, d, q, hd, sd):
    total = (p * 0.01) + (n * 0.05) + (d * 0.1) + (q * 0.25) + (hd * 0.5) + sd
    return total


pennies = int(input('How many pennies?: '))
nickles = int(input('How many nickles?: '))
dimes = int(input('How many dimes?: '))
quarters = int(input('How many quarters?: '))
half = int(input('How many half dollars?: '))
dollars = int(input('How many silver dollars?: '))

print(f'There is ${value(pennies, nickles, dimes, quarters, half, dollars)} in the jar!')
