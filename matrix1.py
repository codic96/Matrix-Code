''' Assigning subsequent Rows to Matrix first row elements '''
#initializing list

test_list = [[5,8,9],[5,4,2],[10,12,12]]

#printing original list
print('The print Original list' + str(test_list))

#dict() to convert back to dict
#slicing and pairing using zip() and list slicing

res = dict(zip(test_list[0],test_list[1:]))

#printing result
print("The Assigned Matrix :"+ str(res))
