from django.db import models

# Create your models here.
class Route(models.Model):
    Directions = models.TextChoices('Ida', 'Volta')
    name = models.CharField(max_length=20)
    direction = models.CharField(max_length=10, choices=Directions.choices)


class BusStop(models.Model):
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)


class Employee(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    district = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    bus_stop = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True)    


class Settings(models.Model):
    number_of_routes = models.IntegerField()
    min_number_of_passengers = models.IntegerField()
    max_number_of_passengers = models.IntegerField()
    max_number_of_bus_stops = models.IntegerField()
    max_traveling_time = models.IntegerField()
    max_distance_to_house = models.IntegerField()

