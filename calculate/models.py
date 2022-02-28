from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator#, MinValueValidator

from itemsDB.models import *


class MasterClass(models.Model):
	title = models.CharField(max_length=50, verbose_name='Название')
	point_count = models.PositiveIntegerField(
		verbose_name='Points', default=0,
		validators=[MaxValueValidator(50)]
	)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Класс'
		verbose_name_plural = 'Классы'


class Mastery(models.Model):
	title = models.CharField(max_length=50, verbose_name='Название')
	master_class_1 = models.ForeignKey(MasterClass,
		verbose_name='Мастерство 1', on_delete=models.SET_NULL,
		null=True, blank=True, related_name='+')
	master_class_2 = models.ForeignKey(MasterClass,
		verbose_name='Мастерство 2', on_delete=models.SET_NULL,
		null=True, blank=True, related_name='+')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Мастерство'
		verbose_name_plural = 'Мастерства'
		ordering = ['title']


class Person(models.Model):
	author = models.ForeignKey(User, verbose_name='Автор',
		on_delete=models.CASCADE)
	mastery_class = models.ForeignKey(Mastery, verbose_name='Мастерство',
		on_delete=models.SET_NULL, blank=True, null=True)
	at_create = models.DateTimeField(auto_now=True, verbose_name='Дата создание')
	weapon_left = models.ForeignKey(Axe, verbose_name='Левая рука',
		on_delete=models.CASCADE, blank=True, null=True)
	weapon_right = models.ForeignKey(Shield, verbose_name='Правая рука',
		on_delete=models.CASCADE, blank=True, null=True)
	helmet = models.ForeignKey(Helmet, verbose_name='Шлем',
		on_delete=models.CASCADE, blank=True, null=True)
	ring_left = models.ForeignKey(Ring, verbose_name='Левое кольцо',
		on_delete=models.CASCADE, blank=True, null=True, related_name='+')
	ring_right = models.ForeignKey(Ring, verbose_name='Правое кольцо',
		on_delete=models.CASCADE, blank=True, null=True, related_name='+')
	amulet = models.ForeignKey(Amulet, verbose_name='Амулет',
		on_delete=models.CASCADE, blank=True, null=True)
	chest_armor = models.ForeignKey(ChestArmor, verbose_name='Нагрудная броня',
		on_delete=models.CASCADE, blank=True, null=True)
	pants = models.ForeignKey(Pants, verbose_name='Поножи',
		on_delete=models.CASCADE, blank=True, null=True)
	shoulder = models.ForeignKey(Shoulder, verbose_name='Наплечник',
		on_delete=models.CASCADE, blank=True, null=True)
	gloves = models.ForeignKey(Gloves, verbose_name='Перчатки',
		on_delete=models.CASCADE, blank=True, null=True)
	boots = models.ForeignKey(Boots, verbose_name='Ботинки',
		on_delete=models.CASCADE, blank=True, null=True)
	relic = models.ForeignKey(Relic, verbose_name='Реликвия',
		on_delete=models.CASCADE, blank=True, null=True)
	medal = models.ForeignKey(Medal, verbose_name='Медаль',
		on_delete=models.CASCADE, blank=True, null=True)
	belt = models.ForeignKey(Belt, verbose_name='Пояс',
		on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return f'Person ({self.pk})' # self.mastery_class.title

	class Meta:
		verbose_name = 'Персонаж'
		verbose_name_plural = 'Персонажи'
		ordering = ['at_create']