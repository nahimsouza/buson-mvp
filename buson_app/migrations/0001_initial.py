# Generated by Django 4.1.2 on 2022-10-12 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100, verbose_name='Rua')),
                ('number', models.PositiveIntegerField(verbose_name='Número')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Bairro')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('postal_code', models.CharField(max_length=10, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=10, verbose_name='Placa')),
                ('num_seats', models.PositiveIntegerField(verbose_name='Capacidade')),
                ('num_seats_occupied', models.PositiveIntegerField(verbose_name='Ocupação')),
            ],
            options={
                'verbose_name': 'Bus',
                'verbose_name_plural': 'Buses',
            },
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='buson_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_routes', models.PositiveIntegerField(verbose_name='Número de Linhas')),
                ('min_number_of_passengers', models.PositiveIntegerField(verbose_name='Mínimo de Passageiros')),
                ('max_number_of_passengers', models.PositiveIntegerField(verbose_name='Máximo de Passageiros')),
                ('max_number_of_bus_stops', models.PositiveIntegerField(verbose_name='Máximo de Paradas')),
                ('max_traveling_time', models.TimeField(verbose_name='Tempo Máximo de Viagem')),
                ('max_distance_to_house', models.PositiveIntegerField(verbose_name='Distância Maxima até a Casa')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nome da Rota')),
                ('num_passengers', models.PositiveIntegerField(verbose_name='Número de passageiros')),
                ('direction', models.CharField(choices=[('I', 'Ida'), ('V', 'Volta'), ('N', 'Nenhuma das opções')], max_length=1)),
                ('stops', models.ManyToManyField(related_name='routes', to='buson_app.busstop')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('cpf', models.CharField(default='XXX.XXX.XXX-XX', max_length=14, verbose_name='CPF')),
                ('telephone', models.CharField(default='(XX) XXXX-XXXX', max_length=16, verbose_name='Telefone')),
                ('birthday', models.DateField(default='AAAA/MM/DD', verbose_name='Data de Nascimento')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buson_app.address', verbose_name='Endereço')),
                ('bus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='passengers', to='buson_app.bus')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='main_route',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_route', to='buson_app.route'),
        ),
        migrations.AddField(
            model_name='bus',
            name='return_route',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='return_route', to='buson_app.route'),
        ),
    ]
