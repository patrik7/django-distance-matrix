from xml.etree.ElementTree import fromstring, XMLParser, TreeBuilder

import sys

from datetime import timedelta
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.db import transaction, IntegrityError

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils import timezone

from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash

import json
import requests
from rollbar import report_exc_info

from email_campaigns.models import Campaign, EmailTemplate
from quoting import google_api
from quoting.models import json_user, Product, Animal, Quote, PRODUCT_LIFETIME, Address
from livestock.models import SubCategory, Category
from one_click_auth.models import Token

from email_campaigns.utils import schedule_send_email

from xmljson import badgerfish as bf

from django.conf import settings
import time

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

