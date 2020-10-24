a = int(input("enter the value of a="))
b = int(input("enter the value of b="))
g = int(input("enter the value of g(for addition enter 1, for substraction enter 2, for division enter 3, for multiplication enter 4="))
c = a+b
d = a-b
e = a%b
f = a*b
if g == 1:
	print("Addition of a and b is",c)
elif g == 2:
		print("Substraction of a and b is",d)
elif g == 3:
			print("Divison of a and b is",e)
elif g == 4:
				print("Muliplication of a and b",f)