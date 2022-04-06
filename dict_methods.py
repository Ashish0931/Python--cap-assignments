#Dictionary methods#
dict1={"key1":"value1","key2":"value2","key3":"value3"}
dict2={}
print("dict1: ",dict1)
print("dict2: ",dict2)
print("copying values from dict1 to dict 2: ")
dict2=dict1.copy() #dictionary copy method
print("copy done. dict2: ",dict2)
print("----------------------")
new_dict=(dict1.fromkeys("keys",0)) #creating a dictionary with key and value using fromkeys method
print ("printing new dict  made using from keys: ",new_dict)
print("----------------------")
print("value of key key1: ",dict1.get("key1")) #get method
print("----------------------")
print("items in a dictionary: ", dict1.items()) #item method
print("----------------------")
print("removing key with key key3 : ", dict1.pop("key3")) #pop method
print(dict1)
print("----------------------")
print("dict2 before popping out: ",dict2)
print("popping out last element in dict 2: ",dict2.popitem()) #popitem method
print("dict2:",dict2)
print("----------------------")
dict1.update({"key1":"updated_value1"}) #update method
print("updated dict:",dict1)
print("----------------------")
print("values of dict1:",dict1.values()) #values method

print("----------------------")
print("dict1 before clear: ",dict1)
print("dict1 after clear: ",dict1.clear()) #clear method