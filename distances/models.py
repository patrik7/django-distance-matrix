from __future__ import unicode_literals

import math
from django.db import models
from django.conf import settings


class Sector(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()

	latitude_with_road = models.FloatField()
	longitude_with_road = models.FloatField()

	class Meta:
		unique_together = [
			['x', 'y']
		]

	@staticmethod
	def get_or_create(lat, lng):
		x = math.floor(lng/settings.DISTANCES_RESOLUTION_LAT) #longitude resoultion wors differently on various latitudes - TODO, address later
		y = math.floor(lat/settings.DISTANCES_RESOLUTION_LNG)

		try:
			s = Sector.objects.get(x=x,y=y)
		except Sector.DoesNotExist:
			s = Sector(x=x, y=y, latitude_with_road=lat, longitude_with_road=lng)
			s.save()

		return s


class Distance(models.Model):
	sector1 = models.ForeignKey(Sector,related_name='distance1')
	sector2 = models.ForeignKey(Sector,related_name='distance2')

	distance_km = models.IntegerField(null=True,blank=True)

	class Meta:
		index_together = [
			['sector1', 'sector2']
		]

	@staticmethod
	def get_or_create(sector1, sector2):
		try:
			d = Distance.objects.get(sector1=sector1, sector2=sector2)
		except Distance.DoesNotExist:
			d = Distance(sector1=sector1, sector2=sector2,distance_km=None)
			d.save()

		return d
