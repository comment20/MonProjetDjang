# Generated by Django 5.0.8 on 2024-08-25 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('francais', models.FloatField()),
                ('histoire_geo', models.FloatField()),
                ('anglais', models.FloatField()),
                ('mathematiques', models.FloatField()),
                ('physique_chimie', models.FloatField()),
            ],
        ),
    ]
