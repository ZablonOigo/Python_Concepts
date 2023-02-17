'''syntax
for item in collection
 statement '''
#loop over a list
car=['bmw','audi','Mclaren']
for i in car:
    print(i) 
#break out of loop
num=[2,3,4,5,6]
for j in num:
    print(j)
    if j==5:
        break    
#jump overan iteration
cars=['bmw','audi','Mclaren']
for i in cars:
    if i=='audi':
        continue
    print(i)    
#loopd over nested loop
car_model=[['bmw 18','bmw xw','bmw x1'],
['ferrari 812','ferrari f8','ferrari gtc4'],
['Mclaren 576s','Mclaren 576GT','Mclaren 720s']
]    
for x in car_model:
    for model in x:
            print('car model -', model)

