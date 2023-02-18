#file handling
# open () accepts two arguments file name and acess mode in which file is acessed
'''
x- create and execute
w-write
w+-write and read
r-read-only
r+ - read and write
a -append 
a+ - append to existing data in file '''
#close()once all operation are done we must close the file
myfile=open('file.txt', 'w+')
myfile.write('bob\n')
myfile.write('Python is the modern day language. It makes things so simple.')

print(myfile)  
if myfile:
    print('file is opened successfully')

#close the opened file
myfile.close()   

#file append
myfile=open('file.txt','a')
myfile.write('mercy\n')
myfile.write('peter\n')
myfile.write('kingsley\n')
myfile.write('jane\n')
myfile.close()

  
#open the file.txt in write mode.    
fileptr = open("file1.txt","a")  
    
#overwriting the content of the file    
fileptr.write(" Python has an easy syntax and user-friendly interaction.")    
      
#closing the opened file     
fileptr.close()  

#file read  read()
people=open('file.txt','r')
print(people.read())


#loop through a file
file1=open('file3.txt','w+')
file1.write('mercy\n')
file1.write('peter\n')
file1.write('kingsley\n')
file1.write('jane\n')
file1.close()
file1=open('file3.txt' , 'r')
for person in file1:
    print(person)

#delete a file
import os
os.remove('file1.txt')
#check if file exist
if os.path.exists('file1.txt'):
    os.remove('file1.txt')
else:
    print('no such file')    


#copy a file
''' copyfile() method from shutil module'''

from shutil import copyfile
copyfile('file3.txt','file4.txt')
file4=open('file4.txt','r')
print(file4.read())


#rename and move file 
'''use move ( ) method from shutil module '''
from shutil import move
move('myfile.txt','anotherfile.txt')


