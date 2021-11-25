import sys 
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

#a = 1
#b = -3
#c = -4

d = b**2 - 4 * a * c

x_1 = (-b + d**(1 / 2)) / (2 * a)
x_2 = (-b - d**(1 / 2)) / (2 * a)

print(int(x_1), int(x_2))