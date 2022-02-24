from django.shortcuts import render

from calculate.logic.item_manager import ITEM_TYPES

def calculate(request):
	if request.method == 'POST':
		print(f'Cliend send {request.body}\n\n')
	context = {
		'title': 'Calculate page',
		'item_types': ITEM_TYPES
	}

	return render(request, 'calculate/calculate.html', context)