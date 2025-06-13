
import json, camelcase, cowsay

# string = '''
# {
#     "persons": [
#         {
#             "name": "Bill Gate",
#             "phone_no": "+1 300 540",
#             "gender": "M",
#             "emails": [billgate@yahoo.com, gatebill@pro.com],
#             "has_license": true
#         },
#         {
#             "name": "Jane White",
#             "phone_no": "+1 450 700 00",
#             "gender": "F",
#             "emails": [Janewhite-@yahoo.com, whitejane@pro.com],
#             "has_license": false
#         }
#     ]
# }
# '''

# person = json.loads(string)

# print(person["persons"])

# print(string)



response = '[{"city": "Lagos", "temperature": 29, "condition": "Sunny"},' \
'{"city": "PH", "temperature": 65, "condition": "Rainy"}]'

data = json.loads(response)
for c in data:
    print(c["city"])


list = {
    "name": "John",
    "age": 24,
    "single": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5}
    ]
}

print(json.dumps(list, indent=2, sort_keys=True))


c = camelcase.CamelCase()

text = 'Some text'

print(c.hump(text))


cowsay.cow("Hello Lase!!")