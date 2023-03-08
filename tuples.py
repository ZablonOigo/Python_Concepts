#are used to store multiple item in a single variable (array)
#they are immutable meaning cannot be changed -read-only
#written with round brackets ()
#its ordered

#initialization
people=('mary','Bob')
print(type(people))

print(people)
print(len(people))

#updating a tuple will result to an error as this is read-only
#but there is a trick convert to a list then change the item and convert back to a tuple
people_list=list(people)
people_list.append('sarah')
people=tuple(people_list)
print(type(people))
print(people)

#check if an item exist
if 'john' in people:
    print('yes available')
else:
    print('no not available')

#taking user input
tuple1=tuple(input('enter the tuple element'))
print(tuple1)
        


fruit_list = ['apple', 'orange', 'banana']
fruit_list2 = list(fruit_list)
print(id(fruit_list) == id(fruit_list2))  # False
