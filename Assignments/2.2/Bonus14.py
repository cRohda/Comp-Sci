import random as r

# Makes lists of characters
let = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,'  # Sets letters as a string
alpha = let.split(',')  # Splits the string into a list, I found this less work than manually making a list
num1 = r.randint(0,9)  # Makes num1 a random number
num2 = r.randint(0,9)  # Makes num2 a random number
special = ['!', '?', '%', '#', '*']  # Makes a list of special characters

a1 = r.choice(alpha)
a2 = r.choice(alpha)
a3 = r.choice(alpha)  # Creates 5 random letters as different variable
a4 = r.choice(alpha)
a5 = r.choice(alpha)
s1 = r.choice(special)  # Choose a random special character

final = f'{a1}{a2}{a3}{a4}{a5}{num1}{num2}{s1}'  # Makes a variable of the random result
print(f'Your password is: {final}')  # Prints the result