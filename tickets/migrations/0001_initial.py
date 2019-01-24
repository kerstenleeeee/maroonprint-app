# Generated by Django 2.1.3 on 2018-11-25 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('busID', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Bus_Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Bus_Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentTerminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driverID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('displayName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('userID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('displayName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('terminalID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('terminalName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('tripID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('departureDate', models.DateField()),
                ('departureTime', models.TimeField()),
                ('seatsLeft', models.IntegerField()),
                ('destinationTerminal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='destinationTerminal', to='tickets.Terminal')),
                ('sourceTerminal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sourceTerminal', to='tickets.Terminal')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='tripID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Trip'),
        ),
        migrations.AddField(
            model_name='rating',
            name='userID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Passenger'),
        ),
        migrations.AddField(
            model_name='currentterminal',
            name='terminalID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Terminal'),
        ),
        migrations.AddField(
            model_name='currentterminal',
            name='tripID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Trip'),
        ),
        migrations.AddField(
            model_name='bus_trip',
            name='tripID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Trip'),
        ),
        migrations.AddField(
            model_name='bus_driver',
            name='driverID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Driver'),
        ),
        migrations.AddField(
            model_name='booking',
            name='tripID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Trip'),
        ),
        migrations.AddField(
            model_name='booking',
            name='userID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tickets.Passenger'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('userID', 'tripID')},
        ),
        migrations.AlterUniqueTogether(
            name='currentterminal',
            unique_together={('terminalID', 'tripID')},
        ),
        migrations.AlterUniqueTogether(
            name='bus_trip',
            unique_together={('busID', 'tripID')},
        ),
        migrations.AlterUniqueTogether(
            name='bus_driver',
            unique_together={('busID', 'driverID')},
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('userID', 'tripID')},
        ),
    ]
