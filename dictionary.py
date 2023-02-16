#used to store data in a key value pair like js(objects)
#they do not guarantee order -not indexed
# they are mutable can be changed

#created using curly bracket and each key is separated from its value by colon (:)

people={'bob':30,'mary':40}
print(type(people))
print('\n',people)
#adding values
people['sarah']=32
print(people)

#updating a dictionary
#if the key already exist value is easily updated
people['bob']=20
print(people)
#deleting dictionary
people.pop('sarah')
print(people)
#or clear () remove everyone
#check if a given key already exists in dictionary
if 'sarah' in people:
    print('\n yes available')
else:
    print('\n not available')    

#looping
#print only the keys
for x in people:
    print(x)   
    #print key and value 
    print(people[x])