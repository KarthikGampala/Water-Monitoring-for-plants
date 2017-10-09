# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Temperature(models.Model):
	tem_value=models.CharField(max_length=250)
	def __str__(self):
		return self.tem_value
class Humidity(models.Model):
	hum_value=models.CharField(max_length=250)
	def __str__(self):
		return self.hum_value
class Moisture(models.Model):
	moi_value=models.CharField(max_length=250)
	def __str__(self):
		return self.moi_value
class WaterLevel(models.Model):
	level_value=models.CharField(max_length=250)
	def __str__(self):
		return self.level_value	
