car= ['suzuki','BMW','Toyota','Tvs','BMW']
a = type(car)
print(a)
string = ' '.join(car)
print(string)
def check_vow(string,vowels):
	final = [each for each in string if each in vowels]
	print(len(final))
	print(final)
vowels = "AaEeIiOoUu"
check_vow(string,vowels);

