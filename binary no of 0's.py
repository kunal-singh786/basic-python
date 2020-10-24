base=int(input("Enter the value of base between 1 to 16 =  ")) 
num =input("Enter a number that you want to convert in binary = ")
binary = (bin(int(num,base))[2: ])
print("The value of binary of given number is = ",binary)
count = binary.count(str(0))
print("The number of 0's present in the binary of given number is = ",count)
if (count%2 == 0):
 print("Then the number of 0's present in the binary of given number is even")
else:
 	print("Then the number of 0's present in the binary of given number is odd")
 