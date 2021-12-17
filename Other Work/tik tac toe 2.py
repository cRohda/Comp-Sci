import random as r
import tkinter as tk

# Functions
def spot1():
    if turns % 2 == 0:
        x1.grid(row=2, column=0)
    else:
        o1.grid(row=2, column=0)

def spot2():
    if turns % 2 == 0:
        x1.grid(row=2, column=2)
    else:
        o1.grid(row=2, column=2)

def spot3():
    if turns % 2 == 0:
        x1.grid(row=2, column=4)
    else:
        o1.grid(row=2, column=4)

def spot4():
    if turns % 2 == 0:
        x1.grid(row=4, column=0)
    else:
        o1.grid(row=4, column=0)

def spot5():
    if turns % 2 == 0:
        x1.grid(row=4, column=2)
    else:
        o1.grid(row=4, column=2)

def spot6():
    if turns % 2 == 0:
        x1.grid(row=4, column=4)
    else:
        o1.grid(row=4, column=4)

def spot7():
    if turns % 2 == 0:
        x1.grid(row=6, column=0)
    else:
        o1.grid(row=6, column=0)

def spot8():
    if turns % 2 == 0:
        x1.grid(row=6, column=2)
    else:
        o1.grid(row=6, column=2)

def spot9():
    if turns % 2 == 0:
        x1.grid(row=6, column=4)
    else:
        o1.grid(row=6, column=4)

# window creation
window = tk.Tk()
window.title('TicTacToe')
window.configure(bg='white')

# sprites
x = tk.PhotoImage(file='X.png')
o = tk.PhotoImage(file='O.png')
blank = tk.PhotoImage(file='Blank.png')
horiz = tk.PhotoImage(file='Horiz.png')
vert = tk.PhotoImage(file='Vert.png')
mid = tk.PhotoImage(file='Mid.png')

# creating blanks
Blank1 = tk.Button(image=blank, bg='white', command=spot1)
Blank2 = tk.Button(image=blank, bg='white', command=spot2)
Blank3 = tk.Button(image=blank, bg='white', command=spot3)
Blank4 = tk.Button(image=blank, bg='white', command=spot4)
Blank5 = tk.Button(image=blank, bg='white', command=spot5)
Blank6 = tk.Button(image=blank, bg='white', command=spot6)
Blank7 = tk.Button(image=blank, bg='white', command=spot7)
Blank8 = tk.Button(image=blank, bg='white', command=spot8)
Blank9 = tk.Button(image=blank, bg='white', command=spot9)

# creating vertical lines
Vert1 = tk.Label(image=vert, bg='white')
Vert2 = tk.Label(image=vert, bg='white')
Vert3 = tk.Label(image=vert, bg='white')
Vert4 = tk.Label(image=vert, bg='white')
Vert5 = tk.Label(image=vert, bg='white')
Vert6 = tk.Label(image=vert, bg='white')

# creating horizontal lines
Horiz1 = tk.Label(image=horiz, bg='white')
Horiz2 = tk.Label(image=horiz, bg='white')
Horiz3 = tk.Label(image=horiz, bg='white')
Horiz4 = tk.Label(image=horiz, bg='white')
Horiz5 = tk.Label(image=horiz, bg='white')
Horiz6 = tk.Label(image=horiz, bg='white')

# Creating middle crosses
Mid1 = tk.Label(image=mid, bg='white')
Mid2 = tk.Label(image=mid, bg='white')
Mid3 = tk.Label(image=mid, bg='white')
Mid4 = tk.Label(image=mid, bg='white')

# Creating labels for X's
x1 = tk.Label(image=x, bg='white')
x2 = tk.Label(image=x, bg='white')
x3 = tk.Label(image=x, bg='white')
x4 = tk.Label(image=x, bg='white')
x5 = tk.Label(image=x, bg='white')
x6 = tk.Label(image=x, bg='white')
x7 = tk.Label(image=x, bg='white')
x8 = tk.Label(image=x, bg='white')
x9 = tk.Label(image=x, bg='white')

# Creating labels for O's
o1 = tk.Label(image=o, bg='white')
o2 = tk.Label(image=o, bg='white')
o3 = tk.Label(image=o, bg='white')
o4 = tk.Label(image=o, bg='white')
o5 = tk.Label(image=o, bg='white')
o6 = tk.Label(image=o, bg='white')
o7 = tk.Label(image=o, bg='white')
o8 = tk.Label(image=o, bg='white')
o9 = tk.Label(image=o, bg='white')

# Griding Blank spots
Blank1.grid(row=2, column=0)
Blank2.grid(row=2, column=2)
Blank3.grid(row=2, column=4)
Blank4.grid(row=4, column=0)
Blank5.grid(row=4, column=2)
Blank6.grid(row=4, column=4)
Blank7.grid(row=6, column=0)
Blank8.grid(row=6, column=2)
Blank9.grid(row=6, column=4)

# Griding the Grid
Vert1.grid(row=2, column=1)
Vert2.grid(row=2, column=3)
Vert3.grid(row=4, column=1)
Vert4.grid(row=4, column=3)
Vert5.grid(row=6, column=1)
Vert6.grid(row=6, column=3)

Horiz1.grid(row=3, column=0)
Horiz2.grid(row=3, column=2)
Horiz3.grid(row=3, column=4)
Horiz4.grid(row=5, column=0)
Horiz5.grid(row=5, column=2)
Horiz6.grid(row=5, column=4)

Mid1.grid(row=3, column=1)
Mid2.grid(row=3, column=3)
Mid3.grid(row=5, column=1)
Mid4.grid(row=5, column=3)

turns = 1

window.mainloop()

