
#string
name='rabbit'
print(name)
print(type(name))

#string are array of bytes
fullName='hello Engineer'
print(fullName[2])#index 2
print(len(fullName))
#loop through using For in
for x in fullName:
  print(x)

#check string exist should return true else should return false if not found  
text ='best thing in life are free'
print('free' in text)  



#string slicing
#you can return a range of character by using the slice
txt='webdeveloper'
print(txt[2:5])
#bde

#slice start from
print(txt[:5])
#webde

#slice end
print(txt[2:])
#bdeveloper

#string methods
web=' mern developer'
print(web.upper())
print(web.lower())
#remove whitepace before and after actual text
print(web.strip())


# combine string using format()
quantity=3
item=567
price=49.95
my_order='I want {} pieces of item {} for {} dollars '
print(my_order.format(quantity,item,price))