# Generated by Django 4.1.3 on 2022-11-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=32)),
                ('weather', models.CharField(max_length=32)),
                ('temperature', models.IntegerField()),
            ],
            options={
                'verbose_name': '天気予報',
                'verbose_name_plural': '天気予報',
            },
        ),
    ]
