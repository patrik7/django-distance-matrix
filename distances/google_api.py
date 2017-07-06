# -*- coding: utf-8
import json

import googlemaps
import math

from django.conf import settings
from quoting.models import Address, Company, Product
import logging

logger = logging.getLogger('google_api')

if not settings.IS_TEST:
	gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
else:
	gmaps = None


def distance(lat1, lng1, lat2, lng2):
	if gmaps is None:
		#MOCK

		return 120
	else:

		geocode_results = gmaps.distance_matrix(mode='driving',origins='%f,%f' % (lat1, lng1), destinations='%f,%f' % (lat2, lng2))

		if geocode_results.get('status') == 'OK' and len(geocode_results.get('rows', [])) > 0:
			r = geocode_results['rows'][0]

			e = r['elements'][0]

			d = math.floor(e['distance']['value']/1000)

			logger.info("Fetched distance for sector %d km" % d)

			return d

		return None

