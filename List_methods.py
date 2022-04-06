#PYTHON - Methods of Lists
from copy import copy


test_list=[]
test_list.append("first value")
x=25
test_list.append(x) #list append operation
test_list.append(10)#list append operation
test_list.append(11)#list append operation
test_list.append(12)#list append operation
test_list.append(13)#list append operation
print(test_list)
test_list_2=test_list.copy()
print("printing list with copied value: ",test_list_2) #list copy operation
test_list.append(25)
test_list.append(25)
print("Printing count of 25 number in list: " ,test_list.count(25)) #count operation
fruits = ['apple', 'banana', 'cherry']
test_list_2.extend(fruits) #Extend operation
print("Extending lsit with another list", test_list_2)

print("Index of apple in list is: ",test_list_2.index("apple")) #Printing index of an element in list
test_list_2.insert(5,"A") #inserting an element at  a particular index position in list 
print("inserting A at 5th index postion", test_list_2)
test_list_2.pop(6) #pop operation
print("removing element at 6 position:", test_list_2)
test_list_2.remove("A") #remove operation
print("removing A element from list: ",test_list_2)
test_list_2.reverse() #reverse operation
print("reversed list:  ",test_list_2)
test_list_3=[10,18,56,34]   #sort operation
print("list before sorted:", test_list_3)
test_list_3.sort()

print("sorted list: ",test_list_3)