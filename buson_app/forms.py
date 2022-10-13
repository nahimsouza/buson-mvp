from django import forms


class EmployeeForm(forms.Form):

    name = forms.CharField(max_length=200)
    street = forms.CharField(max_length=100)
    number = forms.IntegerField()
    district = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=10)
    cpf = forms.CharField(max_length=14)
    telephone = forms.CharField(max_length=16)
    birthday = forms.DateField()
