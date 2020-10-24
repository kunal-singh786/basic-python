base=int(input("Enter the value of base between 1 to 16 =  ")) 
num =input("Enter a number that you want to convert in binary = ")
binary = (bin(int(num,base))[2: ])
print("The value of binary of given number is = ",binary)
count = binary.count(str(1))
count1 = binary.count(str(0))
print("The number of 1's present in the binary of given number is = ",count)
print("The number of 0's present in the binary of given number is = ",count1)
if (count%2 == 0 and count1%2 !=1):
 print("Then the number of 1's present in the binary of given number is even")
 print("Then the number of 0's present in the binary of given number is even")
elif(count%2 == 0 and count1%2 ==1):
 	print("Then the number of 1's present in the binary of given number is even")
 	print("Then the number of 0's present in the binary of given number is odd")
elif(count%2 != 0 and count1%2!=1):
 		print("Then the number of 1's present in the binary of given number is odd")
 		print("Then the number of 0's present in the binary of given number is even")
elif (count%2 != 0 and count1%2==1):
 			print("Then the number of 1's present in the binary of given number is odd")
 			print("Then the number of 0's present in the binary of given number is odd")
         
         
 