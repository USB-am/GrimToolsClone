# -*- coding: utf-8 -*-

__all__ = ('Amulet', 'Augment', 'Axe', 'Axe2h', 'Belt', 'Boots', 'ChestArmor',
	'Dagger', 'Gloves', 'Helmet', 'Mace', 'Mace2h', 'Medal', 'Offhand',
	'Pants', 'Ranged', 'Ranged2h', 'Relic', 'Ring', 'Scepter', 'Shield',
	'Shoulder', 'Sword', 'Sword2h', 'Item')

from django.db import models


class Item(models.Model):
	name = models.CharField(
		verbose_name='Название',
		max_length=255)
	description = models.TextField(
		verbose_name='История',
		blank=True,
		null=True)
	type = models.CharField(
		verbose_name='Тип предмета',
		max_length=255)
	equip_type = models.CharField(
		verbose_name='Категория',
		max_length=255)
	color = models.CharField(
		verbose_name='Цвет предмета',
		max_length=255)
	base_stat = models.TextField(
		verbose_name='Базовые характеристики',
		blank=True,
		null=True)
	skill_params = models.TextField(
		verbose_name='Дополнительные характеристики',
		blank=True,
		null=True)
	set_name = models.CharField(
		verbose_name='Название комплекта',
		max_length=255,
		null=True)
	set_parts = models.TextField(
		verbose_name='Части комплекта',
		blank=True,
		null=True)
	access_condition = models.TextField(
		verbose_name='Условия доступа',
		blank=True,
		null=True)
	dlc_name = models.CharField(
		verbose_name='Название дополнения',
		max_length=255,
		null=True)
	image = models.TextField(
		verbose_name='Картинка',
		blank=True,
		null=True)

	def __str__(self) -> str:
		return self.name.title()

	def get_name(self) -> str:
		return self.name.title()

	class Meta:
		verbose_name = 'Предмет'
		verbose_name_plural = 'Предметы'
		ordering = ['color', 'name']


class Amulet(Item):
	category = 'juwelry'
	class Meta:
		verbose_name = 'Амулет'
		verbose_name_plural = 'Амулеты'

class Augment(Item):
	category = 'other'
	class Meta:
		verbose_name = 'Присыпка'
		verbose_name_plural = 'Присыпки'

class Axe(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Топор'
		verbose_name_plural = 'Топоры'

class Axe2h(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Двуручный топор'
		verbose_name_plural = 'Двуручные топоры'

class Belt(Item):
	category = 'armor'
	class Meta:
		verbose_name = 'Пояс'
		verbose_name_plural = 'Пояса'

class Boots(Item):
	category = 'armor'
	class Meta:
		verbose_name = 'Ботинки'
		verbose_name_plural = 'Ботинки'

class ChestArmor(Item):
	category = 'armor'
	class Meta:
		verbose_name = 'Нагрудная броня'
		verbose_name_plural = 'Нагрудная броня'

class Dagger(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Кинжал'
		verbose_name_plural = 'Кинжалы'

class Gloves(Item):
	category = 'armor'
	class Meta:
		verbose_name = 'Перчатки'
		verbose_name_plural = 'Перчатки'

class Helmet(Item):
	category = 'armor'
	class Meta:
		verbose_name = 'Шлем'
		verbose_name_plural = 'Шлемы'

class Mace(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Булава'
		verbose_name_plural = 'Булавы'

class Mace2h(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Двуручная булава'
		verbose_name_plural = 'Двуручные булавы'

class Medal(Item):
	category = 'juwelry'
	class Meta:
		verbose_name = 'Медаль'
		verbose_name_plural = 'Медали'

class Offhand(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'

class Pants(Item):
	category = 'armor'
	class Meta:
		verbose_name = 'Штаны'
		verbose_name_plural = 'Штаны'

class Ranged(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Пистолет'
		verbose_name_plural = 'Пистолеты'

class Ranged2h(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Ружье'
		verbose_name_plural = 'Ружья'

class Relic(Item):
	category = 'other'
	class Meta:
		verbose_name = 'Реликвия'
		verbose_name_plural = 'Реликвии'

class Ring(Item):
	category = 'juwelry'
	class Meta:
		verbose_name = 'Кольцо'
		verbose_name_plural = 'Кольца'

class Scepter(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Скипетр'
		verbose_name_plural = 'Скипетры'

class Shield(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Щит'
		verbose_name_plural = 'Щиты'

class Shoulder(Item):
	category = 'armor'
	class Meta:
		verbose_name = 'Наплечник'
		verbose_name_plural = 'Наплечники'

class Sword(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Меч'
		verbose_name_plural = 'Мечи'

class Sword2h(Item):
	category = 'weapon'
	class Meta:
		verbose_name = 'Двуручный меч'
		verbose_name_plural = 'Двуручные мечи'

class Components(Item):
	category = 'other'
	class Meta:
		verbose_name = 'Компонент'
		verbose_name_plural = 'Компоненты'