from django.contrib import admin

from buson_app.models import Address, Bus, BusStop, Employee, Route, Settings

admin.site.register(Address)
admin.site.register(BusStop)
admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Employee)
admin.site.register(Settings)
