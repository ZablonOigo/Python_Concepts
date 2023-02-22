''' class is an instance of an object
object is anything that has state and behavior '''
class vehicle:
    #constructor
    def __init__(self,year,model,plate_number,curent_speed=0):
        self.year=year
        self.model=model
        self.plate_number=plate_number
        self.curent_speed=curent_speed
# methods
    def accelerate(self,value):
        self.curent_speed+=value  
        return self.curent_speed 
    def move(self):
        speed=self.accelerate(int(20))
        return speed
       
    def stop(self):
        self.curent_speed=0
        return self.curent_speed
    def vehicleDetaile(self):
        return self.model+','+str(self.year)+','+self.plate_number
mycar=vehicle(2009,'F8','abc567',int(100))
print('my car details\n')
print(mycar.vehicleDetaile())
print('my car is moving at a speed of ',mycar.move(),'Km/h')
print('car speed when parked is ',mycar.stop())
print('current speed',mycar.accelerate(int(40)))


class Person:
    def __init__(self,name,age,gender,height):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height

    def details(self):
        detail='my name is {}, I\'m {} years'
        return detail.format(self.name,self.age)
    def people(self):
     
        detail=' ,height {} ,gender {}'
        return   self.details()+ detail.format(self.height,self.gender)    
person1=Person('john',str(40),'male',float(6))
print(person1.people())            

#inheritance
#base class
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def val(self):
 
        return f"my name is {self.fname} {self.lname}"
#child class
class student(person):
    pass
person2=person('john','doe')
print(person2.val())  
student1=student('john','wright')
print(student1.val())    


#add the __init__() to the child class

class pupil:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def names(name):
        return f"student name {name.fname} {name.lname}"
class Student(pupil):
    def __init__(self,fname,lname,graduationyear):
        super().__init__(fname,lname)
        self.graduationyear=graduationyear

#add method to the child class
    def welcome(self):
       print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

student3=Student('mercy','jane',str(2023))
print(student3.names())
print(student3.graduationyear)  
student3.welcome()  


#multiple inheritance

class Animal:
    def speak(self):
        print('Animal Speaking')
class dog(Animal):
    def bark(self):
        print("dog barks")
class dogchild(dog):
    def eat(self):
        print('eating bread...')
d=dogchild()
d.speak()
d.bark()
d.eat()                




#simple arithmetic
class math:
    def add(self,x,y):
        return x+y
    def multiply(self,x,y):
        return x*y    
    def division(self,x,y):
        return x/y
    def pow(self,x,y):
        return x^y
pupil1=math()
print(pupil1.multiply(4,5)) 
print(pupil1.add(4,5))                
print(pupil1.division(4,5))                
print(pupil1.pow(4,5))                
