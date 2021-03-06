# Generated by Django 3.2 on 2021-05-03 19:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='view_animals.shelter')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=1)),
                ('arrival_date', models.DateField(default=django.utils.timezone.now)),
                ('weight', models.IntegerField(default=1)),
                ('height', models.IntegerField(default=1)),
                ('special_signs', models.TextField(default='subscribe....')),
                ('is_arrived', models.BooleanField(default=True)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='view_animals.shelter')),
            ],
        ),
    ]
