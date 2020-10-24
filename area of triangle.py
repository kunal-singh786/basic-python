a = 5
b = 3
c = 6
s = (a+b+c)/2
print('The semi perimeter of triangle is',s)
print(type(s))
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(type(area))
print('The area of the triangle is',area)