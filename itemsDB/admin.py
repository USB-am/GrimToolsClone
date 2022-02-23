from django.contrib import admin

from .models import *


item_list = [Amulet, Augment, Axe, Axe2h, Belt, Boots,
	ChestArmor, Dagger, Gloves, Helmet, Mace, Mace2h,
	Medal, Offhand, Pants, Ranged, Ranged2h, Relic,
	Ring, Scepter, Shield, Shoulder, Sword, Sword2h]


class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'type', 'color', 'set_name', 'dlc_name')
	list_display_links = ('name', 'type', 'color', 'set_name', 'dlc_name')
	search_fields = ('name', 'type', 'color')


[admin.site.register(item, ItemAdmin) for item in item_list]