# Generated by Django 4.2.5 on 2023-09-12 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pregunte',
            new_name='Pregunta',
        ),
    ]
