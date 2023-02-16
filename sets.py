#set is a collection of unordered item
#each element must be unique immutable -cannot be changed
#sets are unordered ,do not guarantee order

#creating sets
day={'monday','teusday','wednesday','thursday','friday'}
print(type(day))

print(day)
#loopin through using for in
print('looping through using "for in" ')
for i in day:
    print(i)

#adding item to sets
#add() method or update ()
month=set(['january','february','march','april'])
print('\n printing original set')
print(month)
month.add('may')
month.add('june')
print('\n modified set')
print(month)
month.update(['july','august'])
print('\n updated set')
print(month)
#for in
for j in month:
    print('\t'+j)
#removing an item
#discard() remove ()
month.discard('january')
print(month)
month.remove('february')
print(month)

#set operation

#union of two sets is calculated using pipe(|)
day2=set(['monday','teusday'])
day3=set(['wednesday','thursday'])
day4=day2.union(day3)
print(day4)
day5=day2|day3
print(day5)

#intersection of two sets
#can be performed using & operator
day6=day2.intersection(day3)
print(day6)