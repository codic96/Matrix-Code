#Python program to create a list
#from given list having number and its cude in each tuple

#creating a list
list1 = [1,2,3,5,6]

#using list comprehension to iterate each values in list

res = [(val,pow(val,5)) for val in list1]

#print the result
print(res)
