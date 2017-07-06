# -*- coding: utf-8
from django.core.management.base import BaseCommand

from distances.models import Distance

from rollbar import report_exc_info

from distances.google_api import distance


class Command(BaseCommand):
	help = 'Fetch missing distances from google'

	def handle(self, *args, **options):
		for d in Distance.objects.filter(distance_km=None):
			try:
				d.distance_km = distance(d.sector1.latitude_with_road, d.sector1.longitude_with_road, d.sector2.latitude_with_road, d.sector2.longitude_with_road)
				d.save()
			except:
				report_exc_info()