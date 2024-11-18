import json

adat = {"nev": "Anna", "kor" : 25, "varos": "Bp"}
json_string = json.dumps(adat)



json_adat = '{"nev": "Anna", "kor" : 25, "varos": "Bp"}'
adat = json.loads(json_adat)
# print(adat.get("nev"))


with open("adat.json", "w", encoding='utf-8') as file:
    json.dump(adat, file, indent=4)


with open("adat.json", "r", encoding='utf-8') as file:
    adat = json.load(file)
    # print(type(adat))
    # print(adat.get("kor"))


sample_json = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sample_json)
# print(type(data))
# print(data['company']['employee']['payble']['salary'])


json_list = [
   {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },
   {
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }
]

data = []
try:
    data = json.loads(json_list)
except Exception as e:
    # print(e)
    data.append(f'e: {e}')


data_list = [item.get('name') for item in json_list]
# print(data_list)


j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
j_list = [{'4': 5, '6': 7, '1': 3, '2': 4}]
print(j_str)

print(json.dumps(j_str, sort_keys=True, indent=4))

