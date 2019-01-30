# Generated by Django 2.1.3 on 2019-01-30 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bps', '0002_auto_20190130_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('floorID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('floorNo', models.IntegerField()),
                ('buildID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bps.Building')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='floor',
            unique_together={('buildID', 'floorID')},
        ),
    ]
