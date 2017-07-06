import math

from distances.models import Sector, Distance
from distances.google_api import distance as gdistance

from django.conf import settings

def _swap_sectors(s1, s2):
	if s1.id < s2.id:
		return (s1, s2)
	else:
		return (s2, s1)


def get_distance(lat1, lng1, lat2, lng2, fetch_now=False):

	s1 = Sector.get_or_create(lat1, lng1)
	s2 = Sector.get_or_create(lat2, lng2)

	s1, s2 = _swap_sectors(s1, s2)

	distance = Distance.get_or_create(s1, s2)

	if fetch_now:
		distance.distance_km = gdistance(s1.latitude_with_road, s1.longitude_with_road, s2.latitude_with_road, s2.longitude_with_road)
		distance.save()

	if distance.distance_km is None:
		return distance.distance_km
	else:
		return (math.floor(distance.distance_km/settings.DISTANCES_AVERAGING_KM) + 1)*settings.DISTANCES_AVERAGING_KM
