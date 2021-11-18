from collections import Counter

#initializing list
test_list = [12,13,13,14,15,122,90,67]

#printing original list
print('The Original list '+str(test_list))

temp = Counter(test_list)
res = [[key]*val for key,val in temp.items()]

#printing the result
print('Matrix after result'+ str(res))
