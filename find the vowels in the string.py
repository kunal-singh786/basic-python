''' Write a program to get the number of vowels in the input string'''
def check_vow(string,vowels):
#Here i am using comprehension statement to get the vowels in the string
	final = [each for each in string if each in vowels]
	#print(len(final))
	print(final)
	
string = "Python is cross platform programing language"
vowels = "AaEEIiOoUu"
check_vow(string,vowels);