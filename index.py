#Create an empty list
my_list = []

#Appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting 15 at the second position in the list
my_list.insert(1, 15)
print(my_list)

#Extend my_list with other items
my_list.extend([50, 60, 70])
print(my_list)

#Remove the last item
my_list.pop()
print(my_list)

#Sort in ascending order
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
