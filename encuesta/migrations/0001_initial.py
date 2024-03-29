# Generated by Django 4.2.5 on 2023-09-12 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_texto', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion_texto', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuesta.pregunte')),
            ],
        ),
    ]
