import json
# json.loads()
x='{"name":"john", "age":30, "city":"New York"}'
detail=json.loads(x)
print(detail['age'])


# conver python to json
data={
    'name':'Doe',
    'age':'40',
    'city':'London'

}
# convert into json
y=json.dumps(data)
print(y)