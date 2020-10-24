base=int(input("enter base")) 
a=int(input("enter no:"),base) 
print(a) 
c=int(input("Enter the require conversion"))
if c==1:
	print(bin(a)) 
elif c==2:
	print(oct(a)) 
elif c==3: 
    print(hex(a))