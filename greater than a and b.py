a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))
if(a > b):
    print("{0} is Greater than {1}".format(a,b))
elif(b > a):
    print("{0} is Greater than {1}".format(a,b))
else:
    print("Both a and b are Equal")