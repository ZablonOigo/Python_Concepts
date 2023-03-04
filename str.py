# removing duplicates from string
mylist=['apple','banana','mango','kiwi','apple','kiwi','mango']
mylist=list(dict.fromkeys(mylist))
print(mylist)