#list used to store multiple item in a single variable(array)
list1=['apple','banana','cherry']
print(list1)
print(type(list1))
#iterate using (for in)
for x in list1:
    print(x)

#list method
#append()
fruit=['apple','banana','kiwi']
fruit.append('orange')
print(fruit)


#clear()
#remove all element from the list
fruit.clear()
print(fruit)

#copy()
#returns a copy of the list
fruit=['apple','banana','kiwi']
fruit1=fruit.copy()
print(fruit1)

#count () return the number of element (index) with specified value
fruit2=['kiwi','mango','passion']
x=fruit2.count('mango')
print(x)

#extend() add element of a list to end of cureent list
car=['bmw','ford','volvo']
fruit.extend(car)
print(fruit)


#index () return the index of the first element with specified value
y=car.index('ford')
print(y)


#insert() insert specified value at specified position
car.insert(1,'toyota')
print(car)


#pop() remove an element at specified position
car.pop(1)
print(car)

#remove() remove item in specified value
car.remove('volvo')
print(car)

#reverse() reverse elements of list
fruit.reverse()
print(fruit)

#sort() sorting a list
bus=['bus6','bus2','bus4','bus5','bus3']
bus.sort()
print(bus)

#list length
print(len(bus))

#range indexes
print(bus[2:4])

#check if an items exist
if 'bus2' in bus:
    print('yes "bus2" is in bus list')

#change range item

num=[1,2,3,4,5,6,7]
num[1:3]=[14,15]
print(num)

#looping through by referring to index number. range() and len()
a=[1,2,3,34,15,76]
for v in range(len(a)):
    print(a[v])
#using while loop
b=[4,5,3,2,1]
i=0
while i<len(b):
    print(b[i])
    i+=1
#list comprehension 
# add values of an existing list to an empty list
veggies=['kales','cabbage','cucumber','brocolli']
newveggies=[]
for f in veggies:
    if "c" in f:
        newveggies.append(f)
print(newveggies)      

#0r shorter syntax
newveggies=[x for x in veggies if  'c' in x]
print(newveggies)

# sequence
numbers = [1, 4, 5, 3, 5, 7, 8, 5]
print(numbers.index(5, 3, 5))
print(numbers[2:6])
print(min(numbers))  # 1
print(max(numbers))  # 8
