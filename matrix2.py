''' Group similar elements into Matrix '''

from itertools import groupby
#initializing list

test_list = [12,13,14,15,16,17,21]

#printing original list
print('The Original list'+ str(test_list))

res = [list(val) for keys,val in groupby(sorted(test_list))]
#Printing result

print('Matrix after grouping'+ str(res))
