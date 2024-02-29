#Creating emptylist

my_list = []

print(my_list)
#append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)
#Inserting the value 15 at the second position

my_list.insert(1, 15)

print(my_list)

#Remove the last element from my_list

my_list.pop()
print(my_list)

# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_30}")
print(my_list)