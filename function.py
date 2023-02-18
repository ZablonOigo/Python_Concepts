#python we use def keyword to define a function
#function is a block of code that is called to perform a certain function
#function enhance code reusability,easier syntax.
#syntax
''' def name_of_function(parameter):
      code block    '''
def myfunction (num):
    print(num*num)
myfunction(2)          
#square of a number
def square(num):
    return num**2
mynum=square(5)
print('the square of num is',mynum )    

#list item
def myarr(a):
    arr=[]
    for i in a:
        arr.append(i**2)
    return arr
list1=[1,2,3,4]
result=myarr(list1)
print('the square of the values are ',result)

#variable length arguments
# *args-these are non-keyword arguments
def function(*args):
    myarr=[]
    for i in args:
        myarr.append(i.upper())
    return myarr
#passing args argument    
object= function('Python', 'Functions', 'tutorial')
print(object)       

# **kwargs-thes are keyword argument
def function1(**kwargs):
    arr=[]
    #x,j key/value pair
    for x,j in kwargs.items():
        arr.append([x,j])
    return arr
myarr=function1(first="Python", Second = "Functions", Third = "Tutorial")    
print(myarr)    


#lambda function
#are anonymous function implying they dont have a name
#we can used lambda keyword in pyhton to define an unnamed function
#syntax
'''  lambda arguments:expression '''
add=lambda num:num**2
print(add(4))

#filter odd number from a given list
odd_list=[23,45,12,45,67,22,10]
list_=list(filter(lambda num:(num % 2!=0),odd_list))
print(list_)



#using lambda with map()
#map() used to sqaure entries in a list
num1=[2,3,4,5,6,7,8,9]
mynum=list(map(lambda num:num**2,num1))
print(mynum)

#if else statement
val=lambda a,b:'true' if(a<b) else 'false'
print(val(20,4))