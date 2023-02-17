'''used when you want to repeat a block of code a certain number of times or
the samelogic over each item in collection'''
#there are two type of loops for and while
#syntax 
''' while condition:
      statement '''

#square of nummber
number=1
while number<=10:
    print(number,'squared is ', number**2)
    number+=1

else :
    print('No number is left')

#how to break out of  a while loop
num=0
while num<=6:
    print(num)
    num+=1
    if num == 4:
        break
 #skip an item in a while loop
day=1
while day<5:
    day+=1
    if day==4:
        continue
    print('\n',day)           