import json
# json.loads()
x='{"name":"john", "age":30, "city":"New York"}'
detail=json.loads(x)
print(detail['age'])