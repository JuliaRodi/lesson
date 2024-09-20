immutable_var = 5,9,"milk",False
print(immutable_var)
#immutable_var[0] = 7
#print(immutable_var) #TypeError: 'tuple' object does not support item assignment
mutable_list = [5,9,"milk",False]
mutable_list[2] = 4
print(mutable_list)