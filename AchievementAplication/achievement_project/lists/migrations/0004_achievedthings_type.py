# Generated by Django 5.0.4 on 2024-05-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_alter_achievedthings_name_alter_todothings_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievedthings',
            name='type',
            field=models.CharField(default=None, max_length=15),
        ),
    ]