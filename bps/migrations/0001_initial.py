# Generated by Django 2.1.3 on 2019-03-02 12:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('buildID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('buildName', models.CharField(max_length=100)),
                ('buildFloors', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('floorID', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('floorNo', models.IntegerField()),
                ('floorImageLink', models.URLField(blank=True, null=True)),
                ('buildID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bps.Building')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='floor',
            unique_together={('buildID', 'floorID')},
        ),
    ]
