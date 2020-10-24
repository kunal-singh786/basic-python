# Write a program to get a list of even numbers from a given list of number ( use only comprehension)
a = [12,17,65,44,33,27,98,76,55,22,2,7,9,4,6]
# syntax of comprenhension [expression for item in list]
b = [num for num in a if num%2 ==0]
print("Even number:",b)