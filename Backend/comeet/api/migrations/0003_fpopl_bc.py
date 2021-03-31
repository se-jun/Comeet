# Generated by Django 3.0.5 on 2021-03-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_gugun'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fpopl_BC',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=20)),
                ('per_time', models.CharField(max_length=20)),
                ('age_range', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('gugun', models.CharField(max_length=10)),
                ('popl', models.IntegerField()),
            ],
        ),
    ]