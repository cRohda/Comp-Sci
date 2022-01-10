world = [['a', 'b', 'c'],
         ['d', 'e', 'f'],
         ['g', 'h', 'i']]

world2 = [[], [], []]

world3 = [[], [], []]

movement = [2, -1]

horizontal = movement[1]
vertical = movement[0]

lengthHorizontal = len(world[1])
lengthVertical = len(world)

for i in range(lengthVertical):
    for a in range(lengthHorizontal):
        x = world[i[a]]
