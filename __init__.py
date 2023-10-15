import json
import traceback
from block import Block

def read_lang():
  dir_to_lang = "en_us.json"

  file_read_lang = open(dir_to_lang, 'r')
  dict_lang = json.load(file_read_lang)

  return dict_lang

# Add both "block." and "item." tuples to list
def add_block_to_local_list(block: Block):
  build_list = list()
  for i in range(9):
    # Tuple for block name and localized name
    block_name_full = "".join(["block", ".allthecompressed.", block.block_name, "_", str(i+1), "x"])
    item_name_full = "".join(["item", ".allthecompressed.", block.block_name, "_", str(i+1), "x"])
    block_name_local = "".join([block.block_name_local, " ", str(i+1), "x"])

    build_pair_block = (block_name_full, block_name_local)
    build_pair_item = (item_name_full, block_name_local)
    build_list.append(build_pair_block)
    build_list.append(build_pair_item)
  return build_list

# Read en_us.json localization file
dict_lang = read_lang()

# Try adding a block
# list_test = create_list_from_block(Block("minecraft","azalea_planks", "Azalea Planks"))

# def append_block_to_list(block: Block):

#   # List of all block. and item. entries from 1x to 9x
#   list_append = create_append_list(block)
#   return list_append

#   # Return list of current en_us.json file
#   list_sort_dict_lang = list(dict_lang.items()) # What does this return??
#   print(list_sort_dict_lang)

#   # Add local list to existing en_us.json list
#   build_list = list_sort_dict_lang + list_append


#   # Sort
#   build_list.sort()

#   dict_built = dict(build_list)
#   print(dict_built.items())

#   # with open('write_here.json','w') as outfile:
#     # json.dump(dict_built, outfile, indent=2)

# Compile all required blocks first.
def add_blocks_to_list(all_input_blocks: list[Block]):
  build_list = []
  for block in all_input_blocks:
    build_list += add_block_to_local_list(block)

  return build_list

# Add to existing list
def append_existing_localization(block_list: list[Block]):
  list_from_dict = list(read_lang().items())
  full_list = list_from_dict + block_list
  return full_list

# THEN sort
# Finally, convert back to dict
def list_to_sorted_dict(list):
  hold_list = list 
  hold_list.sort()
  pass
  return dict(hold_list)

def write_to_json(dict):
  with open('write_here.json', 'w') as outfile:
    json.dump(dict, outfile, indent=2)

block_input = Block("minecraft", "tinted_glass", "Tinted Glass")
block_input2 = Block("minecraft", "chiseled_glass", "Chiseled Glass")
block_input3 = Block("puellamagi", "kyubey_remains", "Kyubey Remains")

block_list = [block_input, block_input2, block_input3]

list_to_append = add_blocks_to_list(block_list)
updated_list = append_existing_localization(list_to_append)
dict_sorted = list_to_sorted_dict(updated_list)

write_to_json(dict_sorted)


# write_block_to_json(dict_write_to_json)
