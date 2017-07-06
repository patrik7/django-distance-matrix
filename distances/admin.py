from django.contrib import admin

# Register your models here.
from distances.models import Sector


class SectorAdmin(admin.ModelAdmin):
	list_display = ['id', 'x', 'y', 'latitude_with_road', 'longitude_with_road']


#admin.site.register(Sector, SectorAdmin)

