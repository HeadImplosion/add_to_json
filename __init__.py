import json
import traceback

list_test = [("Black", "Nagsia"), ("White", "Honoka"), ("Luminous", "Hikari"), ("Asphalt", "Ishino")]
list_test.sort()

dict_test = dict(list_test)

print(dict_test)

with open('write_to_json.json', 'w') as outfile:
    json.dump(dict_test, outfile, indent=2)