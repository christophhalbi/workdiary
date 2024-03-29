# Generated by Django 3.2.13 on 2022-06-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='incidenttag',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='repo',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='techstack',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
