# Generated by Django 2.1.15 on 2020-03-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricerca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grafo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='grafo',
            name='published_date',
        ),
        migrations.AddField(
            model_name='grafo',
            name='data_PC',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='grafo',
            name='tipo',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='grafo',
            name='chiave',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]