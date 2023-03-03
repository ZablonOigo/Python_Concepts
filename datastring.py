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


i = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
j= json.dumps(i)

# the result is a JSON string:
print(j)
