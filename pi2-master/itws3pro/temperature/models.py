# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Plants(models.Model):
	plant_id = models.AutoField(primary_key=True)
	latitude = models.FloatField(default=None)
	longitude = models.FloatField(default=None)
	
	def __str__(self):
		return str(self.plant_id)

class Temperature(models.Model):
	plant_id = models.ForeignKey(Plants,blank=True,null = True)
	tem_value=models.CharField(max_length=250)
	hum_value=models.CharField(max_length=250)
	moist_value=models.CharField(max_length=250)
	lev_value=models.CharField(max_length=250)
	rain_value=models.CharField(max_length=250)
	def __str__(self):
		return str(self.tem_value)
