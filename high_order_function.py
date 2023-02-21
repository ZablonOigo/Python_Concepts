#default function to take another function parameter
def spell(text):
    #making text in upper
    return text.upper()
text=input('enter atext to print it in uppercase')
print(spell(text))
#assigning variable with the default function
txt=spell
print(txt(text))    


# print both lower and upper
def text(word):
    return word.upper()
def word(spell):
    return spell.lower()
def scream(func):
    speak=func('I Love Python')
    print(speak)  
scream(text)
scream(word)    

#returning a function as a result
def add(a):
    def adding(b):
        return a+b
    return adding
#taking both number variable as user input
a=int(input('enter first number'))
b=int(input('enter second number'))
addition=add(a)
result=addition(b)

print('the sum of two number is: ',result) 
