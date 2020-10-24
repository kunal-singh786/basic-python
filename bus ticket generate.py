print("                       Jotti Travelers")
bus_no =int(input("Enter the bus number(Gurugram to Other= 35, Other to Gurugram= 36)="))
name = str(input("Name:-"))
age = int(input("Age:-"))
gender = str(input ("Gender:-"))
source = str(input("Source:-"))
des = str(input("Destination:-"))
rate = int(input("Enter the distance between source and destination(for Amritsar = 3 , for kanpur = 5,for Patna =8 and For kolkata 12)="))
cost = rate*100
if cost == 300:
	print(" You want to pay",cost," and this ticket is valid only for Gurugram to Amritsar")
elif cost == 500:
	print(" You want to pay",cost," and this ticket is valid only for Gurugram to Kanpur")
elif cost == 800:
	print(" You want to pay",cost," and this ticket is valid only for Gurugram to Patna ")
elif cost == 1200:
	print(" You want to pay",cost," and this ticket is valid only for Gurugram to Kolkata ")
print("Note:- if you travel without taking ticket than you want to pay the fine upto 5000 and for any clarification please contact our helpline number 9789926551")