inp = input('Enter a series of words, SEPERATED BY COMMAS WITH NO SPACE (e.g. hello,hi): ')
list = inp.split(',')

ph1 = 0
count1 = 0
index1 = 0
ph2 = 0
count2 = 0
index2 = 0

for x in list:
    if len(x) > count1:
        count1 = len(x)
        index = list[ph1]
    ph1 += 1

for y in list:
    if count1 > len(y) > count2:
        count2 = len(y)
        index2 = list[ph2]
    ph2 += 1

print(index2)