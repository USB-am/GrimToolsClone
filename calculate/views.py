from django.shortcuts import render

from calculate.logic import item_manager as ItemManager
# ITEM_TYPES, EQUIP_CELL, convert_json_fields_to_obj
from itemsDB.models import *

from json import loads


def calculate(request):
	context = {
		'title': 'Calculate page',
		'item_types': ItemManager.ITEM_TYPES,
	}

	return render(request, 'calculate/calculate.html', context)


def getItemsByCategory(request):
	if request.method != 'POST':
		raise AttributeError('Send request to this URL for apply answer!')

	data = loads(request.body.decode())
	print(f'Client send [{type(data)}] {data}')
	category = data.get('item_type')

	if category is None:
		raise AttributeError('Uncorrected request!')

	items = ItemManager.EQUIP_CELL[category][0].objects.all()[:75]
	ItemManager.convert_json_fields_to_obj(items)
	context = {
		'title': f'{category.title()} - Calculate page',
		'items_types': ItemManager.ITEM_TYPES,
		'items': items,
	}

	return render(request, 'calculate/items_list.html', context)