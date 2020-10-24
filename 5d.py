a = input("Enter the string")
b = list(a)
l = [ ]
for i in b:
	c = b.count(i)
	l.append((c,i))
l.sort()
print('count of all characters in a is',l)