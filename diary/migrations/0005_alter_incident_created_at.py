# Generated by Django 3.2.13 on 2022-07-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20220624_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='created_at',
            field=models.DateField(),
        ),
    ]
