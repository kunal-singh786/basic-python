string_1 = str(input("Enter a string1:-"))
string_2= str(input("Enrer a string2:-"))
string_11 = list(string_1)
string_12 = list(string_2)
string_11.sort(reverse = True)
string_12.sort(reverse= True)
if string_11 == string_12:
	print("This is an Anagram")
else:
	print("This is not Anagram")