x = 0
a = 1
y = True
while y == True:
    x = x + a
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    if count >= 500:
        y = False
        print(x)
    a = a + 1