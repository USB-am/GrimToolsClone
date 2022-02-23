# -*- coding: utf-8 -*-

from .models import *
import os, json


name_to_class = {
	'amulets': Amulet,
	'augments': Augment,
	'axes': Axe,
	'axes2h': Axe2h,
	'belts': Belt,
	'boots': Boots,
	'chest': ChestArmor,
	'daggers': Dagger,
	'gloves': Gloves,
	'helms': Helmet,
	'maces': Mace,
	'maces2h': Mace2h,
	'medals': Medal,
	'offhands': Offhand,
	'pants': Pants,
	'ranged1h': Ranged,
	'ranged2h': Ranged2h,
	'relics': Relic,
	'rings': Ring,
	'scepters': Scepter,
	'shields': Shield,
	'shoulders': Shoulder,
	'swords': Sword,
	'swords2h': Sword2h
}

COLOR_DICT = {
	'common': 0,
	'magical': 1,
	'magic': 1,
	'rare': 2,
	'epic': 3,
	'legendary': 4,
}


def main():
	path_to_json_files = os.path.join(os.getcwd(), 'itemsDB', 'temp_db')

	if not os.path.exists(path_to_json_files):
		raise OSError(f'File "{path_to_json_files}" not found!')

	files = os.listdir(path_to_json_files)
	item_list = []

	for file in files:
		path_to_json = os.path.join(path_to_json_files, file)

		items_file = open(path_to_json, mode='r', encoding='utf-8')
		items = json.load(items_file)
		items_file.close()

		item_class = name_to_class[file.split('.')[0]]

		for item_dict in items:
			item_dict['color'] = COLOR_DICT[item_dict['color']]
			item = item_class(**item_dict)
			# print(f'Item: {item}\n\nItem dict: {item_dict}')
			# exit()
			item.save()