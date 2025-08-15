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
print(person_json)

with open('person.json', 'w') as file:
    json.dump(person, file)