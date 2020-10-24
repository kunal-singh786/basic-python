import cmath
a = (int(input('Enter the value of a:')))
b = (int(input('Enter the value of b')))
c = (int(input('Enter the value of c:')))
d = (b**2)-(4*a*c)
print('The value of d is',d)
sol1 = (-(b)- cmath.sqrt(d)/(2*a))
sol2 = (-(b)+ cmath.sqrt(d)/(2*a))
print('The solution of {0} and {1} is'.format(sol1,sol2))