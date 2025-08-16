import json

person = {
  "firstName": "John",
  "lastName": "Doe",
  "hobbies": ["reading", "gaming", "coding"],
  "age": 30,
  "hasChildren": True,
  "children": [
    {
      "firstName": "Jane",
      "lastName": "Doe",
      "age": 5
    },
    {
      "firstName": "Jack",
      "lastName": "Doe",
      "age": 3
    }
  ]
}

# person_json = json.dumps(person, indent=4, separators=(': ', "="))
person_json = json.dumps(person, indent=4, sort_keys=True)
# print(person_json)

# with open('person.json', 'w') as file:
#   json.dump(person, file, indent=4)

# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(person)

# convert_to_dict = json.loads(person_json)
# print(convert_to_dict)

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Alice", 29)

# def encode_user(obj):
#     if isinstance(obj, User):
#         return {
#             "name": obj.name,
#             "age": obj.age,
#             obj.__class__.__name__: "User"
#         }
#     else:
#         raise TypeError('Object of type is not json serializable')

from json import JSONEncoder
class JsonEncode(JSONEncoder):
    def default(self,obj):
        if isinstance(obj, User):
            return {
                "name":obj.name,
                "age": obj.age,
                obj.__class__.__name__: True
            }
        return JSONEncoder.default(self, obj)
    
user = json.dumps(user, cls=JsonEncode)
print(json.loads(user))
# print(JsonEncode().encode(user))