#accesing dict from inside a list 
test_list=[1,2,3,{"key1":1,"key2":2},7,8,9]
print(test_list[3]["key1"])     #accessing dict from a list
print(test_list[3]["key2"])     #accessing dict from a list

#accsing a list from a dict
test_dict={"key1":1, "key2":2,"key4":3}
test_dict["key3"]=[1,3,5]
print(test_dict["key3"][0]) #accessing data from a list inside a dictionary
print(test_dict["key3"][1]) #accessing data from a list inside a dictionary#
print(test_dict["key3"][2]) #accessing data from a list inside a dictionary

#adding data into tuple
test_tuple=(1,2,4,78,434)
print("before modified tuple: ",test_tuple) #printing non modified tuple
ls=list(test_tuple) #converting tuple to list
ls.insert(2,432) #inserting data into list
test_tuple=tuple(ls) #converting list back to tuple
print("modified tuple: ", test_tuple) #printing modified tuple