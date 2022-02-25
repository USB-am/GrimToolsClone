# -*- coding: utf-8 -*-

from json import loads

from itemsDB.models import *



JSON_FIELDS = (
	'base_stat',
	'set_parts',
	'skill_params',
	'access_condition',
	'image'
)


ITEM_TYPES = {
	'weapon': (Axe, Axe2h, Dagger, Mace, Mace2h, Offhand, Ranged, Ranged2h, Scepter,
		Shield, Sword, Sword2h
	),
	'armors': (Belt, Boots, ChestArmor, Gloves, Helmet, Pants, Shoulder),
	'jewelry': (Amulet, Medal, Ring)
}

EQUIP_CELL = {
	'weapon-left': (Axe, Axe2h, Dagger, Mace, Mace2h, Offhand, Ranged, Ranged2h, Scepter,
		Shield, Sword, Sword2h),
	'weapon-right': (Axe, Axe2h, Dagger, Mace, Mace2h, Offhand, Ranged, Ranged2h, Scepter,
		Shield, Sword, Sword2h),
	'helm': (Helmet,),
	'ring-left': (Ring,),
	'ring-right': (Ring,),
	'amulet': (Amulet,),
	'chest-armor': (ChestArmor,),
	'legs': (Pants,),
	'shoulders': (Shoulder,),
	'gloves': (Gloves,),
	'boots': (Boots,),
	'relic': (Relic,),
	'medal': (Medal,),
	'belt': (Belt,)
}


def str_to_json(item, item_param_name):
	val = item.__dict__[item_param_name]
	if val is not None:
		item.__dict__[item_param_name] = loads(
			r'{}'.format(val.replace('\'', '"'))
		)


def convert_json_fields_to_obj(items):
	for item in items:
		[str_to_json(item, param) for param in JSON_FIELDS]