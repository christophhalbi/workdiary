# Generated by Django 4.0.4 on 2022-07-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_entry_description_alter_incident_meltdown_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]