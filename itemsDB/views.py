from django.shortcuts import render

from calculate.logic.item_manager import ITEM_TYPES

# from .__json_to_djangoDB import main


def items(request):
	context = {
		'title': 'Items Data Base',
		'item_types': ITEM_TYPES,
	}

	# main()

	return render(request, 'itemsDB/items.html', context)