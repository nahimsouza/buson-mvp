from django.db import models


class Address(models.Model):

    street = models.CharField(max_length=100, verbose_name='Rua')
    number = models.PositiveIntegerField(verbose_name='Número')
    district = models.CharField(max_length=100, verbose_name='Bairro')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    state = models.CharField(max_length=50, verbose_name='Estado')
    postal_code = models.CharField(max_length=10, verbose_name='CEP')

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return str(self.street) + ', ' + str(self.number) + ' - ' + \
            str(self.district) + ', ' + \
            str(self.city) + ' - ' + str(self.state)


class BusStop(models.Model):

    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name='points')
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')

    def __str__(self):
        return str(self.address)


class Route(models.Model):

    DIRECTIONS_CHOICES = (
        ('I', 'Ida'),
        ('V', 'Volta'),
        ('N', 'Nenhuma das opções')
    )

    name = models.CharField(max_length=20, verbose_name='Nome da Rota')
    num_passengers = models.PositiveIntegerField(
        verbose_name='Número de passageiros')
    direction = models.CharField(
        max_length=1, choices=DIRECTIONS_CHOICES, blank=False, null=False)
    stops = models.ManyToManyField(BusStop, related_name='routes')

    def __str__(self):
        return self.name


class Bus(models.Model):

    license_plate = models.CharField(max_length=10, verbose_name='Placa')
    num_seats = models.PositiveIntegerField(verbose_name='Capacidade')
    num_seats_occupied = models.PositiveIntegerField(verbose_name='Ocupação')
    main_route = models.OneToOneField(
        Route, on_delete=models.SET_NULL, null=True, blank=True, related_name='main_route')
    return_route = models.OneToOneField(
        Route, on_delete=models.SET_NULL, null=True, blank=True, related_name='return_route')

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'

    def __str__(self):
        return self.license_plate


class Employee(models.Model):

    name = models.CharField(max_length=200, verbose_name='Nome')
    cpf = models.CharField(
        max_length=14, null=True, blank=True, default='XXX.XXX.XXX-XX', verbose_name='CPF')
    telephone = models.CharField(
        max_length=16, null=True, blank=True, default='(XX) XXXX-XXXX', verbose_name='Telefone')
    birthday = models.DateField(
        null=True, blank=True, verbose_name='Data de Nascimento')
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name='Endereço')
    bus = models.ForeignKey(Bus, on_delete=models.PROTECT,
                            null=True, blank=True, related_name='passengers')
    bus_stop = models.ForeignKey(BusStop, on_delete=models.PROTECT,
                                 null=True, blank=True, related_name='employees')

    def __str__(self):
        return self.name


class Settings(models.Model):

    number_of_routes = models.PositiveIntegerField(
        verbose_name='Número de Linhas')
    min_number_of_passengers = models.PositiveIntegerField(
        verbose_name='Mínimo de Passageiros')
    max_number_of_passengers = models.PositiveIntegerField(
        verbose_name='Máximo de Passageiros')
    max_number_of_bus_stops = models.PositiveIntegerField(
        verbose_name='Máximo de Paradas')
    max_traveling_time = models.PositiveIntegerField(
        verbose_name='Tempo Máximo de Viagem')
    max_distance_to_house = models.PositiveIntegerField(
        verbose_name='Distância Maxima até a Casa')

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'
