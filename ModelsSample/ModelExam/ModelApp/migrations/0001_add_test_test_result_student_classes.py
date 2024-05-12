# Generated by Django 5.0.3 on 2024-04-01 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tests',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.classes')),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Test_results',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.students')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.tests')),
            ],
            options={
                'db_table': 'test_results',
            },
        ),
    ]