def add(x,y):
    return x+y
def subtract(x,y):
    return x-y    
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y   

option='''Select operation.\n
        1.Add\n
        2.Subtract \n 
        3.Multiply\n
        4.Divide   '''
print(option)

while True:
    choice=input('Please enter a choice 1/2/3/4: ')
    if choice in ('1','2','3','4'):
        try:
              num1=float(input('enter first number'))
              num2=float(input('enter second number')) 
        except ValueError:
            print('Invalid input.Please enter a number')
            continue

        if choice =='1':
            print(f'{num1} + {num2} =', add(num1,num2)) 
        elif choice == '2':
            print(f'{num1} - {num2} =', subtract(num1,num2)) 
        elif choice == '3':
            print(f'{num1} * {num2} =', multiply(num1,num2)) 
        elif choice == '4':
            print(f'{num1} / {num2} =', divide(num1,num2))
     #check if user wants another calculation
    #  break the while loop if answer is no
        next_calculation=input('Do you want another calculation ?')
        if next_calculation == 'no':
            break
    else:
        print('Invalid Input')  

                                 


      