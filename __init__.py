import json
import traceback
from block import Block

# def list_to_dict_test():
#     list_test = [("Black", "Nagsia"), ("White", "Honoka"), ("Luminous", "Hikari"), ("Asphalt", "Ishino")]
#     list_test.sort()

#     dict_test = dict(list_test)

#     print(dict_test)

#     with open('write_to_json.json', 'w') as outfile:
#         json.dump(dict_test, outfile, indent=2)

def read_lang():
    dir_to_lang = "C:\\Users\\MP\\Documents\\py\\AllTheCompressed\\src\\generated\\resources\\assets\\allthecompressed\\lang\\en_us.json"

    file_read_lang = open(dir_to_lang, 'r')
    dict_lang = json.load(file_read_lang)

    # print (dict_lang)
    # for e in dict_lang:
        # print("e: " + str(e))

    return dict_lang

def create_list_from_block(block: Block):
    build_list = list()
    for i in range(9):
        # Tuple for block name and localized name
        block_name_full = "".join(["block", ".allthecompressed.", block.block_name, "_", str(i+1), "x"])
        block_name_local = "".join([block.block_name_local, " ", str(i+1), "x"])
        build_pair = (block_name_full, block_name_local)
        build_list.append(build_pair)
    return build_list

dict_lang: dict = read_lang()
list_test = create_list_from_block(Block("minecraft","azalea_planks", "Azalea Planks"))



list_sort_dict_lang = list(dict_lang.items()) # What does this return??
print(list_sort_dict_lang)

build_list = list_sort_dict_lang + list_test

# View list before sort
for i in build_list:
    print("[00] " + str(i))
# Sort
build_list.sort()

# View list after sort
for i in build_list:
    print("[01] " + str(i))

dict_built = dict(build_list)
print(dict_built.items())

with open('write_here.json','w') as outfile:
    json.dump(dict_built, outfile, indent=2)