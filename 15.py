# JSON 
import json

dic = '{"Name": "Faheem", "Age":      22, "Country":  "Pakistan"}'


a = json.loads(dic)

print(a)
print(type(a))



dic1 = {
    "Model":    "Mustang",
    "Location": "Karachi",
    "Country":  "Pakistan"
}

x = json.dumps(dic1)

print(x.capitalize)




print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))