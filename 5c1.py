string_1 = str(input("Enter a string1:-"))
string_2= string_1[::-1]
print("Reverse of string1",string_2)
string_11 = list(string_1)
string_12 = list(string_2)
string_11.sort() #(reverse = True|False)
string_12.sort() #(reverse= True|False)
if string_11 == string_12:
	print("This is an Anagram")
else:
	print("This is not Anagram")