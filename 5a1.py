mobile = ['nokia','samsung','vivo','oppo','redmi']
x = type(mobile)
print(x)
string = ' '.join(mobile)
print(string)
def check_vow(string,vowels):
	final = [each for each in string if each in vowels]
	print(len(final))
	print(final)
vowels = "AaEeIiOoUu"
check_vow(string,vowels);