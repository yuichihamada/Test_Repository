# Generated by Django 5.0.3 on 2024-03-29 08:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0002_add_student_school_prefecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'places',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 29, 8, 45, 29, 899455, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 29, 8, 45, 29, 899636, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ModelApp.places')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
    ]
