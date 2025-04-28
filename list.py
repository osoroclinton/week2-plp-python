#create an empty list
my_list = []
print("1. Empty list:", my_list)

#appending the elements: 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("2. After appending elements:", my_list)

#move 15 to position 1
my_list.insert(1, 15)
print("3. After inserting 15 at position 1:", my_list)

#extends my_list with another list
my_list.extend([50, 60, 70])
print("4. After extending the list:", my_list)

#remove the last element on the list
my_list.pop()
print("5. After removing the last element:", my_list)

#sort list to ascending order
my_list.sort()
print("6. After sorting in ascending order:", my_list)

#find an element in the list
index_of_30 = my_list.index(30)
print("7. Index of value 30:", index_of_30)