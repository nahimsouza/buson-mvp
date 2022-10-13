from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from buson_app.forms import EmployeeForm
from buson_app.models import Address, Employee


def index(request):
    return render(request, 'buson_app/index.html')

def configuracoes(request):
    return render(request, 'buson_app/configuracoes.html')

def rotas(request):
    return render(request, 'buson_app/rotas.html')

def gerenciarColaborador(request):
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
                employee.cpf = form['cpf'].value()
                employee.telephone = form['telephone'].value()
                employee.birthday = form['birthday'].value()
                employee.address = address
                employee.save()

            except:
                form = EmployeeForm()
                return render(request, 'buson_app/colaboradores.html', {'form': form})

    form = EmployeeForm()
    return render(request, 'buson_app/colaboradores.html', {'form': form})
