from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from buson_app.forms import EmployeeForm, SettingsForm
from buson_app.models import Address, Employee, Settings


def index(request):
    return render(request, 'buson_app/index.html')

def configuracoes(request):
    settings = Settings.objects.first() or Settings()
    
    if request.method == 'POST':
        form = SettingsForm(request.POST)

        if form.is_valid():
            try:
                settings.number_of_routes = form['number_of_routes'].value()
                settings.min_number_of_passengers = form['min_number_of_passengers'].value()
                settings.max_number_of_passengers = form['max_number_of_passengers'].value()
                settings.max_number_of_bus_stops = form['max_number_of_bus_stops'].value()
                settings.max_traveling_time = form['max_traveling_time'].value()
                settings.max_distance_to_house = form['max_distance_to_house'].value()
                settings.save()
            except Exception as e:
                form = SettingsForm()
                return render(request, 'buson_app/configuracoes.html', {'form': form, 'settings': settings})

    form = SettingsForm()
    return render(request, 'buson_app/configuracoes.html', {'form': form, 'settings': settings})

def rotas(request):
    return render(request, 'buson_app/rotas.html')

def gerenciarColaborador(request):

    employee_list = Employee.objects.all()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            try:
                address = Address()
                address.street = form['street'].value()
                address.number = form['number'].value()
                address.district = form['district'].value()
                address.postal_code = form['postal_code'].value()
                address.city = form['city'].value()
                address.state = form['state'].value()
                address.save()

                employee = Employee()
                employee.name = form['name'].value()
                employee.address = address
                employee.save()

            except:
                form = EmployeeForm()
                return render(request, 'buson_app/colaboradores.html', {'form': form, 'list': employee_list})

    form = EmployeeForm()
    return render(request, 'buson_app/colaboradores.html', {'form': form, 'list': employee_list})
