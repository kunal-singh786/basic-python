''' write a program to perform various various arithmetic operation'''
int_1 = int(input("Enter a number:-"))
int_2 = int(input("Enter a number:-"))
c = input('Enter the mathematical operation:-')
add = int_1+int_2
sub = int_1 - int_2
mul = int_1*int_2
div = int_1/int_2
modulo = int_1%int_2
exp= int_1**int_2
remainder = int_1//int_2
if c== 'add':
	print("The addition of two number is :-",add)
elif c == 'sub':
	print("The substraction of two number is:-",sub)
elif c == 'mul':
	print("The multiplication of two number is:-" ,mul)
elif c == 'div':
	print("The division of two number is:-",div)
elif c== 'modulo':
	print("The modulo of two number is:-",modulo)
elif c== 'exp':
	print("The exponential of two number is:-",exp)
elif c== 'remainder':
	print("The remainder of two number is:-" ,remainder)