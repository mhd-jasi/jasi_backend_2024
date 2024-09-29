# Generated by Django 5.1 on 2024-09-25 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=12)),
                ('Address', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('Appointment_Doctor', models.CharField(max_length=100)),
                ('Appointment_Date', models.DateField()),
                ('Appointment_Time', models.TimeField()),
                ('Token', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=15)),
                ('Phone', models.CharField(max_length=12)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Username', models.CharField(max_length=55)),
                ('Address', models.TextField()),
                ('Department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=12)),
                ('Age', models.IntegerField()),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=154)),
                ('Gender', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=12)),
                ('Email', models.EmailField(max_length=254)),
                ('Category', models.CharField(max_length=50)),
                ('Address', models.TextField()),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=12)),
                ('Email', models.EmailField(max_length=254)),
                ('Username', models.CharField(max_length=50)),
                ('Address', models.TextField()),
                ('Department', models.CharField(max_length=50)),
            ],
        ),
    ]
