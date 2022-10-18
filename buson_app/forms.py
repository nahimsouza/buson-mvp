from django import forms


class EmployeeForm(forms.Form):

    name = forms.CharField(max_length=200)
    street = forms.CharField(max_length=100)
    number = forms.IntegerField()
    district = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=10)

class SettingsForm(forms.Form):
    
    number_of_routes = forms.IntegerField()
    min_number_of_passengers = forms.IntegerField()
    max_number_of_passengers = forms.IntegerField()
    max_number_of_bus_stops = forms.IntegerField()
    max_traveling_time = forms.IntegerField()
    max_distance_to_house = forms.IntegerField()
