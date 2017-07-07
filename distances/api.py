
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.translation import ugettext as _

import json

from distances.matrix import get_distance

@require_http_methods(["POST"])
def distance(request):

	data = json.loads(request.body)

	try:
		lat1 = data['position1']['latitude']
		lng1 = data['position1']['longitude']

		lat2 = data['position2']['latitude']
		lng2 = data['position2']['longitude']

		return JsonResponse({
			'distance': get_distance(lat1, lng1, lat2, lng2, fetch_now=True)
		})

	except KeyError as ke:

		return JsonResponse({
			'debug': 'KeyError: ' + ke.__str__(),
			'message': _('%(field)s is missing') % {'field': ke.args[0]}
		}, status=406)

